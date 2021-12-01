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
)->dto.BlogFilter:

    blog_filter = dto.BlogFilter()

    if id:
        blog_filter.id = id
    if title:
        blog_filter.title =title
    return blog_filter