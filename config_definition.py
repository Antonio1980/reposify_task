import json
import os
import configparser
from allure_ import allure_dir
from base.enums import Environment

executor = {
    "buildName": "root project:- 'reposify tests'",
    "type": "Python 3.9, pytest 5.4.2",
    "IDE": "PyCharm 2019.2",
    "Builder": "tox 3.10.0"
}


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode="r", buffering=-1, closefd=True):
        parser.read(config)
        return parser


def save_allure_environment(env_dir, env_var):
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)
    with open(os.path.join(env_dir + "environment.properties"), "w+") as f:
        f.write(env_var)


def save_allure_executor(env_dir):
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)
    with open(os.path.join(env_dir + "executor.json"), "w+") as f:
        f.write(json.dumps(executor))


if "ENV" in os.environ.keys():
    environment = os.environ.__getitem__("ENV").lower()
else:
    os.environ["ENV"] = Environment.LOCAL.value
    environment = Environment.LOCAL.value


class BaseConfig:
    root_dir = os.path.abspath(os.path.dirname(__file__))

    config_file = os.path.join(root_dir, "config.cfg")
    parser = get_parser(config_file)

    ALLURE_DIR = os.path.join(allure_dir, parser.get("PATH", "allure_dir"))
    save_allure_environment(ALLURE_DIR, "env=" + os.environ.__getitem__("ENV").lower())

    save_allure_executor(ALLURE_DIR)

    API_URL = parser.get("URL's", "api_url")

