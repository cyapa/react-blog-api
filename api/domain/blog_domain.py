from api.model import blog_model
from api.dto import Blog
from typing import List


async def read_blogs()->List[Blog]:
    return await blog_model.find_many()