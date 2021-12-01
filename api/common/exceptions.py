class APIException(Exception):
    pass


class BlogHttpException(APIException):
    pass


class BlogNotFound(APIException):
    pass


class BlogDeleteError(APIException):
    pass

class EmptyFilter(BlogHttpException):
    def __init__(self,)->None:
        super().__init__("Empty filters are not allowed")  


