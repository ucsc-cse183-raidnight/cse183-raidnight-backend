"""
This file contains the A*-based matchmaking algorithm. It operates in 2 phases:

1. Find potential timespans (naive)
2. Assign players to roles
"""
import collections
import datetime
import math

import pytz

from . import constants, schemas
from .utils import get_game_signup_full

RULE_BREAK_COST = 30
CANNOT_PLAY_COST = 9999
DEBUG_ASTAR = True  # if true, prints debug info


def load_all_signups(db, session_id):
    """
    Utility: given the game session id, load all signups

    :rtype: list[schemas.GameSignupFull]
    """
    out = []
    for signup in db(db.game_signups.session_id == session_id).select():
        out.append(get_game_signup_full(db, signup.id))
    return out


def find_timespans(signups):
    """
    Given a list of signups, return a list of tuples (start, stop, signup_ids)

    Note that if stop < start, the interval spans a week reset

    :type signups: list[schemas.GameSignupFull]
    """
    # convert all times to utc, and mark offsets where availability changes
    event_offsets = set()
    for signup in signups:
        for time in signup.times[:]:  # iterate over a copy so we can modify the original
            try:
                tzinfo = pytz.timezone(time.timezone)
                # get offset in hours
                utc_offset = tzinfo.utcoffset(datetime.datetime.now()) / datetime.timedelta(hours=1)
            except pytz.UnknownTimeZoneError:
                try:
                    utc_offset = float(time.timezone)
                except ValueError:
                    print(f"WARN: Cannot understand time zone {time.timezone!r}")
                    utc_offset = -7  # oh well, you live in california now

            time.offset -= utc_offset
            time.timezone = "Etc/UTC"
            # ---- normalize ----
            # make offset fall in week
            if (time.offset <= 0) or (time.offset >= constants.HOURS_IN_WEEK):
                time.offset %= constants.HOURS_IN_WEEK
            # if interval would wrap around, split it into 2
            if time.offset + time.duration > constants.HOURS_IN_WEEK:
                duration_after_wrap = (time.offset + time.duration) % constants.HOURS_IN_WEEK
                time.duration = constants.HOURS_IN_WEEK - time.offset
                signup.times.append(schemas.SignupTime(offset=0, duration=duration_after_wrap, timezone="Etc/UTC"))

        for time in signup.times:  # iterate again since we may have modified the array
            event_offsets.add(time.offset)
            event_offsets.add(time.offset + time.duration)

    # each signup now has normalized times
    # these are the hours where someone's availability changes
    event_offsets.add(0)
    event_offsets.add(constants.HOURS_IN_WEEK)
    event_offsets = sorted(list(event_offsets))

    # build the sets of who is available when
    # we keep track of the sets of people available at the current idx in buffer, and then examine the next event time:
    # for each set where the set of availability is not a superset, pop it and add it to the list
    out = []  # list of triples (start, stop, ids)
    buffer = []  # list of pairs (start_time, available (set of ids))
    for event_time in event_offsets:
        available_set = {s for s in signups if is_available(s, event_time)}
        # pop any that are not subsets of the current available set
        for item in buffer[:]:
            start_time, ids = item
            if not available_set.issuperset(ids):
                buffer.remove(item)
                out.append((start_time, event_time, ids))
        # if this specific set is not already in the buffer, add it
        if available_set and not any(avail == available_set for _, avail in buffer):
            buffer.append((event_time, available_set))
    # sanity check: flush anything still in the buffer
    for start_time, ids in buffer:
        out.append((start_time, constants.HOURS_IN_WEEK, ids))

    # merge any that span a week reset
    # this can probably be done in less than O(n^2) time but I haven't eaten dinner yet and n <= 8 so whatever
    starting_at_0 = [i for i in out if i[0] == 0]
    ending_at_168 = [i for i in out if i[1] == constants.HOURS_IN_WEEK]
    for end in ending_at_168:
        for start in starting_at_0:
            if end[2] == start[2]:
                out.remove(end)
                out.remove(start)
                out.append((end[0], start[1], end[2]))

    # sort by preference for people, then length - add a point if duration is greater than 3h
    # formula: score = people + sqrt(duration) / 1.2
    # noinspection PyShadowingNames
    def scorer(item):
        start, stop, ids = item
        if stop < start:
            duration = constants.HOURS_IN_WEEK - start + stop
        else:
            duration = stop - start
        people = len(ids)
        duration_score = people + math.sqrt(duration) / 1.2
        return people + duration_score

    return sorted(out, key=scorer, reverse=True)


def is_available(signup, offset):
    """Whether or not the given signup is available at the given instant."""
    return any(t.offset <= offset < t.offset + t.duration for t in signup.times)


