create TABLE IF NOT EXISTS table_A (
    a integer,
    b integer,
    c integer
)
;

INSERT INTO table_A (a, b, c) 
VALUES (1, 7, 9)
;

SELECT * FROM table_A
;

DROP table IF EXISTS table_A
;