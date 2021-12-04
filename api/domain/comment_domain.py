from typing import List, Optional
from api import dto
from api.db_provider import AsyncSessionLocal
from api.model import comment_model


async def read_comments(db_session: AsyncSessionLocal,comment_filter:Optional[dto.CommentFilter]=None)->List[dto.Comment]:
    return await comment_model.find_many(db_session=db_session,comment_filter=comment_filter)

    