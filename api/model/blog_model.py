from api.dto import Blog
from typing import List


async def find_many()->List[Blog]:
    return [{"id":1,"title":"h"}]