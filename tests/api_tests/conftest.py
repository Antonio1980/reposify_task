import pytest
from base.logger import automation_logger, logger

title = "Test"
body = "Test Body"
user_id = 22


@pytest.fixture
@automation_logger(logger)
def post_id(api_client):
    _response = api_client.post_service.add_post(title, body, user_id)
    assert _response[0] is not None
    assert _response[1].status_code == 201
    assert _response[1].reason == "Created"

    return _response[0]["id"], user_id
