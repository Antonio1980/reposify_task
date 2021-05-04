import json
import random
import string

from base.logger import automation_logger, logger


class Utils:
    @staticmethod
    @automation_logger(logger)
    def to_json_dumps(object_, key=None):
        if key:
            return json.dumps(json.loads(json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)
                                         ).pop(key))
        else:
            return json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)

    @staticmethod
    @automation_logger(logger)
    def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

