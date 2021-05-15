"""
This file contains some dummy data for use in developing the frontend.
"""
from . import schemas


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

full_session = schemas.GameSessionFull.parse_obj({
    "all_roles": [
        {
            "children": [],
            "icon": "img/paladin.png",
            "id": 71,
            "name": "Paladin",
            "parent_id": 70,
            "rules": [
                {
                    "id": 163,
                    "operator": "le",
                    "role_id": 71,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/warrior.png",
            "id": 72,
            "name": "Warrior",
            "parent_id": 70,
            "rules": [
                {
                    "id": 164,
                    "operator": "le",
                    "role_id": 72,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/darkknight.png",
            "id": 73,
            "name": "Dark Knight",
            "parent_id": 70,
            "rules": [
                {
                    "id": 165,
                    "operator": "le",
                    "role_id": 73,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/gunbreaker.png",
            "id": 74,
            "name": "Gunbreaker",
            "parent_id": 70,
            "rules": [
                {
                    "id": 166,
                    "operator": "le",
                    "role_id": 74,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/paladin.png",
                    "id": 71,
                    "name": "Paladin",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 163,
                            "operator": "le",
                            "role_id": 71,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/warrior.png",
                    "id": 72,
                    "name": "Warrior",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 164,
                            "operator": "le",
                            "role_id": 72,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/darkknight.png",
                    "id": 73,
                    "name": "Dark Knight",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 165,
                            "operator": "le",
                            "role_id": 73,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/gunbreaker.png",
                    "id": 74,
                    "name": "Gunbreaker",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 166,
                            "operator": "le",
                            "role_id": 74,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/tank.png",
            "id": 70,
            "name": "Tank",
            "parent_id": None,
            "rules": [
                {
                    "id": 162,
                    "operator": "eq",
                    "role_id": 70,
                    "session_id": 8,
                    "value": 2
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/whitemage.png",
            "id": 76,
            "name": "White Mage",
            "parent_id": 75,
            "rules": [
                {
                    "id": 168,
                    "operator": "le",
                    "role_id": 76,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/scholar.png",
            "id": 77,
            "name": "Scholar",
            "parent_id": 75,
            "rules": [
                {
                    "id": 169,
                    "operator": "le",
                    "role_id": 77,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/astrologian.png",
            "id": 78,
            "name": "Astrologian",
            "parent_id": 75,
            "rules": [
                {
                    "id": 170,
                    "operator": "le",
                    "role_id": 78,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/whitemage.png",
                    "id": 76,
                    "name": "White Mage",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 168,
                            "operator": "le",
                            "role_id": 76,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/scholar.png",
                    "id": 77,
                    "name": "Scholar",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 169,
                            "operator": "le",
                            "role_id": 77,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/astrologian.png",
                    "id": 78,
                    "name": "Astrologian",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 170,
                            "operator": "le",
                            "role_id": 78,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/healer.png",
            "id": 75,
            "name": "Healer",
            "parent_id": None,
            "rules": [
                {
                    "id": 167,
                    "operator": "eq",
                    "role_id": 75,
                    "session_id": 8,
                    "value": 2
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/monk.png",
            "id": 81,
            "name": "Monk",
            "parent_id": 80,
            "rules": [
                {
                    "id": 173,
                    "operator": "le",
                    "role_id": 81,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/dragoon.png",
            "id": 82,
            "name": "Dragoon",
            "parent_id": 80,
            "rules": [
                {
                    "id": 174,
                    "operator": "le",
                    "role_id": 82,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/ninja.png",
            "id": 83,
            "name": "Ninja",
            "parent_id": 80,
            "rules": [
                {
                    "id": 175,
                    "operator": "le",
                    "role_id": 83,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/samurai.png",
            "id": 84,
            "name": "Samurai",
            "parent_id": 80,
            "rules": [
                {
                    "id": 176,
                    "operator": "le",
                    "role_id": 84,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/monk.png",
                    "id": 81,
                    "name": "Monk",
                    "parent_id": 80,
                    "rules": [
                        {
                            "id": 173,
                            "operator": "le",
                            "role_id": 81,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/dragoon.png",
                    "id": 82,
                    "name": "Dragoon",
                    "parent_id": 80,
                    "rules": [
                        {
                            "id": 174,
                            "operator": "le",
                            "role_id": 82,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/ninja.png",
                    "id": 83,
                    "name": "Ninja",
                    "parent_id": 80,
                    "rules": [
                        {
                            "id": 175,
                            "operator": "le",
                            "role_id": 83,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/samurai.png",
                    "id": 84,
                    "name": "Samurai",
                    "parent_id": 80,
                    "rules": [
                        {
                            "id": 176,
                            "operator": "le",
                            "role_id": 84,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/melee.png",
            "id": 80,
            "name": "Melee DPS",
            "parent_id": 79,
            "rules": [
                {
                    "id": 172,
                    "operator": "ge",
                    "role_id": 80,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/bard.png",
            "id": 86,
            "name": "Bard",
            "parent_id": 85,
            "rules": [
                {
                    "id": 178,
                    "operator": "le",
                    "role_id": 86,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/machinist.png",
            "id": 87,
            "name": "Machinist",
            "parent_id": 85,
            "rules": [
                {
                    "id": 179,
                    "operator": "le",
                    "role_id": 87,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/dancer.png",
            "id": 88,
            "name": "Dancer",
            "parent_id": 85,
            "rules": [
                {
                    "id": 180,
                    "operator": "le",
                    "role_id": 88,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/bard.png",
                    "id": 86,
                    "name": "Bard",
                    "parent_id": 85,
                    "rules": [
                        {
                            "id": 178,
                            "operator": "le",
                            "role_id": 86,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/machinist.png",
                    "id": 87,
                    "name": "Machinist",
                    "parent_id": 85,
                    "rules": [
                        {
                            "id": 179,
                            "operator": "le",
                            "role_id": 87,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/dancer.png",
                    "id": 88,
                    "name": "Dancer",
                    "parent_id": 85,
                    "rules": [
                        {
                            "id": 180,
                            "operator": "le",
                            "role_id": 88,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/pranged.png",
            "id": 85,
            "name": "Physical Ranged DPS",
            "parent_id": 79,
            "rules": [
                {
                    "id": 177,
                    "operator": "ge",
                    "role_id": 85,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/blackmage.png",
            "id": 90,
            "name": "Black Mage",
            "parent_id": 89,
            "rules": [
                {
                    "id": 182,
                    "operator": "le",
                    "role_id": 90,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/summoner.png",
            "id": 91,
            "name": "Summoner",
            "parent_id": 89,
            "rules": [
                {
                    "id": 183,
                    "operator": "le",
                    "role_id": 91,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [],
            "icon": "img/redmage.png",
            "id": 92,
            "name": "Red Mage",
            "parent_id": 89,
            "rules": [
                {
                    "id": 184,
                    "operator": "le",
                    "role_id": 92,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/blackmage.png",
                    "id": 90,
                    "name": "Black Mage",
                    "parent_id": 89,
                    "rules": [
                        {
                            "id": 182,
                            "operator": "le",
                            "role_id": 90,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/summoner.png",
                    "id": 91,
                    "name": "Summoner",
                    "parent_id": 89,
                    "rules": [
                        {
                            "id": 183,
                            "operator": "le",
                            "role_id": 91,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/redmage.png",
                    "id": 92,
                    "name": "Red Mage",
                    "parent_id": 89,
                    "rules": [
                        {
                            "id": 184,
                            "operator": "le",
                            "role_id": 92,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/caster.png",
            "id": 89,
            "name": "Magic Ranged DPS",
            "parent_id": 79,
            "rules": [
                {
                    "id": 181,
                    "operator": "ge",
                    "role_id": 89,
                    "session_id": 8,
                    "value": 1
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/monk.png",
                            "id": 81,
                            "name": "Monk",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 173,
                                    "operator": "le",
                                    "role_id": 81,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/dragoon.png",
                            "id": 82,
                            "name": "Dragoon",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 174,
                                    "operator": "le",
                                    "role_id": 82,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/ninja.png",
                            "id": 83,
                            "name": "Ninja",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 175,
                                    "operator": "le",
                                    "role_id": 83,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/samurai.png",
                            "id": 84,
                            "name": "Samurai",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 176,
                                    "operator": "le",
                                    "role_id": 84,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/melee.png",
                    "id": 80,
                    "name": "Melee DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 172,
                            "operator": "ge",
                            "role_id": 80,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/bard.png",
                            "id": 86,
                            "name": "Bard",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 178,
                                    "operator": "le",
                                    "role_id": 86,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/machinist.png",
                            "id": 87,
                            "name": "Machinist",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 179,
                                    "operator": "le",
                                    "role_id": 87,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/dancer.png",
                            "id": 88,
                            "name": "Dancer",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 180,
                                    "operator": "le",
                                    "role_id": 88,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/pranged.png",
                    "id": 85,
                    "name": "Physical Ranged DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 177,
                            "operator": "ge",
                            "role_id": 85,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/blackmage.png",
                            "id": 90,
                            "name": "Black Mage",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 182,
                                    "operator": "le",
                                    "role_id": 90,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/summoner.png",
                            "id": 91,
                            "name": "Summoner",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 183,
                                    "operator": "le",
                                    "role_id": 91,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/redmage.png",
                            "id": 92,
                            "name": "Red Mage",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 184,
                                    "operator": "le",
                                    "role_id": 92,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/caster.png",
                    "id": 89,
                    "name": "Magic Ranged DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 181,
                            "operator": "ge",
                            "role_id": 89,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/dps.png",
            "id": 79,
            "name": "DPS",
            "parent_id": None,
            "rules": [
                {
                    "id": 171,
                    "operator": "eq",
                    "role_id": 79,
                    "session_id": 8,
                    "value": 4
                }
            ],
            "session_id": 8
        }
    ],
    "all_rules": [
        {
            "id": 162,
            "operator": "eq",
            "role_id": 70,
            "session_id": 8,
            "value": 2
        },
        {
            "id": 163,
            "operator": "le",
            "role_id": 71,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 164,
            "operator": "le",
            "role_id": 72,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 165,
            "operator": "le",
            "role_id": 73,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 166,
            "operator": "le",
            "role_id": 74,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 167,
            "operator": "eq",
            "role_id": 75,
            "session_id": 8,
            "value": 2
        },
        {
            "id": 168,
            "operator": "le",
            "role_id": 76,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 169,
            "operator": "le",
            "role_id": 77,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 170,
            "operator": "le",
            "role_id": 78,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 171,
            "operator": "eq",
            "role_id": 79,
            "session_id": 8,
            "value": 4
        },
        {
            "id": 172,
            "operator": "ge",
            "role_id": 80,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 173,
            "operator": "le",
            "role_id": 81,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 174,
            "operator": "le",
            "role_id": 82,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 175,
            "operator": "le",
            "role_id": 83,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 176,
            "operator": "le",
            "role_id": 84,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 177,
            "operator": "ge",
            "role_id": 85,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 178,
            "operator": "le",
            "role_id": 86,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 179,
            "operator": "le",
            "role_id": 87,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 180,
            "operator": "le",
            "role_id": 88,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 181,
            "operator": "ge",
            "role_id": 89,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 182,
            "operator": "le",
            "role_id": 90,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 183,
            "operator": "le",
            "role_id": 91,
            "session_id": 8,
            "value": 1
        },
        {
            "id": 184,
            "operator": "le",
            "role_id": 92,
            "session_id": 8,
            "value": 1
        }
    ],
    "description": "whee",
    "id": 8,
    "invite_key": "xgOA8s4",
    "name": "hello world",
    "owner": {
        "avatar_hash": "448f9060e0d7a3afba733a7fa53e9280",
        "email": "mommothazaz123@gmail.com",
        "id": 1,
        "username": "zhu.exe#4211"
    },
    "roles": [
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/paladin.png",
                    "id": 71,
                    "name": "Paladin",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 163,
                            "operator": "le",
                            "role_id": 71,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/warrior.png",
                    "id": 72,
                    "name": "Warrior",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 164,
                            "operator": "le",
                            "role_id": 72,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/darkknight.png",
                    "id": 73,
                    "name": "Dark Knight",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 165,
                            "operator": "le",
                            "role_id": 73,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/gunbreaker.png",
                    "id": 74,
                    "name": "Gunbreaker",
                    "parent_id": 70,
                    "rules": [
                        {
                            "id": 166,
                            "operator": "le",
                            "role_id": 74,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/tank.png",
            "id": 70,
            "name": "Tank",
            "parent_id": None,
            "rules": [
                {
                    "id": 162,
                    "operator": "eq",
                    "role_id": 70,
                    "session_id": 8,
                    "value": 2
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [],
                    "icon": "img/whitemage.png",
                    "id": 76,
                    "name": "White Mage",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 168,
                            "operator": "le",
                            "role_id": 76,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/scholar.png",
                    "id": 77,
                    "name": "Scholar",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 169,
                            "operator": "le",
                            "role_id": 77,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [],
                    "icon": "img/astrologian.png",
                    "id": 78,
                    "name": "Astrologian",
                    "parent_id": 75,
                    "rules": [
                        {
                            "id": 170,
                            "operator": "le",
                            "role_id": 78,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/healer.png",
            "id": 75,
            "name": "Healer",
            "parent_id": None,
            "rules": [
                {
                    "id": 167,
                    "operator": "eq",
                    "role_id": 75,
                    "session_id": 8,
                    "value": 2
                }
            ],
            "session_id": 8
        },
        {
            "children": [
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/monk.png",
                            "id": 81,
                            "name": "Monk",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 173,
                                    "operator": "le",
                                    "role_id": 81,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/dragoon.png",
                            "id": 82,
                            "name": "Dragoon",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 174,
                                    "operator": "le",
                                    "role_id": 82,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/ninja.png",
                            "id": 83,
                            "name": "Ninja",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 175,
                                    "operator": "le",
                                    "role_id": 83,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/samurai.png",
                            "id": 84,
                            "name": "Samurai",
                            "parent_id": 80,
                            "rules": [
                                {
                                    "id": 176,
                                    "operator": "le",
                                    "role_id": 84,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/melee.png",
                    "id": 80,
                    "name": "Melee DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 172,
                            "operator": "ge",
                            "role_id": 80,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/bard.png",
                            "id": 86,
                            "name": "Bard",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 178,
                                    "operator": "le",
                                    "role_id": 86,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/machinist.png",
                            "id": 87,
                            "name": "Machinist",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 179,
                                    "operator": "le",
                                    "role_id": 87,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/dancer.png",
                            "id": 88,
                            "name": "Dancer",
                            "parent_id": 85,
                            "rules": [
                                {
                                    "id": 180,
                                    "operator": "le",
                                    "role_id": 88,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/pranged.png",
                    "id": 85,
                    "name": "Physical Ranged DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 177,
                            "operator": "ge",
                            "role_id": 85,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                },
                {
                    "children": [
                        {
                            "children": [],
                            "icon": "img/blackmage.png",
                            "id": 90,
                            "name": "Black Mage",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 182,
                                    "operator": "le",
                                    "role_id": 90,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/summoner.png",
                            "id": 91,
                            "name": "Summoner",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 183,
                                    "operator": "le",
                                    "role_id": 91,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        },
                        {
                            "children": [],
                            "icon": "img/redmage.png",
                            "id": 92,
                            "name": "Red Mage",
                            "parent_id": 89,
                            "rules": [
                                {
                                    "id": 184,
                                    "operator": "le",
                                    "role_id": 92,
                                    "session_id": 8,
                                    "value": 1
                                }
                            ],
                            "session_id": 8
                        }
                    ],
                    "icon": "img/caster.png",
                    "id": 89,
                    "name": "Magic Ranged DPS",
                    "parent_id": 79,
                    "rules": [
                        {
                            "id": 181,
                            "operator": "ge",
                            "role_id": 89,
                            "session_id": 8,
                            "value": 1
                        }
                    ],
                    "session_id": 8
                }
            ],
            "icon": "img/dps.png",
            "id": 79,
            "name": "DPS",
            "parent_id": None,
            "rules": [
                {
                    "id": 171,
                    "operator": "eq",
                    "role_id": 79,
                    "session_id": 8,
                    "value": 4
                }
            ],
            "session_id": 8
        }
    ],
    "selected_time_duration": None,
    "selected_time_offset": None,
    "selected_time_timezone": None
})
full_session_roles = {r.name: r.id for r in full_session.all_roles}
full_session_roles_by_id = {r.id: r.name for r in full_session.all_roles}


# data from real signup sessions on when2meet
def signup(name, offset_and_durations, wanted_roles=[], ok_roles=[]):
    class DummySignup(schemas.GameSignupFull):
        id: str

    return DummySignup(
        id=name,
        anonymous_name=name,
        times=[schemas.SignupTime(offset=offset, duration=duration, timezone="Etc/UTC")
               for offset, duration in offset_and_durations],
        roles=[schemas.SignupRole(role_id=full_session_roles[role_name], weight=0) for role_name in wanted_roles]
              + [schemas.SignupRole(role_id=full_session_roles[role_name], weight=10) for role_name in ok_roles])


signups = [
    signup("Orelya",
           [(15, 1.5), (18, 2),
            (13 + 24, 7),
            (15 + 48, 5),
            (15 + 72, 5),
            (13 + 96, 7),
            (15 + 120, 5)],
           ["Dark Knight", "Warrior"],
           ["Scholar", "Machinist"]),
    signup("Sazri",
           [(15, 1.5),
            (12 + 24, 4.5),
            (14 + 48, 8),
            (12 + 72, 10),
            (10 + 96, 12),
            (10 + 120, 12),
            (12 + 144, 4.5)],
           ["Paladin"]),
    signup("Tahla",
           [(18, 2), (21, 1),
            (17 + 24, 5),
            (18 + 48, 4),
            (17 + 72, 5),
            (10 + 96, 12),
            (10 + 120, 12),
            (17 + 144, 5)],
           ["White Mage", "Red Mage"],
           ["Gunbreaker", "Dancer", "Dragoon"]),
    signup("Kai",
           [(21, 1),
            (17 + 24, 5),
            (18 + 72, 4),
            (19.5 + 96, 1.5)],
           ["Red Mage"],
           ["Dragoon"]),
    signup("Wyse",
           [(12 + 24, 10),
            (16 + 48, 6),
            (12 + 72, 10),
            (12 + 96, 10),
            (12 + 120, 10),
            (12 + 144, 10)],
           ["Monk"]),
    signup("Zeke",
           [(14 + 24, 8),
            (14 + 48, 8),
            (14 + 72, 8),
            (10 + 96, 12),
            (10 + 120, 12),
            (14 + 144, 8)],
           ["Red Mage", "Dragoon"],
           ["Summoner", "Machinist", "White Mage", "Black Mage"]),
    signup("Ventaile",
           [(18 + 24, 3),
            (18 + 72, 3),
            (17.5 + 96, 3.5),
            (17 + 144, 4)],
           ["Machinist"],
           ["Scholar"]),
    signup("Thancwed",
           [(14 + 24, 6),
            (10 + 48, 12),
            (10 + 96, 6), (18 + 96, 4),
            (13 + 120, 9),
            (14 + 144, 8)],
           ["Ninja"]),
    # signup("Spooky Ghost",
    #        [(18 + 24, 3),
    #         (18 + 72, 3),
    #         (17.5 + 96, 3.5),
    #         (17 + 144, 4)],
    #        ["White Mage",],
    #        ["Scholar"]),
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
