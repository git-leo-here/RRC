CREATE DATABASE IF NOT EXISTS School;
USE School;
CREATE TABLE adminTeachers( TeacherID INT AUTO_INCREMENT , Name VARCHAR(32) NOT NULL , password VARCHAR(12) NOT NULL , PRIMARY KEY (TeacherID));
CREATE TABLE adminStudents( StudentID INT AUTO_INCREMENT , StudentName VARCHAR(32) NOT NULL , GuardianName CHAR(32) NOT NULL , DOB DATE , PRIMARY KEY (StudentID));
CREATE TABLE adminMain( ClassSec varchar(3), TeacherID int , subjects SET('P','C','M','B') NOT NULL , PRIMARY KEY (ClassSec) , FOREIGN KEY (TeacherID) REFERENCES adminTeachers(TeacherID) );
