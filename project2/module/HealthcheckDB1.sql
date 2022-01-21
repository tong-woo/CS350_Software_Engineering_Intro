# data for health check app
CREATE DATABASE healthcheck;
USE healthcheck;
 

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
	(userID		VARCHAR(5),
	 email		VARCHAR(30),
	 userpassword	VARCHAR(20),
     usertype		VARCHAR(1),
	 PRIMARY KEY(userID) 
	);

CREATE TABLE Patient
	(userID		VARCHAR(5), 
	 firstname		VARCHAR(15), 
	 lastname		    VARCHAR(20),
     birth	DATE,
     city		VARCHAR(20),
     height		INT(3),
     weight		INT(3),
     skinthickness		INT(2),
     chol	INT(3),
	 PRIMARY KEY(userID),
     FOREIGN KEY (userID) REFERENCES Users(userID) on delete cascade 
	);

CREATE TABLE Doctor
	(userID		VARCHAR(5), 
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
	(userID		VARCHAR(5), 
     city		VARCHAR(20),
     height		INT(3),
     weight		INT(3),
     skinthickness		INT(2),
     chol	INT(3),
     Timestamps	TIME, # find out what time format we use
	 PRIMARY KEY(userID),
     FOREIGN KEY (userID) REFERENCES Users(userID)
	);

CREATE TABLE Suggestions
	(sugID			VARCHAR(5), 
	 suggestion		VARCHAR(200),
	 ranking		INT(1), 
     userID	VARCHAR(5), # the doctor who made suggestion
     PRIMARY KEY(sugID),
     FOREIGN KEY (userID) REFERENCES Users(userID) on delete cascade
	);
    
CREATE TABLE SugDis
(disID		VARCHAR(5),
sugID		VARCHAR(5),
primary key(sugID,disID),
FOREIGN KEY (sugID) REFERENCES Suggestions(sugID) on delete cascade);



# Insertion of multiple table rows in one go!

INSERT Users VALUES
('1','user@user1.com','1234','D'),
('2','user@user2.com','12345','D'),
('3','user@user4.com','123456','P'),
('4','user@user4.com','123456','P');

INSERT Patient VALUES
('3','Kim','Kim','1992-04-18','Seoul',175,75,15,85),
('4','Hans', 'Mikkelsen','1984-10-01','Busan',168,69,20,100);

INSERT Doctor values
('1','Brian','Obama','Docrtor Seoul hospital'),
('2','Albert', 'schwatz','Berlin central hospital');

insert NewUsers values
('iam@new.com','08:00'),
('123@163.com','09:00');

insert Suggestions values
('sug1','Exercise two times a week in 30 min',3,'2');

insert SugDis values
('dis01','sug1');


