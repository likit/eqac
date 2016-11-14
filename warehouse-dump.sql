--
-- File generated with SQLiteStudio v3.1.1 on Mon Nov 14 14:40:08 2016
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
INSERT INTO methods (id, name) VALUES (1, 'Vitros');
INSERT INTO methods (id, name) VALUES (2, 'BCG');
INSERT INTO methods (id, name) VALUES (3, 'BCP');
INSERT INTO methods (id, name) VALUES (4, 'IFCC');
INSERT INTO methods (id, name) VALUES (5, 'AACC');
INSERT INTO methods (id, name) VALUES (6, 'DGKC');
INSERT INTO methods (id, name) VALUES (7, 'Beckman');
INSERT INTO methods (id, name) VALUES (8, 'REFLO');
INSERT INTO methods (id, name) VALUES (9, 'DADE');
INSERT INTO methods (id, name) VALUES (10, 'KE-wout-pyridoxal');
INSERT INTO methods (id, name) VALUES (11, 'KE-pyridoxal');
INSERT INTO methods (id, name) VALUES (12, 'Enzyme-kinetic');
INSERT INTO methods (id, name) VALUES (13, 'Enzyme');
INSERT INTO methods (id, name) VALUES (14, 'Jendrassik-Grof');
INSERT INTO methods (id, name) VALUES (15, 'Malloy-Evelyn');
INSERT INTO methods (id, name) VALUES (16, 'DCA/DPD');
INSERT INTO methods (id, name) VALUES (17, 'Diazonium');
INSERT INTO methods (id, name) VALUES (18, 'CPC/Asenazo');
INSERT INTO methods (id, name) VALUES (19, 'ISE');
INSERT INTO methods (id, name) VALUES (20, 'ISE-direct');
INSERT INTO methods (id, name) VALUES (21, 'ISE-indirect');
INSERT INTO methods (id, name) VALUES (22, 'Enzyme-Colorimetric');
INSERT INTO methods (id, name) VALUES (23, 'CK-NAC');
INSERT INTO methods (id, name) VALUES (24, 'Colorimatric');
INSERT INTO methods (id, name) VALUES (25, 'Jaffe-Kinetic');
INSERT INTO methods (id, name) VALUES (26, 'Jaffe-EP');
INSERT INTO methods (id, name) VALUES (27, 'GOD');
INSERT INTO methods (id, name) VALUES (28, 'HK');
INSERT INTO methods (id, name) VALUES (29, 'GDH');
INSERT INTO methods (id, name) VALUES (30, 'Direct-determination');
INSERT INTO methods (id, name) VALUES (31, 'Phospho.Precip./Polyanioin');
INSERT INTO methods (id, name) VALUES (32, 'Others');
INSERT INTO methods (id, name) VALUES (33, 'SSCC');
INSERT INTO methods (id, name) VALUES (34, 'Molybdenum-EP');
INSERT INTO methods (id, name) VALUES (35, 'Molybdenum-UV');
INSERT INTO methods (id, name) VALUES (36, 'Biuret-Blank');
INSERT INTO methods (id, name) VALUES (37, 'Biuret-Unblank');
INSERT INTO methods (id, name) VALUES (38, 'EnzColorTotalTG');
INSERT INTO methods (id, name) VALUES (39, 'Glycerol-Blank');
INSERT INTO methods (id, name) VALUES (40, 'Enzyme-EP-Blank');
INSERT INTO methods (id, name) VALUES (41, 'Enzyme-EP-Unblank');

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
INSERT INTO tests (id, name) VALUES (6, 'bilirubin');
INSERT INTO tests (id, name) VALUES (7, 'calcium');
INSERT INTO tests (id, name) VALUES (8, 'chloride');
INSERT INTO tests (id, name) VALUES (9, 'cholesterol');
INSERT INTO tests (id, name) VALUES (10, 'ck');
INSERT INTO tests (id, name) VALUES (11, 'creatinine');
INSERT INTO tests (id, name) VALUES (12, 'ggt');
INSERT INTO tests (id, name) VALUES (13, 'glucose');
INSERT INTO tests (id, name) VALUES (14, 'hdl');
INSERT INTO tests (id, name) VALUES (15, 'ldh');
INSERT INTO tests (id, name) VALUES (16, 'ldl');
INSERT INTO tests (id, name) VALUES (17, 'inorp');
INSERT INTO tests (id, name) VALUES (18, 'potassium');
INSERT INTO tests (id, name) VALUES (19, 'protein');
INSERT INTO tests (id, name) VALUES (20, 'sodium');
INSERT INTO tests (id, name) VALUES (21, 'triglyceride');
INSERT INTO tests (id, name) VALUES (22, 'uric-acid');

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
