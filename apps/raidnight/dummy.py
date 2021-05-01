"""
This file contains some dummy data for use in developing the frontend.
"""
from . import presets


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

fuller_session = {
    "id": 8,
    "name": "hello world",
    "description": "whee",
    "owner": {
        "id": 1,
        "username": "zhu.exe#4211",
        "email": "mommothazaz123@gmail.com",
        "avatar_hash": "448f9060e0d7a3afba733a7fa53e9280"
    },
    "selected_time_offset": None,
    "selected_time_duration": None,
    "selected_time_timezone": None,
    "roles": [
        {
            "id": 70,
            "session_id": 8,
            "name": "Tank",
            "parent_id": None,
            "icon": "img/tank.png",
            "children": [
                {
                    "id": 71,
                    "session_id": 8,
                    "name": "Paladin",
                    "parent_id": 70,
                    "icon": "img/paladin.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 71,
                            "session_id": 8,
                            "role_id": 71,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 72,
                    "session_id": 8,
                    "name": "Warrior",
                    "parent_id": 70,
                    "icon": "img/warrior.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 72,
                            "session_id": 8,
                            "role_id": 72,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 73,
                    "session_id": 8,
                    "name": "Dark Knight",
                    "parent_id": 70,
                    "icon": "img/darkknight.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 73,
                            "session_id": 8,
                            "role_id": 73,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 74,
                    "session_id": 8,
                    "name": "Gunbreaker",
                    "parent_id": 70,
                    "icon": "img/gunbreaker.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 74,
                            "session_id": 8,
                            "role_id": 74,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 70,
                    "session_id": 8,
                    "role_id": 70,
                    "operator": "eq",
                    "value": 2
                }
            ]
        },
        {
            "id": 75,
            "session_id": 8,
            "name": "Healer",
            "parent_id": None,
            "icon": "img/healer.png",
            "children": [
                {
                    "id": 76,
                    "session_id": 8,
                    "name": "White Mage",
                    "parent_id": 75,
                    "icon": "img/whitemage.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 76,
                            "session_id": 8,
                            "role_id": 76,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 77,
                    "session_id": 8,
                    "name": "Scholar",
                    "parent_id": 75,
                    "icon": "img/scholar.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 77,
                            "session_id": 8,
                            "role_id": 77,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 78,
                    "session_id": 8,
                    "name": "Astrologian",
                    "parent_id": 75,
                    "icon": "img/astrologian.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 78,
                            "session_id": 8,
                            "role_id": 78,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 75,
                    "session_id": 8,
                    "role_id": 75,
                    "operator": "eq",
                    "value": 2
                }
            ]
        },
        {
            "id": 79,
            "session_id": 8,
            "name": "DPS",
            "parent_id": None,
            "icon": "img/dps.png",
            "children": [
                {
                    "id": 80,
                    "session_id": 8,
                    "name": "Melee DPS",
                    "parent_id": 79,
                    "icon": "img/melee.png",
                    "children": [
                        {
                            "id": 81,
                            "session_id": 8,
                            "name": "Monk",
                            "parent_id": 80,
                            "icon": "img/monk.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 81,
                                    "session_id": 8,
                                    "role_id": 81,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 82,
                            "session_id": 8,
                            "name": "Dragoon",
                            "parent_id": 80,
                            "icon": "img/dragoon.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 82,
                                    "session_id": 8,
                                    "role_id": 82,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 83,
                            "session_id": 8,
                            "name": "Ninja",
                            "parent_id": 80,
                            "icon": "img/ninja.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 83,
                                    "session_id": 8,
                                    "role_id": 83,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 84,
                            "session_id": 8,
                            "name": "Samurai",
                            "parent_id": 80,
                            "icon": "img/samurai.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 84,
                                    "session_id": 8,
                                    "role_id": 84,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 80,
                            "session_id": 8,
                            "role_id": 80,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 85,
                    "session_id": 8,
                    "name": "Physical Ranged DPS",
                    "parent_id": 79,
                    "icon": "img/pranged.png",
                    "children": [
                        {
                            "id": 86,
                            "session_id": 8,
                            "name": "Bard",
                            "parent_id": 85,
                            "icon": "img/bard.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 86,
                                    "session_id": 8,
                                    "role_id": 86,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 87,
                            "session_id": 8,
                            "name": "Machinist",
                            "parent_id": 85,
                            "icon": "img/machinist.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 87,
                                    "session_id": 8,
                                    "role_id": 87,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 88,
                            "session_id": 8,
                            "name": "Dancer",
                            "parent_id": 85,
                            "icon": "img/dancer.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 88,
                                    "session_id": 8,
                                    "role_id": 88,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 85,
                            "session_id": 8,
                            "role_id": 85,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 89,
                    "session_id": 8,
                    "name": "Magic Ranged DPS",
                    "parent_id": 79,
                    "icon": "img/caster.png",
                    "children": [
                        {
                            "id": 90,
                            "session_id": 8,
                            "name": "Black Mage",
                            "parent_id": 89,
                            "icon": "img/blackmage.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 90,
                                    "session_id": 8,
                                    "role_id": 90,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 91,
                            "session_id": 8,
                            "name": "Summoner",
                            "parent_id": 89,
                            "icon": "img/summoner.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 91,
                                    "session_id": 8,
                                    "role_id": 91,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 92,
                            "session_id": 8,
                            "name": "Red Mage",
                            "parent_id": 89,
                            "icon": "img/redmage.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 92,
                                    "session_id": 8,
                                    "role_id": 92,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 89,
                            "session_id": 8,
                            "role_id": 89,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 79,
                    "session_id": 8,
                    "role_id": 79,
                    "operator": "eq",
                    "value": 4
                }
            ]
        }
    ],
    "all_roles": [
        {
            "id": 71,
            "session_id": 8,
            "name": "Paladin",
            "parent_id": 70,
            "icon": "img/paladin.png",
            "children": [],
            "rules": [
                {
                    "id": 71,
                    "session_id": 8,
                    "role_id": 71,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 72,
            "session_id": 8,
            "name": "Warrior",
            "parent_id": 70,
            "icon": "img/warrior.png",
            "children": [],
            "rules": [
                {
                    "id": 72,
                    "session_id": 8,
                    "role_id": 72,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 73,
            "session_id": 8,
            "name": "Dark Knight",
            "parent_id": 70,
            "icon": "img/darkknight.png",
            "children": [],
            "rules": [
                {
                    "id": 73,
                    "session_id": 8,
                    "role_id": 73,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 74,
            "session_id": 8,
            "name": "Gunbreaker",
            "parent_id": 70,
            "icon": "img/gunbreaker.png",
            "children": [],
            "rules": [
                {
                    "id": 74,
                    "session_id": 8,
                    "role_id": 74,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 70,
            "session_id": 8,
            "name": "Tank",
            "parent_id": None,
            "icon": "img/tank.png",
            "children": [
                {
                    "id": 71,
                    "session_id": 8,
                    "name": "Paladin",
                    "parent_id": 70,
                    "icon": "img/paladin.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 71,
                            "session_id": 8,
                            "role_id": 71,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 72,
                    "session_id": 8,
                    "name": "Warrior",
                    "parent_id": 70,
                    "icon": "img/warrior.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 72,
                            "session_id": 8,
                            "role_id": 72,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 73,
                    "session_id": 8,
                    "name": "Dark Knight",
                    "parent_id": 70,
                    "icon": "img/darkknight.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 73,
                            "session_id": 8,
                            "role_id": 73,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 74,
                    "session_id": 8,
                    "name": "Gunbreaker",
                    "parent_id": 70,
                    "icon": "img/gunbreaker.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 74,
                            "session_id": 8,
                            "role_id": 74,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 70,
                    "session_id": 8,
                    "role_id": 70,
                    "operator": "eq",
                    "value": 2
                }
            ]
        },
        {
            "id": 76,
            "session_id": 8,
            "name": "White Mage",
            "parent_id": 75,
            "icon": "img/whitemage.png",
            "children": [],
            "rules": [
                {
                    "id": 76,
                    "session_id": 8,
                    "role_id": 76,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 77,
            "session_id": 8,
            "name": "Scholar",
            "parent_id": 75,
            "icon": "img/scholar.png",
            "children": [],
            "rules": [
                {
                    "id": 77,
                    "session_id": 8,
                    "role_id": 77,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 78,
            "session_id": 8,
            "name": "Astrologian",
            "parent_id": 75,
            "icon": "img/astrologian.png",
            "children": [],
            "rules": [
                {
                    "id": 78,
                    "session_id": 8,
                    "role_id": 78,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 75,
            "session_id": 8,
            "name": "Healer",
            "parent_id": None,
            "icon": "img/healer.png",
            "children": [
                {
                    "id": 76,
                    "session_id": 8,
                    "name": "White Mage",
                    "parent_id": 75,
                    "icon": "img/whitemage.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 76,
                            "session_id": 8,
                            "role_id": 76,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 77,
                    "session_id": 8,
                    "name": "Scholar",
                    "parent_id": 75,
                    "icon": "img/scholar.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 77,
                            "session_id": 8,
                            "role_id": 77,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 78,
                    "session_id": 8,
                    "name": "Astrologian",
                    "parent_id": 75,
                    "icon": "img/astrologian.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 78,
                            "session_id": 8,
                            "role_id": 78,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 75,
                    "session_id": 8,
                    "role_id": 75,
                    "operator": "eq",
                    "value": 2
                }
            ]
        },
        {
            "id": 81,
            "session_id": 8,
            "name": "Monk",
            "parent_id": 80,
            "icon": "img/monk.png",
            "children": [],
            "rules": [
                {
                    "id": 81,
                    "session_id": 8,
                    "role_id": 81,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 82,
            "session_id": 8,
            "name": "Dragoon",
            "parent_id": 80,
            "icon": "img/dragoon.png",
            "children": [],
            "rules": [
                {
                    "id": 82,
                    "session_id": 8,
                    "role_id": 82,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 83,
            "session_id": 8,
            "name": "Ninja",
            "parent_id": 80,
            "icon": "img/ninja.png",
            "children": [],
            "rules": [
                {
                    "id": 83,
                    "session_id": 8,
                    "role_id": 83,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 84,
            "session_id": 8,
            "name": "Samurai",
            "parent_id": 80,
            "icon": "img/samurai.png",
            "children": [],
            "rules": [
                {
                    "id": 84,
                    "session_id": 8,
                    "role_id": 84,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 80,
            "session_id": 8,
            "name": "Melee DPS",
            "parent_id": 79,
            "icon": "img/melee.png",
            "children": [
                {
                    "id": 81,
                    "session_id": 8,
                    "name": "Monk",
                    "parent_id": 80,
                    "icon": "img/monk.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 81,
                            "session_id": 8,
                            "role_id": 81,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 82,
                    "session_id": 8,
                    "name": "Dragoon",
                    "parent_id": 80,
                    "icon": "img/dragoon.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 82,
                            "session_id": 8,
                            "role_id": 82,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 83,
                    "session_id": 8,
                    "name": "Ninja",
                    "parent_id": 80,
                    "icon": "img/ninja.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 83,
                            "session_id": 8,
                            "role_id": 83,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 84,
                    "session_id": 8,
                    "name": "Samurai",
                    "parent_id": 80,
                    "icon": "img/samurai.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 84,
                            "session_id": 8,
                            "role_id": 84,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 80,
                    "session_id": 8,
                    "role_id": 80,
                    "operator": "ge",
                    "value": 1
                }
            ]
        },
        {
            "id": 86,
            "session_id": 8,
            "name": "Bard",
            "parent_id": 85,
            "icon": "img/bard.png",
            "children": [],
            "rules": [
                {
                    "id": 86,
                    "session_id": 8,
                    "role_id": 86,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 87,
            "session_id": 8,
            "name": "Machinist",
            "parent_id": 85,
            "icon": "img/machinist.png",
            "children": [],
            "rules": [
                {
                    "id": 87,
                    "session_id": 8,
                    "role_id": 87,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 88,
            "session_id": 8,
            "name": "Dancer",
            "parent_id": 85,
            "icon": "img/dancer.png",
            "children": [],
            "rules": [
                {
                    "id": 88,
                    "session_id": 8,
                    "role_id": 88,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 85,
            "session_id": 8,
            "name": "Physical Ranged DPS",
            "parent_id": 79,
            "icon": "img/pranged.png",
            "children": [
                {
                    "id": 86,
                    "session_id": 8,
                    "name": "Bard",
                    "parent_id": 85,
                    "icon": "img/bard.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 86,
                            "session_id": 8,
                            "role_id": 86,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 87,
                    "session_id": 8,
                    "name": "Machinist",
                    "parent_id": 85,
                    "icon": "img/machinist.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 87,
                            "session_id": 8,
                            "role_id": 87,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 88,
                    "session_id": 8,
                    "name": "Dancer",
                    "parent_id": 85,
                    "icon": "img/dancer.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 88,
                            "session_id": 8,
                            "role_id": 88,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 85,
                    "session_id": 8,
                    "role_id": 85,
                    "operator": "ge",
                    "value": 1
                }
            ]
        },
        {
            "id": 90,
            "session_id": 8,
            "name": "Black Mage",
            "parent_id": 89,
            "icon": "img/blackmage.png",
            "children": [],
            "rules": [
                {
                    "id": 90,
                    "session_id": 8,
                    "role_id": 90,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 91,
            "session_id": 8,
            "name": "Summoner",
            "parent_id": 89,
            "icon": "img/summoner.png",
            "children": [],
            "rules": [
                {
                    "id": 91,
                    "session_id": 8,
                    "role_id": 91,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 92,
            "session_id": 8,
            "name": "Red Mage",
            "parent_id": 89,
            "icon": "img/redmage.png",
            "children": [],
            "rules": [
                {
                    "id": 92,
                    "session_id": 8,
                    "role_id": 92,
                    "operator": "le",
                    "value": 1
                }
            ]
        },
        {
            "id": 89,
            "session_id": 8,
            "name": "Magic Ranged DPS",
            "parent_id": 79,
            "icon": "img/caster.png",
            "children": [
                {
                    "id": 90,
                    "session_id": 8,
                    "name": "Black Mage",
                    "parent_id": 89,
                    "icon": "img/blackmage.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 90,
                            "session_id": 8,
                            "role_id": 90,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 91,
                    "session_id": 8,
                    "name": "Summoner",
                    "parent_id": 89,
                    "icon": "img/summoner.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 91,
                            "session_id": 8,
                            "role_id": 91,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 92,
                    "session_id": 8,
                    "name": "Red Mage",
                    "parent_id": 89,
                    "icon": "img/redmage.png",
                    "children": [],
                    "rules": [
                        {
                            "id": 92,
                            "session_id": 8,
                            "role_id": 92,
                            "operator": "le",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 89,
                    "session_id": 8,
                    "role_id": 89,
                    "operator": "ge",
                    "value": 1
                }
            ]
        },
        {
            "id": 79,
            "session_id": 8,
            "name": "DPS",
            "parent_id": None,
            "icon": "img/dps.png",
            "children": [
                {
                    "id": 80,
                    "session_id": 8,
                    "name": "Melee DPS",
                    "parent_id": 79,
                    "icon": "img/melee.png",
                    "children": [
                        {
                            "id": 81,
                            "session_id": 8,
                            "name": "Monk",
                            "parent_id": 80,
                            "icon": "img/monk.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 81,
                                    "session_id": 8,
                                    "role_id": 81,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 82,
                            "session_id": 8,
                            "name": "Dragoon",
                            "parent_id": 80,
                            "icon": "img/dragoon.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 82,
                                    "session_id": 8,
                                    "role_id": 82,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 83,
                            "session_id": 8,
                            "name": "Ninja",
                            "parent_id": 80,
                            "icon": "img/ninja.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 83,
                                    "session_id": 8,
                                    "role_id": 83,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 84,
                            "session_id": 8,
                            "name": "Samurai",
                            "parent_id": 80,
                            "icon": "img/samurai.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 84,
                                    "session_id": 8,
                                    "role_id": 84,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 80,
                            "session_id": 8,
                            "role_id": 80,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 85,
                    "session_id": 8,
                    "name": "Physical Ranged DPS",
                    "parent_id": 79,
                    "icon": "img/pranged.png",
                    "children": [
                        {
                            "id": 86,
                            "session_id": 8,
                            "name": "Bard",
                            "parent_id": 85,
                            "icon": "img/bard.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 86,
                                    "session_id": 8,
                                    "role_id": 86,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 87,
                            "session_id": 8,
                            "name": "Machinist",
                            "parent_id": 85,
                            "icon": "img/machinist.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 87,
                                    "session_id": 8,
                                    "role_id": 87,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 88,
                            "session_id": 8,
                            "name": "Dancer",
                            "parent_id": 85,
                            "icon": "img/dancer.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 88,
                                    "session_id": 8,
                                    "role_id": 88,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 85,
                            "session_id": 8,
                            "role_id": 85,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                },
                {
                    "id": 89,
                    "session_id": 8,
                    "name": "Magic Ranged DPS",
                    "parent_id": 79,
                    "icon": "img/caster.png",
                    "children": [
                        {
                            "id": 90,
                            "session_id": 8,
                            "name": "Black Mage",
                            "parent_id": 89,
                            "icon": "img/blackmage.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 90,
                                    "session_id": 8,
                                    "role_id": 90,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 91,
                            "session_id": 8,
                            "name": "Summoner",
                            "parent_id": 89,
                            "icon": "img/summoner.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 91,
                                    "session_id": 8,
                                    "role_id": 91,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        },
                        {
                            "id": 92,
                            "session_id": 8,
                            "name": "Red Mage",
                            "parent_id": 89,
                            "icon": "img/redmage.png",
                            "children": [],
                            "rules": [
                                {
                                    "id": 92,
                                    "session_id": 8,
                                    "role_id": 92,
                                    "operator": "le",
                                    "value": 1
                                }
                            ]
                        }
                    ],
                    "rules": [
                        {
                            "id": 89,
                            "session_id": 8,
                            "role_id": 89,
                            "operator": "ge",
                            "value": 1
                        }
                    ]
                }
            ],
            "rules": [
                {
                    "id": 79,
                    "session_id": 8,
                    "role_id": 79,
                    "operator": "eq",
                    "value": 4
                }
            ]
        }
    ],
    "all_rules": [
        {
            "id": 70,
            "session_id": 8,
            "role_id": 70,
            "operator": "eq",
            "value": 2
        },
        {
            "id": 71,
            "session_id": 8,
            "role_id": 71,
            "operator": "le",
            "value": 1
        },
        {
            "id": 72,
            "session_id": 8,
            "role_id": 72,
            "operator": "le",
            "value": 1
        },
        {
            "id": 73,
            "session_id": 8,
            "role_id": 73,
            "operator": "le",
            "value": 1
        },
        {
            "id": 74,
            "session_id": 8,
            "role_id": 74,
            "operator": "le",
            "value": 1
        },
        {
            "id": 75,
            "session_id": 8,
            "role_id": 75,
            "operator": "eq",
            "value": 2
        },
        {
            "id": 76,
            "session_id": 8,
            "role_id": 76,
            "operator": "le",
            "value": 1
        },
        {
            "id": 77,
            "session_id": 8,
            "role_id": 77,
            "operator": "le",
            "value": 1
        },
        {
            "id": 78,
            "session_id": 8,
            "role_id": 78,
            "operator": "le",
            "value": 1
        },
        {
            "id": 79,
            "session_id": 8,
            "role_id": 79,
            "operator": "eq",
            "value": 4
        },
        {
            "id": 80,
            "session_id": 8,
            "role_id": 80,
            "operator": "ge",
            "value": 1
        },
        {
            "id": 81,
            "session_id": 8,
            "role_id": 81,
            "operator": "le",
            "value": 1
        },
        {
            "id": 82,
            "session_id": 8,
            "role_id": 82,
            "operator": "le",
            "value": 1
        },
        {
            "id": 83,
            "session_id": 8,
            "role_id": 83,
            "operator": "le",
            "value": 1
        },
        {
            "id": 84,
            "session_id": 8,
            "role_id": 84,
            "operator": "le",
            "value": 1
        },
        {
            "id": 85,
            "session_id": 8,
            "role_id": 85,
            "operator": "ge",
            "value": 1
        },
        {
            "id": 86,
            "session_id": 8,
            "role_id": 86,
            "operator": "le",
            "value": 1
        },
        {
            "id": 87,
            "session_id": 8,
            "role_id": 87,
            "operator": "le",
            "value": 1
        },
        {
            "id": 88,
            "session_id": 8,
            "role_id": 88,
            "operator": "le",
            "value": 1
        },
        {
            "id": 89,
            "session_id": 8,
            "role_id": 89,
            "operator": "ge",
            "value": 1
        },
        {
            "id": 90,
            "session_id": 8,
            "role_id": 90,
            "operator": "le",
            "value": 1
        },
        {
            "id": 91,
            "session_id": 8,
            "role_id": 91,
            "operator": "le",
            "value": 1
        },
        {
            "id": 92,
            "session_id": 8,
            "role_id": 92,
            "operator": "le",
            "value": 1
        }
    ]
}
