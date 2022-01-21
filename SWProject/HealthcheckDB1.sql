# data for health check app
CREATE DATABASE healthcheck10;
USE healthcheck10;
 

DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS NewUsers;
DROP TABLE IF EXISTS Log;
DROP TABLE IF EXISTS SugDis;
DROP TABLE IF EXISTS Suggestions;

DROP TABLE IF EXISTS Users;
# Table creation! Create Tables 
#with Foreign Keys after the referenced tables are created!

CREATE TABLE Users
	(userID		int,
	 email		VARCHAR(30),
	 userpassword	VARCHAR(20),
     usertype		VARCHAR(1),
     #sex 			char(1),
     state 			int,
     # 1-- on; 0--off
	 PRIMARY KEY(userID) 
	);

CREATE TABLE Patient
	(userID		int, 
	 #firstname		VARCHAR(15), 
	 #lastname		    VARCHAR(20),
     city		VARCHAR(20),
     age		int,
     sex		char(1),
     weight		INT,
     height		INT,
     chol		int,
     skin_thickness  int,
     glucose	int,
	 PRIMARY KEY(userID),
     FOREIGN KEY (userID) REFERENCES Users(userID) on delete cascade 
	);

CREATE TABLE Doctor
	(userID		int, 
	 fistname			VARCHAR(15), 
	 lastname		VARCHAR(20),
	 occupatient		varchar(50),
	 PRIMARY KEY(userID),
	  FOREIGN KEY(userID) REFERENCES Users(userID) ON delete cascade
	);

CREATE TABLE NewUsers
	(email		VARCHAR(30),
    Timestamps	TIME, # find out what time format we use,
	 PRIMARY KEY (email)
	);

CREATE TABLE Log
	(userID		int, 
     city		VARCHAR(20),
     age		int,
     sex	char(1),
     weight		INT,
     height		INT,
     chol	INT,
     skinthickness		INT,
     gluc	int,
     Timestamps	TIME, # find out what time format we use
	 PRIMARY KEY(userID),
     FOREIGN KEY (userID) REFERENCES Users(userID)
	);

CREATE TABLE Suggestions
	(sugID			int, 
	 suggestion		VARCHAR(200),
	 ranking		INT(1), 
     userID	int, # the doctor who made suggestion
     disID  VARCHAR(5),
     PRIMARY KEY(sugID),
     FOREIGN KEY (userID) REFERENCES Users(userID) on delete cascade
	);


# Insertion of multiple table rows in one go!

INSERT Users VALUES
(1,'user@user1.com','1234','D',1),
(2,'user@user2.com','12345','D',1),
(3,'user@user4.com','123456','P',1),
(4,'user@user4.com','123456','P',1);

INSERT Patient VALUES
(3,'Seoul',20,'f',75,175,100,20,130),
(4,'Busan',19,'m',69,168,110,17,120);

INSERT Doctor values
(1,'Brian','Obama','Docrtor Seoul hospital'),
(2,'Albert', 'schwatz','Berlin central hospital');

insert NewUsers values
('iam@new.com','08:00');

insert Suggestions values
(1,'Exercise two times a week in 30 min',3,2,'pima'),
(2,'Exercise three times a week in 40 min',1,2,'pima'),
(3,'exercise four times a week in 50 min',5,1,'heart'),
(4,'exercise five times a week in 10 min',1,2,'heart'),
(5,'exercise one time a week in 20 min',1,1,'both'),
(6,'exercise two times a month in 30 minutes',2,2,'both');



