from api import dto
from api import db_provider
from typing import List,Optional
from sqlalchemy import exc, select,delete
from sqlalchemy.sql.selectable import Select
from sqlalchemy.sql.dml import Delete


def _blog_from_orm_object(
    blog_orm_object: db_provider.Blog,
) -> dto.Blog:
    return dto.Blog(
        id=dto.BlogID(blog_orm_object.id),
        title=blog_orm_object.title,
        content=blog_orm_object.content,
        ctime=blog_orm_object.ctime,
        mtime=blog_orm_object.mtime,
    )

def _get_blog_filter_query_select(
    blog_filter: Optional[dto.BlogFilter] = None,
) -> Select:
    _query = select(db_provider.Blog)
    if blog_filter is not None:
        if blog_filter.id is not None:
            _query = _query.where(
                db_provider.Blog.id == blog_filter.id
            )
        if blog_filter.title is not None:
            _query = _query.where(
                db_provider.Blog.title == blog_filter.title
            )
        if blog_filter.content is not None:
            _query = _query.where(
                db_provider.Blog.content == blog_filter.content
            )

    return _query

def _get_blog_filter_query_delete(
    blog_filter: Optional[dto.BlogFilter],
) -> Delete:
    _query = delete(db_provider.Blog)

    if blog_filter.id is not None:
        _query = _query.where(
            db_provider.Blog.id == blog_filter.id
        )
    if blog_filter.title is not None:
        _query = _query.where(
            db_provider.Blog.title == blog_filter.title
        )
    if blog_filter.content is not None:
        _query = _query.where(
            db_provider.Blog.content == blog_filter.content
        )
    return _query

async def find_many(db_session: db_provider.AsyncSessionLocal,blog_filter:Optional[dto.BlogFilter]=None)->List[dto.Blog]:
    find_query = _get_blog_filter_query_select(blog_filter=blog_filter)
    result = await db_session.execute(find_query)
    rows = result.all()
    blogs = [_blog_from_orm_object(row[0]) for row in rows]
    return blogs


async def insert_one(db_session:db_provider.AsyncSessionLocal,unsaved_blog:dto.UnsavedBlog)->dto.BlogID:
    blog = db_provider.Blog(
        title=unsaved_blog.title,
        content=unsaved_blog.content,
    )
    db_session.add(blog)
    await db_session.flush()
    return dto.BlogID(blog.id)


async def delete_one(db_session:db_provider.AsyncSessionLocal,blog_filter:dto.BlogFilter)->bool:
    delete_query = _get_blog_filter_query_delete(blog_filter=blog_filter)
    try:
        result = await db_session.execute(delete_query)
    except:
        return False
    return result.rowcount == 1