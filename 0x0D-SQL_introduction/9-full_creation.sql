-- Creating new row and adding its values
CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
);

INSERT INTO second_table (id, name, score)
VALUE (1, 'John', 10),
      (2, 'Alex', 3),
      (3, 'Bob', 14),
      (4, 'George', 8);