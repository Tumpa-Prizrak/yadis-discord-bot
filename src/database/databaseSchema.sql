CREATE TABLE Guild (
    rowid                  INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id               INTEGER NOT NULL
                                   UNIQUE,
    owner                  INTEGER NOT NULL,
    custom_voice_entery_id INTEGER,
    is_blacklisted         INTEGER DEFAULT (0) 
                                   NOT NULL
);
