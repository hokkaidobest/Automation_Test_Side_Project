import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

import requests

class ApiUtils():
    def __init__(self, session):
        self.basic_url = env["UAT_URL"]
        self.session = session

    def get_request(self, url, headers = None, body = None):
        LOGGER.info("[ACTION] Do GET request")
        LOGGER.info(f"[DATA] Request url: {url}")
        LOGGER.info(f"[DATA] Request header: {headers}")
        LOGGER.info(f"[DATA] Request body: {body}")

        try:
            response = self.session.get(url, headers = headers, json = body)
        except requests.exceptions.HTTPError as e:
            print(e)

        return response

    def post_request(self, url, headers = None, body = None):
        LOGGER.info("[ACTION] Do POST request")
        LOGGER.info(f"[DATA] Request url: {url}")
        LOGGER.info(f"[DATA] Request header: {headers}")
        LOGGER.info(f"[DATA] Request body: {body}")

        try:
            response = self.session.post(url, headers = headers, json = body)
        except requests.exceptions.HTTPError as e:
            print(e)

        return response