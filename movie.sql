-- Create a new database
CREATE DATABASE movie_fan_club;

-- Use the new database
USE movie_fan_club;

-- Create a table to store fan club members
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    favorite_movie VARCHAR(100) NOT NULL,
    membership_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Insert some initial data (for testing)
INSERT INTO members (name, favorite_movie) 
VALUES ('Alice', 'The Matrix'), 
       ('Bob', 'Inception'),
       ('Jackie','Titanic'),
       ('Clair', 'Smile');
