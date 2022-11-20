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

    def get_products_id_list_by_category(self, category):
        sql = f"SELECT title FROM product WHERE category = '{category}';"
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        result = []
        for record in records:
            result.append(record[0])
        
        return records