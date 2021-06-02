CREATE TABLE `game_sessions`
(
    `id`                     int(11)      NOT NULL AUTO_INCREMENT,
    `name`                   varchar(128) NOT NULL,
    `description`            text DEFAULT NULL,
    `owner_id`               int,
    `selected_time_offset`   double,
    `selected_time_duration` double,
    `selected_time_timezone` varchar(512),
    PRIMARY KEY (`id`),
    CONSTRAINT `owner_id_fk` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_roles`
(
    `id`         int(11)      NOT NULL AUTO_INCREMENT,
    `name`       varchar(128) NOT NULL,
    `icon`       varchar(512) DEFAULT NULL,
    `session_id` int          NOT NULL,
    `parent_id`  int,
    PRIMARY KEY (`id`),
    CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE,
    CONSTRAINT `parent_id_fk` FOREIGN KEY (`parent_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_rules`
(
    `id`            int(11)     NOT NULL AUTO_INCREMENT,
    `rule_operator` varchar(64) NOT NULL,
    `rule_value`    INT         NOT NULL,
    `session_id`    int         NOT NULL,
    `role_id`       int         NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `game_rules_session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE,
    CONSTRAINT `game_rules_role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_signups`
(
    `id`             int(11) NOT NULL AUTO_INCREMENT,
    `anonymous_name` varchar(128),
    `session_id`     int     NOT NULL,
    `user_id`        int,
    PRIMARY KEY (`id`),
    CONSTRAINT `game_signups_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `game_signups_session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_signup_times`
(
    `id`        int(11)      NOT NULL AUTO_INCREMENT,
    `timezone`  varchar(512) NOT NULL,
    `offset`    DOUBLE       NOT NULL,
    `duration`  DOUBLE       NOT NULL,
    `signup_id` int          NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `game_signup_times_signup_id_fk` FOREIGN KEY (`signup_id`) REFERENCES `game_signups` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_signup_roles`
(
    `id`        int(11) NOT NULL AUTO_INCREMENT,
    `weight`    INT     NOT NULL,
    `signup_id` int     NOT NULL,
    `role_id`   int     NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `game_signup_roles_signup_id_fk` FOREIGN KEY (`signup_id`) REFERENCES `game_signups` (`id`) ON DELETE CASCADE,
    CONSTRAINT `game_signup_roles_role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `game_roles` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `game_invites`
(
    `id`         int(11)      NOT NULL AUTO_INCREMENT,
    `key`        varchar(512) NOT NULL,
    `session_id` INT          NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `game_invites_session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `game_sessions` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;