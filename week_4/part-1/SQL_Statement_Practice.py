import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        database = "assignment",
        user = "root",
        password = "Aa513008",
        buffered = True
    )

    if connection.is_connected():

        cursor = connection.cursor()

        # Task 1 : List out the score record of Chinese course for all students.
        sql = "SELECT name, score FROM StudentScore WHERE course = 'Chinese';"
        cursor.execute(sql)
        records = cursor.fetchall()

        print("The student's Chinese course score record is: ")
        for record in records:
            print(record)

        # Task 2 : List out the score record of English course for all students in descending order.
        sql = "SELECT name, score FROM StudentScore WHERE course = 'English' ORDER BY score DESC;"
        cursor.execute(sql)
        records = cursor.fetchall()

        print("The student's English course score record is: ")
        for record in records:
            print(record)

        # Task 3 : List out all the student name.
        sql = "SELECT name FROM StudentScore GROUP BY name;"
        cursor.execute(sql)
        records = cursor.fetchall()

        list = []
        for record in records:
            list.append(record[0])

        print(f"The list of students' names is: {list}")

        # Task 4 : Get the average score of Chinese course.
        sql = "SELECT AVG(score) FROM StudentScore WHERE course = 'Chinese';"
        cursor.execute(sql)
        record = cursor.fetchone()

        print(f"The average Chinese score of students is: {round(record[0], 0)}")

        # Task 5 : Get the minimum score of English course.
        sql = "SELECT MIN(score) FROM StudentScore WHERE course = 'English';"
        cursor.execute(sql)
        record = cursor.fetchone()

        print(f"The lowest English score is: {record[0]}")

        # Task 6 : Get the maximum score of Maths course.
        sql = "SELECT MAX(score) FROM StudentScore WHERE course = 'Maths';"
        cursor.execute(sql)
        record = cursor.fetchone()

        print(f"The highest math score is: {record[0]}")

        # Task 7 : Get the number of student whose English score higher or equal to 60.
        sql = "SELECT name, score FROM StudentScore WHERE course = 'English' AND score >= 60;"
        cursor.execute(sql)
        records = cursor.fetchall()

        print("The student's English course score record is: ")
        for record in records:
            print(record)

        # Task 8 : List out the score record for a male student whose surname is '周'
        sql = "SELECT name, course, score FROM StudentScore WHERE name like '周%' AND sex = '男';"
        cursor.execute(sql)
        records = cursor.fetchall()

        print("The students whose names begin with the letter 周: ")
        for record in records:
            print(record)

except Error as e:

    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")