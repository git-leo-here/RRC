CREATE DATABASE IF NOT EXISTS School;
USE School;
CREATE TABLE IF NOT EXISTS adminTeachers( TeacherID INT AUTO_INCREMENT , Name VARCHAR(32) NOT NULL , password VARCHAR(12) NOT NULL , ClassSec varchar(3) , PRIMARY KEY (TeacherID));
CREATE TABLE IF NOT EXISTS adminStudents( StudentID INT AUTO_INCREMENT , StudentName VARCHAR(32) NOT NULL , GuardianName CHAR(32) NOT NULL , DOB DATE , PRIMARY KEY (StudentID));
-- CREATE TABLE IF NOT EXISTS adminMain( ClassSec varchar(3), TeacherID int , subjects SET('P','C','M','B') NOT NULL , PRIMARY KEY (ClassSec) , FOREIGN KEY (TeacherID) REFERENCES adminTeachers(TeacherID) );


alter table adminTeachers modify column name varchar(32);
alter table adminTeachers modify column password varchar(12);
alter table adminStudents modify column StudentName char(32);
alter table adminStudents modify column GuardianName char(32);


