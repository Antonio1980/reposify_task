
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Location
 * Technologies
 * Recommended plugins
 * Requirements
 * Tests
 * Configuration
 * Maintainers

INTRODUCTION
------------

The "reposify_task"- simple automation test project (framework with tests).

LOCATION
---------

- SSH: git@github.com:Antonio1980/reposify_task.git
- HTTPS://github.com/Antonio1980/reposify_task.git

TECHNOLOGIES
------------

- pytest - advanced test framework.
- allure-pytest - reporting framework.
- requests - library to work with HTTP/S. 

RECOMMENDED PLUGINS
-------------------
- .gitignore - prevents redundant uploads.
- Docker - for docker integration.

REQUIREMENTS
------------

1. PyCharm IDEA installed.
2. Python 3.7 or 3.9 installed.
3. Python virtualenvironment installed into the project root as venv and activated.
4. Python interpreter configured.
5. Project requirements installed.
6. Project plugins installed.
7. Allure installed locally to: ~/Allure/bin/allure

TESTS
-----
* All examples are shown with collecting results files for allure report.
See allure documentation here: https://docs.qameta.io/allure/

1 Run all tests:
* $ pytest -v tests --alluredir=allure_/allure_results

2 Run tests as a package:
* $ pytest -v tests/processing_tests --alluredir=allure_/allure_results

3 Run specific test:
* $ pytest -v tests/processing_tests/actor_can_create_new_allocation_template_test.py  --alluredir=allure_/allure_results

4 Run per test group (regression group as example):
* $ pytest -v tests -m regression --alluredir=allure_/allure_results

5 Generate temporary allure report:
* $ allure serve allure_/allure_results
  
6 Generate report:
* $ allure generate allure_/allure_results -o allure_/allure_reports --clean
  
7 Open allure report:
* $ allure open allure_/allure_reports

8 Show pytest fixtures and execution plan:
* $ pytest --collect-only
* $ pytest --fixtures

9 Ignore Not Finished tests (cross project)
* $ pytest -v tests/ --ignore-glob='NF*.py'

10 Build docker image: 
* $ docker build . --rm -f "Dockerfile" -t [project_name]:latest 

11 Run tests under tox and pass environment variable:
* $ ENV=int tox -- -m [GROUP_NAME] --alluredir=../allure_/allure_results

12 Run tests under tox:
* $ tox -- -m [GROUP_NAME] --alluredir=../allure_/allure_results


* Test Groups:

1. regression - Short tests that should pass always.


CONFIGURATION
--------------

NOTE:
Be careful with allure and pytest plugins because of hell of conflicts, current valid plugin configuration is:
plugins: bdd-3.2.1, xdist-1.31.0, forked-1.1.3, allure-pytest-2.8.6

Tox documentation:
https://tox.readthedocs.io/en/latest/example/general.html

- Project base configuration stores in config.cfg that processes by config_definitions.py -> BaseConfig class.

- All imports specified in the requirements.txt file.

* To install all project dependencies run command:
* $ pip install -r requirements.txt

- pytest configuration specified in pytest.ini
currently, using: ignore::DeprecationWarning
will always run fixture run_time_counter

MAINTAINERS
-----------

* Anton Shipulin <antishipul@gmail.com> 
