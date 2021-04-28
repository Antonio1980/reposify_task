import allure
import pytest
from base.constants import TEST_RESULT
from base.logger import automation_logger, logger

test_case = "ADD POST"


@allure.title(test_case)
@allure.testcase(test_case)
@allure.description("""
    Regression tests.
    1. Check that service responded on 'AddPost' request properly.
    2. Check that service response contains desired properties.
    """)
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression
class TestAddPost:

    @automation_logger(logger)
    def test_add_post_method_works(self, api_client):
        allure.step("Verify that response is not empty and status code is 201")
        _response = api_client.post_service.add_post("Test", "Test Post", 8888)

        assert _response[0] is not None
        assert _response[1].status_code == 201
        assert _response[1].reason == "Created"

        logger.info(TEST_RESULT.format(test_case, 1, "PASSED"))

    @automation_logger(logger)
    def test_attributes_in_add_post_method(self, api_client):
        allure.step("Verify response properties.")
        _response = api_client.post_service.add_post("Test", "Test Post", 8888)[0]

        assert isinstance(_response, dict)
        assert "userId" and "id" and "title" and "body" in _response.keys()
        assert isinstance(_response["userId"], int) and _response["userId"] == 8888
        assert isinstance(_response["id"], int) and _response["id"] == 101
        assert isinstance(_response["title"], str) and _response["title"] == "Test"
        assert isinstance(_response["body"], str) and _response["body"] == "Test Post"

        logger.info(TEST_RESULT.format(test_case, 2, "PASSED"))
