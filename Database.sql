---------Create Database------

CREATE DATABASE face_recognizer;

--- using This Databse----

SELECT * FROM face_recognizer.student;

-----------------For using student data---------
----------- creating a table , table name student
CREATE TABLE face_recognizer.student (
  Dep VARCHAR(45) NULL,
  course VARCHAR(45) NULL,
  Year VARCHAR(45) NULL,
  semester VARCHAR(45) NULL,
  Student_id VARCHAR(45) NOT NULL,
  Name VARCHAR(45) NULL,
  Division VARCHAR(45) NULL,
  Roll VARCHAR(45) NULL,
  Gender VARCHAR(45) NULL,
  Dob VARCHAR(45) NULL,
  Email VARCHAR(45) NULL,
  Phone VARCHAR(45) NULL,
  Address VARCHAR(45) NULL,
  Teacher VARCHAR(45) NULL,
  PhotoSample VARCHAR(45) NULL,
  PRIMARY KEY (Student_id));

---------------- For Manage Attendence-----------

CREATE TABLE `stdattendance` (
  `std_id` int NOT NULL,
  `std_roll_no` varchar(45) DEFAULT NULL,
  `std_name` varchar(45) DEFAULT NULL,
  `std_time` varchar(45) DEFAULT NULL,
  `std_date` varchar(45) DEFAULT NULL,
  `std_attendance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
)

------------ For User Loogin ---------

CREATE TABLE `regteach` (
  `fname` varchar(150) DEFAULT NULL,
  `lname` varchar(150) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `ssq` varchar(150) DEFAULT NULL,
  `sa` varchar(150) DEFAULT NULL,
  `pwd` varchar(150) DEFAULT NULL
);
