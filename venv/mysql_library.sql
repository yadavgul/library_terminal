CREATE DATABASE IF NOT EXISTS mysql_library;

USE mysql_library;

#--- user table ---
drop table if exists users;

create table users(
user_id int not null auto_increment,
user_name varchar(40) not null,
user_phone int not null,
user_password varchar(40) not null,
primary key(user_id)
);

#--- librarian table ---
drop table if exists librarian;

create table librarian(
libr_id int not null auto_increment,
libr_name varchar(40) not null,
libr_email varchar(40) not null,
libr_phone int not null,
libr_password varchar(40) not null,
primary key(libr_id)
);

#--- book table ---
drop table if exists book;

create table book(
book_id int not null auto_increment,
author varchar(40) not null,
book_nam varchar(40) not null,
publication varchar(50) not null,
available boolean,
primary key(book_id)
);

# --- rented books table ---
drop table if exists rented_books;

create table rented_books (
book_id int not null,
user_id int not null,
rented_date date not null,
due_date date not null,
returned_date date,
fee float,

CONSTRAINT `book_id_f` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`),
CONSTRAINT `user_id_f` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
);





