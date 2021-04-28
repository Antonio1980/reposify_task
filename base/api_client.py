from base.api_.post_service import PostService


class ApiClient:
    def __init__(self):
        self.post_service = PostService()
