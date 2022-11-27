import mysql.connector

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

class SqlUtils():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = env["DB_UAT_HOST"],
            database = env["DB_UAT_DATABASE"],
            user = env["DB_UAT_USER"],
            password = env["DB_UAT_PASSWORD"],
            buffered = True
        )
        self.cursor = self.connection.cursor()