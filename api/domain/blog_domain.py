from api.model import blog_model
from api.dto import Blog
from typing import List,Optional
from api.db_provider import AsyncSessionLocal
from api import dto


async def read_blogs(db_session: AsyncSessionLocal,blog_filter:Optional[dto.BlogFilter]=None)->List[Blog]:
    return await blog_model.find_many(db_session=db_session,blog_filter=blog_filter)