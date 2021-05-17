from base.api_.requests.request_schema import RequestSchema
from base.constants import *
from base.logger import automation_logger, logger


class RequestBody(RequestSchema):

    def __init__(self):
        super(RequestBody, self).__init__()

    @automation_logger(logger)
    def add_post(self, title: str, body: str, user_id: int):
        self.inner[TITLE] = title
        self.inner[BODY] = body
        self.inner[USER_ID] = user_id
        body = self.from_json("inner")
        logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def update_post(self, title: str, body: str, user_id: int, id_: int):
        self.inner[ID] = id_
        self.inner[TITLE] = title
        self.inner[BODY] = body
        self.inner[USER_ID] = user_id
        body = self.from_json("inner")
        logger.info(REQUEST_BODY.format(body))
        return body
