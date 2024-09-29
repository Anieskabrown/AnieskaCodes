-- First I created my database for my Library System 'CREATE DATABASE' command creates my database for me 
CREATE DATABASE zakiyas_cosy_pages_library;

USE zakiyas_cosy_pages_library; -- Here I used the 'USE' command to sets it as the current database so my tables and queries know they belong to the  zakiyas_cosy_pages_libary database.

-- Here I have created a table for the members of my library
CREATE TABLE Members (
    member_id INT PRIMARY KEY,-- is the primary key 
    first_name VARCHAR(50), -- Varchar for text data (e.g names,emails)
    last_name VARCHAR(50),
    phone_number VARCHAR(15),
    email VARCHAR(100) UNIQUE -- I've UNIQUE constriants ensures that no two members of my library has the same email address
);

INSERT INTO Members 
(member_id, first_name, last_name, phone_number, email)
VALUES 
('54','Christoper','Brown', '0738020482', 'chrisbrown02@gmail.com'),
('50','Kylie', 'Jenner', '07028102830','kyliejenner@outlook.com'),
('52','Morris','Chestnut', '07293028391','morrisschestnut@gmail.com'),
('56','Nia', 'Long','0703802930','nialong@outlook.com'),
('51','Sheldon','Cooper', '070791767865','sheldoncooper@yahoo.com'),
('53','Tupac','Shakur', '074267543278','tupacshakur@outlook.com'),
('57','Maggie','Smith','071228938824','maggiesmith@yaoo.co.uk'),
('55','Chrissy', 'Teagan','073629084024', 'chrissyt@outlook.com');

-- HERE IS MY BOOKS TABLES
CREATE TABLE Books (
    Book_id INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Available_copies INT CHECK (available_copies >=0), -- I have used 'CHECK' Constraint to ensure my books availablity doesnt go below 0
    published_year INT
);

-- HERE ARE SOME MY FAVOURITE BOOKS I'VE READ AND USED AS MY DATABASE FOR MY LIBRARY  IVE DONE THIS FOR MEMBERS BORROWED_BOOKS USING THE 'INSERT' STATEMENT.
INSERT INTO Books 
(Book_id, Title, Author, Genre, published_year, Available_copies)
VALUES 
    ('101', 'The Inheritance Games', 'Jennifer Lawrence', 'Thriller', 2020, 9),
    ('102', 'The Final Gambit', 'Jennifer Lawrence', 'Mystery', 2021, 10),
    ('103', 'It Happened One Summer', 'Tessa Bailey', 'Rom-Com', 2019, 7),
    ('104', 'Never Lied', 'Freida McFadden', 'Psychological thriller', 2022, 8),
    ('105', 'The Housemaid', 'Freida McFadden', 'Domestic Fiction', 2024, 3),
    ('106', 'Terms and Conditions', 'Lauren Asher', 'Romance novel', 2018, 7),
    ('107', 'Final Offer', 'Lauren Asher', 'Romance novel', 2022, 1),
    ('108', 'The Fine Print', 'Lauren Asher', 'Romance novel', 2020, 6),
    ('109', 'Verity', 'Colleen Hoover', 'Psychological thriller', 2020, 2),
    ('110', 'This Could Be Us', 'Kennedy Ryan', 'Contemporary romance', 2023, 3),
    ('111', 'All Ive Wanted All Ive Needed', 'A.E Valdez', 'Contemporary romance', 2024, 4),
    ('112', 'Maybe Someday', 'Colleen Hoover', 'Contemporary romance', 2020, 5);


-- Here is a table for detailing the borrowing system
CREATE TABLE Borrowed_Books (
Borrow_id INT PRIMARY KEY,
Book_Id INT,
Member_Id INT,
Borrow_Date DATE,
Return_Date DATE, -- 'Date' is here to log the borrow and return dates of the boooks
FOREIGN KEY (Book_Id) REFERENCES Books (Book_Id),-- I've use 'FOREIGN KEY' which creates a relationship between borrowed books tables the books table and the members table
 FOREIGN KEY(Member_Id) REFERENCES Members (Member_Id)
);
-- This ensures that:
-- Only valid members can borrow books.
-- Only books available in the Books table can be borrowed.


INSERT INTO Borrowed_Books
(Borrow_id, Book_id, Member_Id, Borrow_Date, Return_Date)
VALUES
(5, 101, 51, '2024-01-20','2024-01-30'),
(6, 112, 50, '2024-01-25', NULL),
(7, 110, 55, '2024-01-22', '2024-02-15'),
(8, 107, 55, '2024-02-11', '2024-02-20'),
(9, 108, 53, '2024-01-30', NULL),
(10, 111, 54, '2024-01-12', '2024-02-12'),
(11, 104, 51, '2024-01-23', NULL),
(12, 105, 52, '2024-02-09', NULL);

-- 5 QUERIES TO GET RETRIEVE DATA
SELECT * FROM Members; -- RETRIEVE DATA ALL MEMBERS
SELECT * FROM Members ORDER BY last_name; -- RETRIEVE DATA ALL MEMBERS SORTED BY LAST NAME 
SELECT first_name, last_name FROM Members WHERE email LIKE '%@outlook.com%'; --  RETRIEVE DATA ALL MEMBERS SORTED BY 'OUTLOOK' EMAIL ACCOUNTS
SELECT * 
FROM Books
WHERE Title LIKE '%Final Offer%' 
   OR Author LIKE '%Laure Asher%'; --  RETRIEVE DATA ALL BOOKS SORTED BY TITLE AND AUTHOR
