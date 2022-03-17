-- create a users table
-- parameters: id, email, name
CREATE TABLE If NOT EXISTS users (  
    id INT NOT NULL  AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(`id`)
);