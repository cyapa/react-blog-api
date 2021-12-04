from typing import List, Optional

from sqlalchemy import delete, exc, select
from sqlalchemy.sql.dml import Delete
from sqlalchemy.sql.selectable import Select
from api.common import exceptions
from api import db_provider, dto


def _comment_from_orm_object(
    comment_orm_object: db_provider.Comment,
) -> dto.Comment:
    return dto.Comment(
        id=dto.CommentID(comment_orm_object.id),
        comment=comment_orm_object.comment,
        ctime=comment_orm_object.ctime,
        mtime=comment_orm_object.mtime,
    )

def _get_comment_filter_query_select(
    comment_filter: Optional[dto.CommentFilter] = None,
) -> Select:
    _query = select(db_provider.Comment)
    if comment_filter is not None:
        if comment_filter.id is not None:
            _query = _query.where(
                db_provider.Comment.id == comment_filter.id
            )
        if comment_filter.blog_id is not None:
            _query = _query.where(
                db_provider.Comment.blog_id == comment_filter.blog_id
            )
    return _query


def _get_comment_filter_query_delete(comment_filter: dto.CommentFilter) -> Delete:
    _query = delete(db_provider.Comment)

    if comment_filter.id is not None:
        _query = _query.where(
            db_provider.Comment.id == comment_filter.id
        )
    if comment_filter.blog_id is not None:
        _query = _query.where(
            db_provider.Comment.blog_id == comment_filter.blog_id
        )
    if comment_filter.is_deleted is not None:
        _query = _query.where(
            db_provider.Comment.is_deleted == comment_filter.is_deleted
        )
    return _query


async def read_many(db_session: db_provider.AsyncSessionLocal,comment_filter:Optional[dto.CommentFilter]=None)->List[dto.Comment]:
    find_query = _get_comment_filter_query_select(comment_filter=comment_filter)
    result = await db_session.execute(find_query)
    rows = result.all()
    comments = [_comment_from_orm_object(row[0]) for row in rows]
    return comments


async def create_one(db_session:db_provider.AsyncSessionLocal,unsaved_comment:dto.UnsavedComment)->dto.CommentID:
    new_comment = db_provider.Comment(
        blog_id=unsaved_comment.blog_id,
        comment=unsaved_comment.comment,
    )
    db_session.add(new_comment)
    await db_session.flush()
    return dto.CommentID(new_comment.id)


async def delete_many(db_session:db_provider.AsyncSessionLocal,comment_filter:dto.CommentFilter)->bool:
    delete_query = _get_comment_filter_query_delete(comment_filter=comment_filter)
    try:
        result = await db_session.execute(delete_query)
    except:
        raise exceptions.CommentDeleteError(f"Error deleting the Comments with filter {comment_filter.dict(exclude_none=True)} ")
    return result.rowcount>0