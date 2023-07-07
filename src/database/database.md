<h2 style="margin: auto; width: 9%;"> Guild </h2>

| name | type | null | other | desctiption |
| :-: | :-: | :-: | :-: | :-: |
| rowid | INTEGER | NOT NULL  | PRIMARY KEY AUTOINCREMENT | row id at the db |
| guild_id | INTEGER | NOT NULL | UNIQUE | guild id at discord |
| name | TEXT | NOT NULL |  | name of guild |
| owner | INTEGER | NOT NULL |  | owner's id at discord |
| custom_voice_entery_id | INTEGER | NULL |  | voice channel for creating temp voice channels
| member_count | INTEGER | NOT NULL |  | meber count |
