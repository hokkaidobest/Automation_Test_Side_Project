import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from sql_objects.sql_utils import *

class User(SqlUtils):

    def get_user_token_by_email(self, email):
        sql = f"SELECT access_token FROM user WHERE email = '{email}';"
        LOGGER.info(f"[DATA] SQL syntax: {sql}")
        
        self.cursor.execute(sql)
        token = self.cursor.fetchone()
        LOGGER.info(f"[DATA] SQL result: {token}")

        return token[0]

    def get_user_info_by_id(self, id):
        sql = f"SELECT provider, name, email, picture FROM user WHERE id = '{id}';"
        LOGGER.info(f"[DATA] SQL syntax: {sql}")

        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        desc = self.cursor.description
        result = {desc[0][0]: data[0], desc[1][0]: data[1], desc[2][0]: data[2], desc[3][0]: data[3]}
        LOGGER.info(f"[DATA] SQL result: {result}")

        return result