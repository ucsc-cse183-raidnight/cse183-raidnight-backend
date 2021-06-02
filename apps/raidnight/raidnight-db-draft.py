CREATE TABLE `game_sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `owner_id_fk` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_sessions',  # not to be confused with sessions, the user kind
    Field('name', 'string', length=128, notnull=True),
    Field('description', 'text', length=2048, notnull=False),
    Field('owner_id', 'reference auth_user', notnull=False),  # can be null to signify anonymous owner
    Field('selected_time_offset', 'double', notnull=False),
    Field('selected_time_duration', 'double', notnull=False),
    Field('selected_time_timezone', 'string', notnull=False, length=512),
    # 1->X: game_signups
    # 1->X: game_invites
    # 1->X: game_roles
    # 1->X: game_rules
)

CREATE TABLE `game_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `icon` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
  CONSTRAINT `parent_id_fk` FOREIGN KEY (`parent_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_roles',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('name', 'string', notnull=True, length=128),
    Field('parent_id', 'reference game_roles'),
    Field('icon', 'string', length=512)
)

CREATE TABLE `game_rules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rule_operator` varchar(64) NOT NULL,
  `rule_value` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
  CONSTRAINT `role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_rules',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('role_id', 'reference game_roles', notnull=True),
    Field('rule_operator', 'string', notnull=True, length=64),
    Field('rule_value', 'integer') #??
)

CREATE TABLE `game_signups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anonymous_name` varchar(128),
  PRIMARY KEY (`id`),
  CONSTRAINT `user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE # can be null
  CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_signups',
    Field('user_id', 'reference auth_user', notnull=False),  # if null, anonymous_name must be not null
    Field('anonymous_name', 'string', length=128),  # mutex user_id
    Field('session_id', 'reference game_sessions', notnull=True)
    # 1->X: game_signup_times
    # 1->X: game_signup_roles
)

CREATE TABLE `game_signup_times` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timezone` varchar(512) NOT NULL,
  `offset` DOUBLE NOT NULL,
  `duration` DOUBLE NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `signup_id_fk` FOREIGN KEY (`signup_id`) REFERENCES `game_signups` (`id`) ON DELETE CASCADE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_signup_times',
    Field('signup_id', 'reference game_signups', notnull=True),
    Field('timezone', 'string', notnull=True, length=512),  # e.g. America/Los_Angeles
    Field('offset', 'double', notnull=True),
    Field('duration', 'double', notnull=True)
)

CREATE TABLE `game_signup_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weight` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `signup_id_fk` FOREIGN KEY (`signup_id`) REFERENCES `game_signups` (`id`) ON DELETE CASCADE 
  CONSTRAINT `role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_signup_roles',
    Field('signup_id', 'reference game_signups', notnull=True),
    Field('role_id', 'reference game_roles', notnull=True),
    Field('weight', 'integer', notnull=True)
)

CREATE TABLE `game_invites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(512) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

db.define_table(
    'game_invites',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('key', 'string', notnull=True, length=128)
)
