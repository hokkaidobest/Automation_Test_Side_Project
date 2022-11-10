import mysql.connector
from mysql.connector import Error

from faker import Faker

try:
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        database = "assignment",
        user = "root",
        password = "Aa513008",
        buffered = True
    )

    # Step 1: Connecting to MySQL server
    if connection.is_connected():

        cursor = connection.cursor()
        
        # User data
        fake = Faker()

        email = fake.email()
        password = fake.password()
        new_password = fake.password()

        # Step 2 : Create a user data with email and password
        insert_sql = f"INSERT INTO user (email, password) VALUES ('{email}', '{password}');"
        cursor.execute(insert_sql)
        connection.commit()

        # Step 3 : Get user id by selecting user data by email
        select_sql = f"SELECT * FROM user WHERE email = '{email}';"
        cursor.execute(select_sql)
        records = cursor.fetchall()
        print(f"The selected data total count is: {cursor.rowcount}.")

        for record in records:
            print(f"The selected data's id is: {record[0]}.")

        # Step 4 : Update user password and select the user data to check if password has been changed.
        update_sql = f"UPDATE user SET password = '{new_password}' WHERE email = '{email}';"
        cursor.execute(update_sql)
        connection.commit()

        confirm_update_password_sql = f"SELECT password FROM user WHERE email = '{email}';"
        cursor.execute(confirm_update_password_sql)
        assert cursor.fetchone()[0] == new_password, "Updated password failed."

        # Step 5 : Delete user by user id and select the user data to check if the user has been deleted.
        delete_sql = f"DELETE FROM user WHERE id = '{record[0]}';"
        cursor.execute(delete_sql)
        connection.commit()

        cursor.execute(select_sql)
        assert cursor.fetchone() == None, "Deleted user failed."

except Error as e:

    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")