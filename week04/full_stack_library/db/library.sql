DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  checked_in BOOLEAN,
  author_id INT NOT NULL REFERENCES authors(id)
);

insert into authors (first_name, last_name) VALUES('Miss', 'Marple');
insert into authors (first_name, last_name) VALUES('William', 'Shakespeare');
insert into authors (first_name, last_name) VALUES('Dan', 'Brown');

insert into books (title, genre, checked_in, author_id) VALUES('The Davinci Code', 'Fiction', True, 3);
insert into books (title, genre, checked_in, author_id) VALUES('Murder on the Orient Express', 'Fiction', True, 1);
insert into books (title, genre, checked_in, author_id) VALUES('Romeo and Juliet', 'Fiction', True, 2);
insert into books (title, genre, checked_in, author_id) VALUES('The Tempest', 'Fiction', True, 2);
insert into books (title, genre, checked_in, author_id) VALUES('The Computer One', 'Fiction', True, 3);
insert into books (title, genre, checked_in, author_id) VALUES('Ten Little Indians', 'Fiction', True, 1);