# Week 4 Part 1 (Deadline: 2022/11/09 23:59)

## Online Learning Material
* [Install MySQL on Windows](https://www.youtube.com/watch?v=WuBcTJnIuzo&t=723s) - [Document](https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html)
* [Install MySQL on Mac](https://www.youtube.com/watch?v=UcpHkYfWarM) - [Document](https://dev.mysql.com/doc/refman/5.7/en/osx-installation.html)
* [Udemy - Learn SQL / MySQL database basics](https://www.udemy.com/cart/subscribe/course/4538848/)

## Assignment 1: Using MySQL in Python

### Step 1: Setup MySQL server and database schema:
1. Install MySQL server in your computer (version 8.x is recommended).
2. Create a database named **assignment**.
3. Create a user table named **user**.
   * The user table should contain at least 3 columns: id, email, password. 
   * Column id should be a primary key and increase automatically.

### Step 2: Write a Python script to CRUD (Create, Read, Update, Delete) user data.
1. Connecting to MySQL server
2. Create a user data with email and password 
3. Get user id by selecting user data by email 
4. Update user password and select the user data to check if password has been changed.
5. Delete user by user id and select the user data to check if the user has been deleted.

Reminder: In this assignment, you should hand in an additional data file in SQL format by mysqldump tool.

## Assignment 2: SQL Statement Practice
1. Copy SQL queries from assignment3.sql and execute in MySQL.
2. Write a Python script to complete following questions:
- List out the score record of Chinese course for all students.
- List out the score record of English course for all students in descending order.
- List out all the student name.
- Get the average score of Chinese course.
- Get the minimum score of English course.
- Get the maximum score of Maths course.
- Get the number of student whose English score higher or equal to 60.
- List out the score record for a male student whose surname is '周'


## Assignment 3: Pagination in MySQL (Advance Optional)
Using pagination, long list of results are shown on multiple pages. The subset of results are shown in a single page with links to next and previous results.

To use pagination we will insert around 50 records. So copy SQL queries from "assignment3.sql" and execute in MySQL.

Try to complete the following program.
- pagination(): return the user first name and last name, according to current page number (current_page) and numbers of record per page (no_of_record).

```python
def pagination(current_page, no_of_record):
    # your code here   

print(pagination(1, 10))
# [{'first_name': 'Tyler', 'last_name': 'Spradley'}, 
# {'first_name': 'David', 'last_name': 'Desmarais'}, 
# {'first_name': 'Miles', 'last_name': 'Harlow'}, 
# {'first_name': 'Becca', 'last_name': 'Kingman'}, 
# {'first_name': 'Rotana', 'last_name': 'Greger'}, 
# {'first_name': 'Cinzia', 'last_name': 'Derige'}, 
# {'first_name': 'Karen', 'last_name': 'Boyce'}, 
# {'first_name': 'Don', 'last_name': 'Ringer'}, 
# {'first_name': 'Dane', 'last_name': 'Schuette'}, 
# {'first_name': 'Melessa', 'last_name': 'Steinhauer'}]

print(pagination(6, 9))
# Remain Five Record in the last page
# [{'first_name': 'Muhammed', 'last_name': 'Knotts'}, 
# {'first_name': 'Allyson', 'last_name': 'Kjelstad'}, 
# {'first_name': 'Tara', 'last_name': 'Wigmanich'}, 
# {'first_name': 'Patrick', 'last_name': 'Baillargeon'}, 
# {'first_name': 'Louise', 'last_name': 'Sublewski'}]

print(pagination(6, 10))
# [], No records found
```








