import allure
import pytest
from base.constants import TEST_RESULT
from base.logger import automation_logger, logger

test_case = "UPDATE POST"


@allure.title(test_case)
@allure.testcase(test_case)
@allure.description("""
    Regression tests.
    1. Check that service responded on 'UpdatePost' request properly.
    2. Check that service response contains desired properties.
    """)
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression
class TestUpdatePost:

    @automation_logger(logger)
    def test_update_post_method_works(self, api_client, post_id):
        allure.step("Verify that response is not empty and status code is 200")
        _response = api_client.post_service.update_post("TestTest", "Post Test Post", post_id[0], post_id[1])

        assert _response[0] is not None
        assert _response[1].status_code == 200
        assert _response[1].reason == "OK"

        logger.info(TEST_RESULT.format(test_case, 1, "PASSED"))

    @automation_logger(logger)
    def test_attributes_in_update_post_method(self, api_client, post_id):
        allure.step("Verify response properties.")
        _response = api_client.post_service.update_post("TestTest", "Post Test Post", post_id[0], post_id[1])[0]

        assert isinstance(_response, dict)
        assert "userId" and "id" and "title" and "body" in _response.keys()
        assert isinstance(_response["userId"], int) and _response["userId"] == post_id[1]
        assert isinstance(_response["id"], int) and _response["id"] == post_id[1]
        assert isinstance(_response["title"], str) and _response["title"] == "TestTest"
        assert isinstance(_response["body"], str) and _response["body"] == "Post Test Post"

        logger.info(TEST_RESULT.format(test_case, 2, "PASSED"))
