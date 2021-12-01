class BlogException(Exception):
    pass


class BlogHttpException(BlogException):
    pass



class EmptyFilter(BlogHttpException):
    def __init__(self,)->None:
        super().__init__("Empty filters are not allowed")  
         