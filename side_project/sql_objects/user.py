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
        
        return token

    def get_user_info_by_id(self, id):
        sql = f"SELECT provider, name, email, picture FROM user WHERE id = '{id}';"
        LOGGER.info(f"[DATA] SQL syntax: {sql}")

        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        LOGGER.info(f"[DATA] SQL result: {row}")

        return row