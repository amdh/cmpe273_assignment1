create database IF NOT EXISTS expenses_management_system;
use expense_management_system;

CREATE TABLE IF NOT EXISTS expenses
(
id INTEGER AUTO_INCREMENT NOT NULL,
name varchar(20) ,
email varchar(20),
category varchar(50),
description varchar(100),
link varchar(200),
estimated_costs INTEGER,
submit_date date,
status varchar(20),
decision_date date,
PRIMARY KEY (id)
) COMMENT='this is my first table';