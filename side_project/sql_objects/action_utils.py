import mysql.connector

class ActionUtils():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "54.201.140.239",
            database = "stylish_backend",
            user = "readonly",
            password = "Automation_221017",
            buffered = True
        )
        self.cursor = self.connection.cursor()