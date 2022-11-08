DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS responses;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
    
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    response_1 TEXT,
    response_2 TEXT,
    response_3 TEXT,
    response_4 TEXT,
    response_5 TEXT,
    response_6 TEXT,
    response_7 TEXT,
    response_8 TEXT,
    response_9 TEXT,
    response_10 TEXT
);

