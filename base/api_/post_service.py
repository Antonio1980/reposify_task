import json
import requests
from json import JSONDecodeError
from base.api_.service_base import BaseApi
from base.api_.requests.requests_body import RequestBody
from base.constants import RESPONSE_TEXT
from base.logger import automation_logger, logger


class PostService(BaseApi):

    def __init__(self):
        super(PostService, self).__init__()

    @automation_logger(logger)
    def get_posts(self):
        uri = self.api_url + "posts"
        try:
            _response = requests.get(url=uri, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.error(F"{e.__class__.__name__} get_posts failed with error: {e}")
            raise e

    @automation_logger(logger)
    def add_post(self, title, body, user_id):
        uri = self.api_url + "posts"
        payload = RequestBody().add_post(title, body, user_id)
        try:
            logger.info(F"API Service URL is POST - {uri}")
            _response = requests.post(uri, data=payload, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.error(F"{e.__class__.__name__} add_post failed with error: {e}")
            raise e

    @automation_logger(logger)
    def update_post(self, title, body, id_, user_id):
        uri = self.api_url + "posts" + "/" + str(user_id)
        payload = RequestBody().update_post(title, body, user_id, id_)
        try:
            logger.info(F"API Service URL is POST - {uri}")
            _response = requests.put(uri, data=payload, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.error(F"{e.__class__.__name__} update_post failed with error: {e}")
            raise e
