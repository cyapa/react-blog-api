from api import dto
from fastapi import Query,Body
from typing import Optional


def blog_filter_from_query_params(
    id:Optional[dto.BlogID] = Query(
        None,
        title="Id of the Blog post",
        description=("Id of the blog post. Example: 1")
    ),
    title:Optional[dto.NoneEmptyStringField] = Query(
        None,
        title="title of the Blog post",
        description=("Title of the blog post. Example: First ever blog post")
    ),  
    is_deleted:Optional[bool] = Query(
        None,
        title="Indicates whether blog is deleted or not",
        description=("Blog is deleted or not. Example: 'true' if deleted, 'false' if not")
    ),
)->dto.BlogFilter:

    blog_filter = dto.BlogFilter()

    if id:
        blog_filter.id = id
    if title:
        blog_filter.title =title
    if is_deleted is not None:
        blog_filter.is_deleted=is_deleted
    return blog_filter