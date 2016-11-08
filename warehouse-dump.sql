--
-- File generated with SQLiteStudio v3.1.0 on Tue Nov 8 23:10:29 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: tests
DROP TABLE IF EXISTS tests;

CREATE TABLE tests (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    UNIQUE
                 NOT NULL
);

INSERT INTO tests (
                      id,
                      name
                  )
                  VALUES (
                      1,
                      'alp'
                  );

INSERT INTO tests (
                      id,
                      name
                  )
                  VALUES (
                      2,
                      'albumin'
                  );


-- Table: trial_sum
DROP TABLE IF EXISTS trial_sum;

CREATE TABLE trial_sum (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id   INTEGER REFERENCES tests (id),
    method_id INTEGER REFERENCES methods (id),
    sd        DECIMAL,
    cv        DECIMAL,
    mean      DECIMAL,
    new_sd    DECIMAL,
    new_cv    DECIMAL,
    new_mean  DECIMAL
);


-- Table: results
DROP TABLE IF EXISTS results;

CREATE TABLE results (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id     INTEGER REFERENCES tests (id),
    method_id   INTEGER REFERENCES methods (id),
    value       DECIMAL NOT NULL,
    customer_id INTEGER REFERENCES customers (id),
    trial       INTEGER NOT NULL,
    included    BOOLEAN,
    ccv         DECIMAL
);


-- Table: customers
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    cid  INTEGER UNIQUE
                 NOT NULL,
    name TEXT    UNIQUE
                 NOT NULL
);


-- Table: methods
DROP TABLE IF EXISTS methods;

CREATE TABLE methods (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    UNIQUE
                 NOT NULL
);

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        1,
                        'vitros'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        2,
                        'bcg'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        3,
                        'bcp'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        4,
                        'IFCC'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        5,
                        'AACC'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        6,
                        'DGKC'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        7,
                        'Beckman'
                    );

INSERT INTO methods (
                        id,
                        name
                    )
                    VALUES (
                        8,
                        'REFLO'
                    );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
