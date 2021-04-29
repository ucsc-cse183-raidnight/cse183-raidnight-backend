"""
This file defines all the presets (roles + rules).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Preset:
    name: str
    description: str
    roles: List[PresetRole] = field(default_factory=list)
    rules: List[PresetRule] = field(default_factory=list)

    def to_vue_dict(self):
        roles_with_rules = [r.to_vue_dict() for r in self.roles]
        role_lookup = {}
        for role in traverse(roles_with_rules):
            role_lookup[role['name']] = role
        for rule in self.rules:
            role_lookup[rule.role.name]['rules'].append(rule.to_vue_dict())
        return {"name": self.name, "description": self.description, "roles": roles_with_rules}


@dataclass
class PresetRole:
    name: str
    icon: Optional[str] = None
    children: List[PresetRole] = field(default_factory=list)

    def to_vue_dict(self):
        children = [r.to_vue_dict() for r in self.children]
        return {"name": self.name, "rules": [], "icon": self.icon, "children": children}


@dataclass
class PresetRule:
    role: PresetRole
    rule_operator: str
    rule_value: Optional[int] = None

    def to_vue_dict(self):
        return {"operator": self.rule_operator, "value": self.rule_value}


DEFAULT_ROLES = [
    tank := PresetRole(name="Tank", icon="img/tank.png", children=[
        paladin := PresetRole(name="Paladin", icon="img/paladin.png"),
        warrior := PresetRole(name="Warrior", icon="img/warrior.png"),
        dark_knight := PresetRole(name="Dark Knight", icon="img/darkknight.png"),
        gunbreaker := PresetRole(name="Gunbreaker", icon="img/gunbreaker.png")
    ]),
    healer := PresetRole(name="Healer", icon="img/healer.png", children=[
        white_mage := PresetRole(name="White Mage", icon="img/whitemage.png"),
        scholar := PresetRole(name="Scholar", icon="img/scholar.png"),
        astrologian := PresetRole(name="Astrologian", icon="img/astrologian.png")
    ]),
    dps := PresetRole(name="DPS", icon="img/dps.png", children=[
        melee := PresetRole(name="Melee DPS", icon="img/melee.png", children=[
            monk := PresetRole(name="Monk", icon="img/monk.png"),
            dragoon := PresetRole(name="Dragoon", icon="img/dragoon.png"),
            ninja := PresetRole(name="Ninja", icon="img/ninja.png"),
            samurai := PresetRole(name="Samurai", icon="img/samurai.png")
        ]),
        pranged := PresetRole(name="Physical Ranged DPS", icon="img/pranged.png", children=[
            bard := PresetRole(name="Bard", icon="img/bard.png"),
            machinist := PresetRole(name="Machinist", icon="img/machinist.png"),
            dancer := PresetRole(name="Dancer", icon="img/dancer.png")
        ]),
        caster := PresetRole(name="Magic Ranged DPS", icon="img/caster.png", children=[
            black_mage := PresetRole(name="Black Mage", icon="img/blackmage.png"),
            summoner := PresetRole(name="Summoner", icon="img/summoner.png"),
            red_mage := PresetRole(name="Red Mage", icon="img/redmage.png")
        ])
    ])
]
ALL_JOBS = [
    paladin, warrior, dark_knight, gunbreaker,
    white_mage, scholar, astrologian,
    monk, dragoon, ninja, samurai,
    bard, machinist, dancer,
    black_mage, summoner, red_mage
]

# ==== Presets ====
# 8-person raid (2T/2H/4D)
raid8 = Preset(
    name="Raid (8-person)",
    description="An 8-person raid with two tanks, two healers, and 4 DPS.",
    roles=DEFAULT_ROLES,
    rules=[
        PresetRule(role=tank, rule_operator='eq', rule_value=2),
        PresetRule(role=healer, rule_operator='eq', rule_value=2),
        PresetRule(role=dps, rule_operator='eq', rule_value=4)
    ]
)

# 8-person raid (2T/2H/4D), 1 player per job
raid8_1ppj = Preset(
    name="Raid (1 player per job)",
    description="An 8-person raid with two tanks, two healers, and 4 DPS, limited to at most one player per job.",
    roles=DEFAULT_ROLES,
    rules=[
        PresetRule(role=tank, rule_operator='eq', rule_value=2),
        PresetRule(role=healer, rule_operator='eq', rule_value=2),
        PresetRule(role=dps, rule_operator='eq', rule_value=4),
        *[PresetRule(role=r, rule_operator='le', rule_value=1) for r in ALL_JOBS]
    ]
)

# 8-person raid (2T/2H/2M/1C/1R), 1 player per job
raid8_strict = Preset(
    name="Raid (Strict)",
    description="An 8-person raid with two tanks, two healers, and 4 DPS, with at least one melee DPS, "
                "one ranged physical DPS, and one magic ranged DPS. One player per job.",
    roles=DEFAULT_ROLES,
    rules=[
        PresetRule(role=tank, rule_operator='eq', rule_value=2),
        PresetRule(role=healer, rule_operator='eq', rule_value=2),
        PresetRule(role=dps, rule_operator='eq', rule_value=4),
        *[PresetRule(role=r, rule_operator='le', rule_value=1) for r in ALL_JOBS],
        PresetRule(role=melee, rule_operator='ge', rule_value=1),
        PresetRule(role=pranged, rule_operator='ge', rule_value=1),
        PresetRule(role=caster, rule_operator='ge', rule_value=1)
    ]
)

# 4-person dungeon (1T/1H/2D)
dungeon4 = Preset(
    name="Dungeon (4-person)",
    description="An 4-person dungeon with one tank, one healer, and two DPS.",
    roles=DEFAULT_ROLES,
    rules=[
        PresetRule(role=tank, rule_operator='eq', rule_value=1),
        PresetRule(role=healer, rule_operator='eq', rule_value=1),
        PresetRule(role=dps, rule_operator='eq', rule_value=2)
    ]
)

# 8-person any
player = PresetRole(name="Player", icon="img/noclass.png", children=DEFAULT_ROLES)
any8 = Preset(
    name="Any 8",
    description="Any combination of 8 players.",
    roles=[player],
    rules=[PresetRule(role=player, rule_operator='eq', rule_value=8)]
)

# 4-person any
any4 = Preset(
    name="Any 4",
    description="Any combination of 4 players.",
    roles=[player],
    rules=[PresetRule(role=player, rule_operator='eq', rule_value=4)]
)

# 24-person alliance raid (3T/6H/15D)
alliance24 = Preset(
    name="Alliance Raid (24-person)",
    description="A 24-person alliance raid with three tanks, six healers, and 15 DPS.",
    roles=DEFAULT_ROLES,
    rules=[
        PresetRule(role=tank, rule_operator='eq', rule_value=3),
        PresetRule(role=healer, rule_operator='eq', rule_value=6),
        PresetRule(role=dps, rule_operator='eq', rule_value=15)
    ]
)

ALL_PRESETS = [raid8, raid8_1ppj, raid8_strict, dungeon4, any8, any4, alliance24]


# ==== utils ====
def traverse(role_dicts):
    for role in role_dicts:
        yield role
        yield from traverse(role['children'])
