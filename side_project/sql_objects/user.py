from sql_objects.sql_utils import *

class User(SqlUtils):

    def get_user_token_by_email(self, email):
        sql = f"SELECT access_token FROM user WHERE email = '{email}';"
        self.cursor.execute(sql)
        user = self.cursor.fetchone()

        return user[0]