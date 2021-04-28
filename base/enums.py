from enum import Enum


class Environment(str, Enum):
    STAGING = "stg"
    INTEGRATION = "int"
    PRODUCTION = "prod"
    LOCAL = "local"
