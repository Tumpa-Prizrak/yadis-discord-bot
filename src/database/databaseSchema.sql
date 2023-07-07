CREATE TABLE Guild (
    rowid                  INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id               INTEGER NOT NULL
                                   UNIQUE,
    name                   TEXT    NOT NULL,
    owner                  INTEGER NOT NULL,
    member_count           INTEGER NOT NULL
                                   DEFAULT (0),
    custom_voice_entery_id INTEGER
);
