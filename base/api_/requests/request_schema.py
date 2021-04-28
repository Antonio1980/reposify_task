from base.utils import Utils


class RequestSchema:
    def __init__(self):
        super(RequestSchema, self).__init__()
        self.inner = dict()

    def from_json(self, key=None):
        return Utils.to_json_dumps(self, key)
