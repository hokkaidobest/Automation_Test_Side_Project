from sql_objects.action_utils import *

class MainPageSql(ActionUtils):
    def get_products_count_without_keyword(self):
        sql = "SELECT COUNT(*) FROM product;"
        self.cursor.execute(sql)
        records = self.cursor.fetchone()

        return records[0]

    def get_product_count_with_keyword(self, keyword):
        sql = f"SELECT COUNT(*) FROM product WHERE title LIKE '%{keyword}%';"
        self.cursor.execute(sql)
        records = self.cursor.fetchone()
        
        return records[0]