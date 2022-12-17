import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from sql_objects.sql_utils import *

class Order(SqlUtils):
    
    def get_order_by_number(self, number):
        sql = f"SELECT * FROM order_table WHERE number = '{number}';"
        self.cursor.execute(sql)
        
        row = self.cursor.fetchone()
        LOGGER.info(f"[DATA] SQL result: {row}")

        return row