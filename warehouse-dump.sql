--
-- File generated with SQLiteStudio v3.1.1 on Mon Nov 14 12:15:41 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: customers
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    cid  INTEGER UNIQUE
                 NOT NULL,
    name TEXT    UNIQUE
                 NOT NULL
);

-- Table: methods
CREATE TABLE methods (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    UNIQUE
                 NOT NULL
);
INSERT INTO methods (id, name) VALUES (1, 'vitros');
INSERT INTO methods (id, name) VALUES (2, 'bcg');
INSERT INTO methods (id, name) VALUES (3, 'bcp');
INSERT INTO methods (id, name) VALUES (4, 'IFCC');
INSERT INTO methods (id, name) VALUES (5, 'AACC');
INSERT INTO methods (id, name) VALUES (6, 'DGKC');
INSERT INTO methods (id, name) VALUES (7, 'Beckman');
INSERT INTO methods (id, name) VALUES (8, 'REFLO');
INSERT INTO methods (id, name) VALUES (9, 'DADE');
INSERT INTO methods (id, name) VALUES (10, 'KE-wout-pyridoxal');
INSERT INTO methods (id, name) VALUES (11, 'KE-pyridoxal');
INSERT INTO methods (id, name) VALUES (12, 'enzyme-kinetic');
INSERT INTO methods (id, name) VALUES (13, 'enzyme');

-- Table: results
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

-- Table: tests
CREATE TABLE tests (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    UNIQUE
                 NOT NULL
);
INSERT INTO tests (id, name) VALUES (1, 'alp');
INSERT INTO tests (id, name) VALUES (2, 'albumin');
INSERT INTO tests (id, name) VALUES (3, 'alt');
INSERT INTO tests (id, name) VALUES (4, 'ast');
INSERT INTO tests (id, name) VALUES (5, 'bun');

-- Table: trial_sum
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

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
