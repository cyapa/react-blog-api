from typing import List, Optional
from api import dto
from api.db_provider import AsyncSessionLocal
from api.model import comment_model


async def read_comments(db_session: AsyncSessionLocal,comment_filter:Optional[dto.CommentFilter]=None)->List[dto.Comment]:
    return await comment_model.find_many(db_session=db_session,comment_filter=comment_filter)

async def insert_one(db_session: AsyncSessionLocal,unsaved_comment:dto.UnsavedComment)->dto.CommentID:
    comment_id=  await comment_model.insert_one(db_session=db_session,unsaved_comment=unsaved_comment)
    await db_session.commit()
    return comment_id