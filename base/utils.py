import json
import random
import string

from base.logger import automation_logger, logger


class Utils:
    @staticmethod
    @automation_logger(logger)
    def to_json_dumps(object_, key=None):
        """
        Converts a class object to JSON object.
        :param object_: a class instance.
        :param key: key/value pair to delete (optional).
        :return: a JSON object (python dictionary).
        """
        if key:
            return json.dumps(json.loads(json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)
                                         ).pop(key))
        else:
            return json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)

    @staticmethod
    @automation_logger(logger)
    def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
        """
        Generates random string with chars and digits.
        :param size: string length expected (default is 8).
        :param chars: string characters consistency.
        :return: random string.
        """
        return ''.join(random.choice(chars) for _ in range(size))

