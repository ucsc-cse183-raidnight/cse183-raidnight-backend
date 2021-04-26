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
