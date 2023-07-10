<h2 style="margin: auto; width: 9%;"> Guild </h2>

| name | type | null | other | desctiption |
| :-: | :-: | :-: | :-: | :-: |
| rowid | INTEGER | NOT NULL  | PRIMARY KEY AUTOINCREMENT | row id at the db |
| guild_id | INTEGER | NOT NULL | UNIQUE | guild id at discord |
| owner | INTEGER | NOT NULL |  | owner's id at discord |
| custom_voice_entery_id | INTEGER | NULL |  | voice channel for creating temp voice channels
| is_blacklisted | BOOLEAN(INT) | NOT NULL | DEFAULT (0) | is guild is blacklisted (cannot execute any commands) |