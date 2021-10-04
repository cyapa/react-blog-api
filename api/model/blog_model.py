from api import dto
from api import db_provider
from typing import List,Optional
from sqlalchemy import exc, select
from sqlalchemy.sql.selectable import Select

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

def _get_blog_filter_query(
    blog_filter: Optional[dto.BlogFilter] = None,
) -> Select:
    find_query = select(db_provider.Blog)
    if blog_filter is not None:
        if blog_filter.id is not None:
            find_query = find_query.where(
                db_provider.Blog.id == blog_filter.id
            )
        if blog_filter.title is not None:
            find_query = find_query.where(
                db_provider.Blog.title == blog_filter.title
            )
        if blog_filter.content is not None:
            find_query = find_query.where(
                db_provider.Blog.content == blog_filter.content
            )

    return find_query


async def find_many(db_session: db_provider.AsyncSessionLocal,blog_filter:Optional[dto.BlogFilter]=None)->List[dto.Blog]:
    find_query = _get_blog_filter_query(blog_filter=blog_filter)
    result = await db_session.execute(find_query)
    rows = result.all()
    blogs = [_blog_from_orm_object(row[0]) for row in rows]
    return blogs