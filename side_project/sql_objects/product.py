import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from sql_objects.sql_utils import *

class Product(SqlUtils):
    def get_product_count_with_keyword(self, keyword):
        sql = f"SELECT COUNT(*) FROM product WHERE title LIKE '%{keyword}%';"
        self.cursor.execute(sql)
        records = self.cursor.fetchone()
        
        return records[0]

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
        # Get selected data
        rows = self.cursor.fetchall()
        # Get column name
        desc = self.cursor.description
        
        result = []
        for row in rows:
            result.append({
                desc[0][0]: row[0], # id
                desc[1][0]: row[1], # category
                desc[2][0]: row[2], # title
                desc[3][0]: row[3], # description
                desc[4][0]: row[4], # price
                desc[5][0]: row[5], # texture
                desc[6][0]: row[6], # wash
                desc[7][0]: row[7], # palce
                desc[8][0]: row[8], # note
                desc[9][0]: row[9], # story
                desc[10][0]: row[10] # main_page
            })
        LOGGER.info(f"[DATA] SQL result: {result}")
        
        return result

    def get_product_by_id(self, id):
        sql = f"SELECT * FROM product WHERE id = '{id}';"
        self.cursor.execute(sql)
        
        # Get selected data
        row = self.cursor.fetchone()
        
        # Get column name
        desc = self.cursor.description
        
        return {
                desc[0][0]: row[0], # id
                desc[1][0]: row[1], # category
                desc[2][0]: row[2], # title
                desc[3][0]: row[3], # description
                desc[4][0]: row[4], # price
                desc[5][0]: row[5], # texture
                desc[6][0]: row[6], # wash
                desc[7][0]: row[7], # palce
                desc[8][0]: row[8], # note
                desc[9][0]: row[9], # story
                desc[10][0]: row[10] # main_page
        }