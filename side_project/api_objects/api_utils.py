import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from requests import Request

class ApiUtils():
    def __init__(self, session):
        self.basic_url = env["UAT_URL"]
        self.session = session

    def send_request(self, method, url, headers = None, body = None):
        LOGGER.info(f"[ACTION] Do {method} request")
        LOGGER.info(f"[DATA] Request url: {url}")
        LOGGER.info(f"[DATA] Request header: {headers}")
        LOGGER.info(f"[DATA] Request body: {body}")

        try:
            req = Request(method, url, headers = headers, json = body)
            prepped = req.prepare()
            response = self.session.send(prepped)
        except Request.exceptions.HTTPError as e:
            print(e)

        return response