SELECT title, author, available_copies FROM Books ORDER BY title; -- RETRIEVES DATA OF THE BOOK TITLES AUTHORS AVAIALSBE COPES FROMM A-Z

SELECT Members.first_name, Members.last_name, Books.title, Borrowed_Books.borrow_date
FROM Borrowed_Books
JOIN Members ON Borrowed_Books.member_id = Members.member_id
JOIN Books ON Borrowed_Books.book_id = Books.book_id
ORDER BY Borrowed_Books.borrow_date; -- THIS QUERY JOINS MY LIBRARIES BORROWED BOOKS MEMEBER AND TH EBOOK ID SO I CAN SEE THE MEMBERS AND THE BOOKS THEY HAVE BORROWED AND THIS IS SORTED BY BORROWED_DATE BY THE ORDER CLAUSE
 
SELECT Title,first_name,last_name, Borrow_Date,Return_Date
FROM Borrowed_Books
JOIN Books
ON Books.Book_id = Borrowed_Books.Book_Id
JOIN  Members ON members.Member_id=Borrowed_Books.member_Id
WHERE Title = 'The Inheritance Games' -- THIS QUERY LOOKS FOR WHO HAS BORROWED A BOOK WHEN THE DID IT AND WHEN THEY WILL RETURN IT USING THER LAST NAME AND FIRST NAME AND THE BORROW AND RETURN DATE 

SELECT title, available_copies FROM Books WHERE title = 'Never Lied'; -- This Query counts the copies of books

DELETE FROM Borrowed_Books WHERE borrow_id = 1;

SELECT COUNT(member_id) AS total_members FROM Members; -- THIS QUERY USES THE COUNT STATEMENT TO LET ME KNOW HOW MANY MEMBERS IS APART OF MY LIBRARY

SELECT AVG(Available_copies) AS avg_copies FROM Books; -- This query uses AVG FUNCTION to calcuate the avg number of available copies for all my books in my library system

SELECT Books.Title, Books.Author
FROM Books
LEFT JOIN Borrowed_Books ON Books.Book_Id = Borrowed_Books.Book_Id
WHERE Borrowed_Books.Borrow_Id IS NULL; -- AS A LIBRARIAN THIS SHOWS ME WHAT BOOKS HAVNT BEEN BORROWED BY USING THE LEFT JOIN.alter

SELECT UPPER(first_name) AS first_name, UPPER(last_name) AS last_name
FROM Members
ORDER BY last_name; -- THE UPPPER FUNCTION CONVERTS MY MEMBERS NAMES TO UPPER CASE 

SELECT CONCAT(first_name, ' ', last_name) AS full_name, email
FROM Members
ORDER BY last_name; -- THIS CONCAT FUCATION RETRIEVES THE DATA Y FOCUSING ON THE FRIST AND LAST WITH A SPACE TO JOIN AND MAKE FULL NAME TABLE WHICH THEN GIVES THE EMAIL TABLE TOO 

-- Here I have created a stored procdure to retrive the list of books by a specific members usinf their id 
-- 
DELIMITER //
CREATE PROCEDURE GetBooksBorrowedByMember(IN member_id INT)
BEGIN
    SELECT Books.Title, Borrowed_Books.Borrow_Date, Borrowed_Books.Return_Date
    FROM Borrowed_Books
    JOIN Books ON Borrowed_Books.Book_Id = Books.Book_Id
    WHERE Borrowed_Books.Member_Id = member_id
    ORDER BY Borrowed_Books.Borrow_Date;
END //
DELIMITER ;
CALL GetBooksBorrowedByMember(51);

-- This stored procedure, GetBooksBorrowedByMember, takes a member_id as input and returns the list of books borrowed by that member, along with the borrow and return dates. Results are sorted by the borrow date./
-- This command will call the stored procedure and return the list of books borrowed by the member with member_id = 51.



--------
-- I think my current structure is mostly normalized. However, i could try to imporve my library database a little better by  creating a Genres table to store book genres separately and reference it in the Books table.
-- 	Below I have created a Genres table and modified the Books table to reference it using a foreign key genre_id, instead of storing genre names directly in the Books table. This eliminates any potential redundancy in the genre data.
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(50)
);

INSERT INTO Genres (genre_id, genre_name)
VALUES
(1, 'Thriller'),
(2, 'Mystery'),
(3, 'Rom-Com'),
(4, 'Psychological thriller'),
(5, 'Domestic Fiction'),
(6, 'Romance novel'),
(7, 'Contemporary romance');

ALTER TABLE Books ADD genre_id INT;
UPDATE Books
SET genre_id = 
    CASE 
        WHEN Genre = 'Thriller' THEN 1
        WHEN Genre = 'Mystery' THEN 2
        WHEN Genre = 'Rom-Com' THEN 3
        WHEN Genre = 'Psychological thriller' THEN 4
        WHEN Genre = 'Domestic Fiction' THEN 5
        WHEN Genre = 'Romance novel' THEN 6
        WHEN Genre = 'Contemporary romance' THEN 7
    END;

ALTER TABLE Books DROP COLUMN Genre;
ALTER TABLE Books ADD FOREIGN KEY (genre_id) REFERENCES Genres(genre_id);

