from typing import List, Optional
from api import dto
from api.db_provider import AsyncSessionLocal
from api.model import comment_model


async def find_comments(db_session: AsyncSessionLocal,comment_filter:Optional[dto.CommentFilter]=None)->List[dto.Comment]:
    return await comment_model.read_many(db_session=db_session,comment_filter=comment_filter)

async def insert_comment(db_session: AsyncSessionLocal,unsaved_comment:dto.UnsavedComment)->dto.CommentID:
    comment_id=  await comment_model.create_one(db_session=db_session,unsaved_comment=unsaved_comment)
    await db_session.commit()
    return comment_id

async def delete_comments(db_session: AsyncSessionLocal,comment_filter:dto.CommentFilter)->bool:
    is_deleted = await comment_model.delete_many(db_session=db_session,comment_filter=comment_filter)
    await db_session.commit()
    return is_deleted