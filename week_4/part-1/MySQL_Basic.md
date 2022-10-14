# Week 4 Part 1 (Deadline: 2022/11/09 23:59)

## Online Learning Material
* [Install MySQL on Windows](https://www.youtube.com/watch?v=WuBcTJnIuzo&t=723s) - [Document](https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html)
* [Install MySQL on Mac](https://www.youtube.com/watch?v=UcpHkYfWarM) - [Document](https://dev.mysql.com/doc/refman/5.7/en/osx-installation.html)
* [Udemy - Learn SQL / MySQL database basics](https://www.udemy.com/cart/subscribe/course/4538848/)

## Assignment 1: Using MySQL in Python

### Step 1: Setup MySQL server and database schema:
1. Install MySQL server in your computer (version 8.x is recommended).
2. Create a database named assignment.
3. Create a user table named **user**.
   * The user table should contain at least 3 columns: id, email, password. 
   * Column id should be a primary key and increase automatically.

### Step 2: Write a Python script to CRUD (Create, Read, Update, Delete) user data.
1. Connecting to MySQL server
2. Insert a user data  
3. Select user by email 
4. Update user password 
5. Delete user by user id

Reminder: In this assignment, you should hand in an additional data file in SQL format by mysqldump tool.

## Assignment 2: Using Mysql in Python - Join Table (Advance Optional)
1. Create 2 tables named **member** and **order**.

| member_id | name |
|-----------|------|
| 1         | Mary |
| 2         | Tom  |

| order_id | member_id | total_amount | no_of_items |
|----------|-----------|--------------|-------------|
| 1        | 1         | $500         | 2           |
| 2        | 1         | $1200        | 5           |
| 3        | 2         | $300         | 1           |
| 4        | 2         | $600         | 2           |
| 5        | 1         | $700         | 3           |