class RoleSolver:
    def __init__(self, game_session, signups):
        """
        :type game_session: schemas.GameSessionFull
        :type signups: list[schemas.GameSignupFull]
        """
        self.game_session = game_session
        self.signups = signups
        self.goal = object()
        self.roles_by_id = {r.id: r for r in game_session.all_roles}

    def neighbors(self, node):
        """
        :type node: frozenset[tuple[schemas.GameSignupFull, schemas.GameSessionRole]]
        """
        if len(node) < len(self.signups):
            signup = self.signups[len(node)]
            for role in signup.roles:
                yield frozenset.union(node, [(signup, self.roles_by_id[role.role_id])])
            yield frozenset.union(node, [(signup, None)])
        yield self.goal

    def get_role_counts(self, roles):
        """
        Given a list of roles, returns a mapping of role id -> count. If a given role has a parent, counts its parents.

        :type roles: list[schemas.GameSessionRole]
        :rtype: dict[int, int]
        """
        role_count = collections.Counter()
        for role in roles:
            if role is None:
                continue
            role_count[role.id] += 1
            while role.parent_id:
                role = self.roles_by_id[role.parent_id]
                role_count[role.id] += 1
        return role_count

    def assigned_cost(self, node, last_node):
        """
        AKA g score: the minimum cost incurred at this node

        :type node: set[tuple[schemas.GameSignupFull, schemas.GameSessionRole]] or object
        :type last_node: set[tuple[schemas.GameSignupFull, schemas.GameSessionRole]]
        """
        if node is self.goal:
            total_cost = self.exact_cost(self.get_role_counts([role for signup, role in last_node]))
            node = last_node
        else:
            # cost only considering ones that cannot be fixed (already assigned more than max)
            role_assignment = self.get_role_counts([role for signup, role in node])
            total_cost = 0
            for rule in self.game_session.all_rules:
                num_people = role_assignment[rule.role_id]
                if num_people < rule.value:
                    continue
                difference = num_people - rule.value

                if rule.operator == schemas.RuleOperator.EQ:
                    total_cost += RULE_BREAK_COST * difference
                elif rule.operator == schemas.RuleOperator.LE:
                    total_cost += RULE_BREAK_COST * difference
                elif rule.operator == schemas.RuleOperator.LT:
                    total_cost += RULE_BREAK_COST * (difference + 1)

        # account for playing meh roles
        for signup, role in node:
            if role is not None:
                signup_role = next((r for r in signup.roles if r.role_id == role.id), None)  # todo optimize me
                if signup_role is not None:
                    total_cost += signup_role.weight

        return total_cost

    def exact_cost(self, role_counts):
        """
        The exact cost incurred by breaking rules by the given role assignment

        :type role_counts: dict[int, int]
        """
        total_cost = 0
        for rule in self.game_session.all_rules:
            num_people = role_counts[rule.role_id]
            difference = num_people - rule.value

            if rule.operator == schemas.RuleOperator.EQ:
                total_cost += RULE_BREAK_COST * abs(difference)
            elif rule.operator == schemas.RuleOperator.LE and difference > 0:
                total_cost += RULE_BREAK_COST * difference
            elif rule.operator == schemas.RuleOperator.LT and difference >= 0:
                total_cost += RULE_BREAK_COST * (difference + 1)
            elif rule.operator == schemas.RuleOperator.GE and difference < 0:
                total_cost += RULE_BREAK_COST * -difference
            elif rule.operator == schemas.RuleOperator.GT and difference <= 0:
                total_cost += RULE_BREAK_COST * -(difference - 1)

        return total_cost

    def speculative_cost(self, node):
        """
        The minimum cost we'll incur because there aren't enough people in the remaining pool to fulfill rules

        aka h - the minimum cost of getting to the goal from the current node
        """
        if node is self.goal:
            return 0

        # all locked in assignments
        assigned_signups = {signup for signup, role_id in node}
        role_count = self.get_role_counts([role for signup, role in node]
                                          + [self.roles_by_id[signup_role.role_id]
                                             for signup in self.signups if signup not in assigned_signups
                                             for signup_role in signup.roles])

        # given all possible assignments, which rules are impossible to satisfy?
        total_cost = 0
        for rule in self.game_session.all_rules:
            num_people = role_count[rule.role_id]
            if num_people > rule.value:
                continue
            difference = rule.value - num_people

            if rule.operator == schemas.RuleOperator.EQ:
                total_cost += RULE_BREAK_COST * difference
            elif rule.operator == schemas.RuleOperator.GE:
                total_cost += RULE_BREAK_COST * difference
            elif rule.operator == schemas.RuleOperator.GT:
                total_cost += RULE_BREAK_COST * (difference + 1)

        return total_cost

    def solve(self):
        """
        :rtype: frozenset[tuple[schemas.GameSignupFull, schemas.GameSessionRole]]
        """
        start = frozenset()
        frontier = {start}

        g_score = collections.defaultdict(lambda: float('inf'))
        g_score[start] = 0
        f_score = collections.defaultdict(lambda: float('inf'))
        f_score[start] = 0
        best_solution = start
        i = 0

        while len(frontier):
            current = min([(node, f_score[node]) for node in frontier], key=lambda n: n[1])[0]

            if DEBUG_ASTAR:
                print(f"Current ({f_score[current]}): ", end='')
                self.print_node(current)
                print("Options:\n")

            if current is self.goal:
                if DEBUG_ASTAR:
                    print("\nSolution!")
                    self.print_node(best_solution)
                return best_solution

            frontier.remove(current)
            for neighbor in self.neighbors(current):
                tentative_g_score = self.assigned_cost(neighbor, current)
                if tentative_g_score < g_score[neighbor]:
                    if neighbor is self.goal:
                        best_solution = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.speculative_cost(neighbor) \
                                        - ((0.0001 * len(current)) + 0.0001)
                    frontier.add(neighbor)

                    if DEBUG_ASTAR:
                        self.print_node(neighbor)
                        print(f"gscore: {g_score[neighbor]}, fscore: {f_score[neighbor]}")
            if DEBUG_ASTAR:
                i += 1
                print(f"\n  ======== Done with iteration {i}, frontier size = {len(frontier)} ========\n")
        raise RuntimeError("this should never happen")

    @staticmethod
    def print_node(node, after=''):
        try:
            print(", ".join(f"{s.id} on {r.name if r else 'none'}" for s, r in node) + after)
        except Exception:
            print("goal" + after)
