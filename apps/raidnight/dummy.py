"""
This file contains some dummy data for use in developing the frontend.
"""
from . import presets, schemas


class Dummy:
    def __repr__(self):
        return f"<Dummy {self.__dict__}>"


def objectify(d):
    o = Dummy()
    o.__dict__ = d
    return o


lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

session1 = objectify({
    'id': 1, 'name': 'Test Session', 'description': 'Some Description', 'owner_id': 1, 'selected_time_offset': None,
    'selected_time_duration': None, 'selected_time_timezone': None
})

session2 = objectify({
    'id': 2, 'name': 'Test 2', 'description': lipsum, 'owner_id': 2, 'selected_time_offset': None,
    'selected_time_duration': None, 'selected_time_timezone': None
})

full_session = objectify({
    'id': 3, 'name': 'Test but like full', 'description': 'has roles and rules', 'owner_id': 2,
    'selected_time_offset': None,
    'selected_time_duration': None,
    'selected_time_timezone': None,
    'roles': presets.raid8_strict.roles,
    'rules': presets.raid8_strict.rules
})


# data from real signup sessions on when2meet
def signup(name, offset_and_durations):
    class DummySignup(schemas.GameSignupFull):
        id: str

    return DummySignup(
        id=name,
        times=[schemas.SignupTime(offset=offset, duration=duration, timezone="Etc/UTC")
               for offset, duration in offset_and_durations],
        roles=[])


signups = [
    signup("Orelya", [(15, 1.5), (18, 2),
                      (13 + 24, 7),
                      (15 + 48, 5),
                      (15 + 72, 5),
                      (13 + 96, 7),
                      (15 + 120, 5)]),
    signup("Sazri", [(15, 1.5),
                     (12 + 24, 4.5),
                     (14 + 48, 8),
                     (12 + 72, 10),
                     (10 + 96, 12),
                     (10 + 120, 12),
                     (12 + 144, 4.5)]),
    signup("Tahla", [(18, 2), (21, 1),
                     (17 + 24, 5),
                     (18 + 48, 4),
                     (17 + 72, 5),
                     (10 + 96, 12),
                     (10 + 120, 12),
                     (17 + 144, 5)]),
    signup("Kai", [(21, 1),
                   (17 + 24, 5),
                   (18 + 72, 4),
                   (19.5 + 96, 1.5)]),
    signup("Wyse", [(12 + 24, 10),
                    (16 + 48, 6),
                    (12 + 72, 10),
                    (12 + 96, 10),
                    (12 + 120, 10),
                    (12 + 144, 10)]),
    signup("Zeke", [(14 + 24, 8),
                    (14 + 48, 8),
                    (14 + 72, 8),
                    (10 + 96, 12),
                    (10 + 120, 12),
                    (14 + 144, 8)]),
    signup("Ventaile", [(18 + 24, 3),
                        (18 + 72, 3),
                        (17.5 + 96, 3.5),
                        (17 + 144, 4)])
]

signups2 = [
    signup("Sazri", [(10, 12),
                     (10 + 24, 7),
                     (10 + 48, 7),
                     (10 + 72, 7),
                     (10 + 96, 12),
                     (10 + 120, 12),
                     (10 + 144, 6)]),
    signup("Tahla", [(10, 12),
                     (17 + 24, 5),
                     (18 + 48, 4),
                     (17 + 72, 5),
                     (18 + 96, 4),
                     (17 + 120, 5),
                     (10 + 144, 12)]),
    signup("Zeke", [(10, 12),
                    (17 + 24, 0.75), (18.25 + 24, 3.75),
                    (17 + 72, 0.75), (18.25 + 72, 3.75),
                    (17 + 96, 0.75), (18.25 + 96, 3.75),
                    (17 + 120, 0.75), (18.25 + 120, 3.75),
                    (10 + 144, 12)]),
    signup("Kai", [(12, 5.5),
                   (17.5 + 24, 4.5),
                   (21 + 48, 1),
                   (16 + 72, 5),
                   (21 + 96, 1),
                   (12 + 144, 4)]),
    signup("Wyse", [(12, 10),
                    (10 + 24, 5),
                    (10 + 72, 12),
                    (10 + 96, 2),
                    (10 + 120, 12),
                    (10 + 144, 12)]),
    signup("Ventaile", [(16.5, 4.5),
                        (16 + 24, 5),
                        (20 + 96, 1),
                        (18 + 120, 3),
                        (16 + 144, 5)]),
    signup("Thancwed", [(14 + 24, 6),
                        (10 + 48, 12),
                        (10 + 96, 6), (18 + 96, 4),
                        (13 + 120, 9),
                        (14 + 144, 8)])
]
