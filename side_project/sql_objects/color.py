from sql_objects.sql_utils import *

class Color(SqlUtils):
    def get_color_name_by_code(self, code):
        sql = f"SELECT name FROM color WHERE code = '{code}';"
        self.cursor.execute(sql)
        records = self.cursor.fetchone()
        
        return records[0]