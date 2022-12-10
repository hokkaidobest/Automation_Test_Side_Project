import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

import requests

class ApiUtils():
    def __init__(self, session):
        self.basic_url = "http://54.201.140.239/api/1.0/"
        self.session = session

    def get_resuest(self, url, headers = None, body = None):
        LOGGER.info("[ACTION] Do GET request")
        LOGGER.info(f"[DATA] Request url: {url}")
        LOGGER.info(f"[DATA] Request header: {headers}")
        LOGGER.info(f"[DATA] Request body: {body}")

        try:
            response = self.session.get(url, headers = headers, json = body)
        except requests.exceptions.HTTPError as e:
            print(e)

        return response

    def post_resuest(self, url, headers = None, body = None):
        LOGGER.info("[ACTION] Do POST request")
        LOGGER.info(f"[DATA] Request url: {url}")
        LOGGER.info(f"[DATA] Request header: {headers}")
        LOGGER.info(f"[DATA] Request body: {body}")

        try:
            response = self.session.post(url, headers = headers, json = body)
        except requests.exceptions.HTTPError as e:
            print(e)

        return response