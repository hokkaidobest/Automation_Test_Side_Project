import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from sql_objects.sql_utils import *

class Product(SqlUtils):
    def get_product_count_with_keyword(self, keyword):
        sql = f"SELECT COUNT(*) FROM product WHERE title LIKE '%{keyword}%';"
        self.cursor.execute(sql)
        records = self.cursor.fetchone()

        return records

    def get_products_count_with_empty_keyword(self):
        sql = "SELECT COUNT(*) FROM product;"
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

    def get_a_product_randomly(self):
        sql = "SELECT id, title FROM product ORDER BY RAND() LIMIT 1;"
        self.cursor.execute(sql)
        
        # Get selected data
        row = self.cursor.fetchone()
        
        # Get column name
        desc = self.cursor.description
        
        return {desc[0][0]: row[0], desc[1][0]: row[1]}

    def get_product_by_category(self, category):
        
        if category == "all":
            sql = "SELECT * FROM product;"
        else:
            sql = f"SELECT * FROM product WHERE category = '{category}';"
        LOGGER.info(f"[DATA] SQL syntax is: {sql}")

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        LOGGER.info(f"[DATA] SQL result: {rows}")
        
        return rows

    def get_product_by_id(self, id):
        sql = f"SELECT * FROM product WHERE id = '{id}';"
        self.cursor.execute(sql)
        
        row = self.cursor.fetchone()
        LOGGER.info(f"[DATA] SQL result: {row}")

        return row

    def get_product_for_checkout(self):
        
        product = {
            "id": 201807201824,
            "name": "前開衩扭結洋裝",
            "qty": 1,
            "price": 799,
            "size": "S",
            "image": "http://54.201.140.239/assets/201807201824/0.jpg",
            "color": {
              "code": "FFFFFF",
              "name": "白色"
            }
        }
        LOGGER.info(f"[DATA] product: {product}")
        
        return product