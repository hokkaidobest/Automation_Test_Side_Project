import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

import pandas as pd

class GetTestData():
    def get_invalid_checkout_data(self):
        reader = pd.read_excel("test_data/Stylish-Test Case.xlsx", "Checkout with Invalid Value", dtype = str).fillna("")
        LOGGER.info(f"[DATA] Orginal checkout with invalid value's data: {reader}")
        reader["Receiver"] = reader["Receiver"].replace("101 chars", "x" * 101)
        reader["Email"] = reader["Email"].replace("51 chars", "x" * 43 + "@abc.com")
        reader["Address"] = reader["Address"].replace("256 chars", "x" * 256)
        LOGGER.info(f"[DATA] Format checkout with invalid value's data: {reader}")

        return reader.to_dict("records")


    def get_valid_checkout_data(self):
        reader = pd.read_excel("test_data/Stylish-Test Case.xlsx", "Checkout with Valid Value", dtype = str)
        LOGGER.info(f"[DATA] Orginal checkout with valid value's data: {reader}")
        
        return reader.to_dict("records")