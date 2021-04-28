import allure
import pytest
from base.constants import TEST_RESULT
from base.logger import automation_logger, logger

test_case = "GET POSTS"


@allure.title(test_case)
@allure.testcase(test_case)
@allure.description("""
    Regression tests.
    1. Check that service responded on 'GetPosts' request properly.
    2. Check that service response contains desired properties.
    """)
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression
class TestGetPosts:

    @automation_logger(logger)
    def test_get_posts_method_works(self, api_client):
        allure.step("Verify that response is not empty and status code is 200")
        _response = api_client.post_service.get_posts()

        assert _response[0] is not None
        assert _response[1].status_code == 200
        assert _response[1].reason == "OK"

        logger.info(TEST_RESULT.format(test_case, 1, "PASSED"))

    @automation_logger(logger)
    def test_attributes_in_get_posts_method(self, api_client):
        allure.step("Verify response properties.")
        _response = api_client.post_service.get_posts()[0]

        assert isinstance(_response, list)
        assert len(_response) > 0
        assert "userId" and "id" and "title" and "body" in _response[0].keys()
        assert isinstance(_response[0]["userId"], int)
        assert isinstance(_response[0]["id"], int)
        assert isinstance(_response[0]["title"], str)
        assert isinstance(_response[0]["body"], str)

        logger.info(TEST_RESULT.format(test_case, 2, "PASSED"))
