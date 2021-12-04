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
        title="Title of the Blog post",
        description=("Title of the blog post. Example: First ever blog post")
    ),  
    is_deleted:Optional[bool] = Query(
        None,
        title="Indicates whether blog is deleted or not",
        description=("Blog is deleted or not. Example: 'true' if deleted, 'false' if not")
    ),
)->dto.BlogFilter:
    comment_filter = dto.BlogFilter()

    if id:
        comment_filter.id = id
    if title:
        comment_filter.title =title.strip()
    if is_deleted is not None:
        comment_filter.is_deleted=is_deleted
    return comment_filter

def unsaved_blog_from_payload(
    title: dto.NoneEmptyStringField = Body(
        None,
        title="Title of the blog",
        description=("Title of the blog. Example: 'Hello world'"),
    ),
    content: dto.NoneEmptyStringField = Body(
        None,
        title="Content of the blog",
        description=("Content of the blog. Example: 'This is mt first project'"),
    ),
)->dto.UnsavedBlog:
    return dto.UnsavedBlog(
        title=title.strip(),
        content=content.strip()
    )


def comment_filter_from_query_params(
    id:Optional[dto.CommentID] = Query(
        None,
        title="Id of the Comment",
        description=("Id of the comment. Example: 1")
    ),
    blog_id:Optional[dto.BlogID] = Query(
        None,
        title="Id of the Blog post",
        description=("Id of the blog post. Example: 2")
    ),  
    is_deleted:Optional[bool] = Query(
        None,
        title="Indicates whether comment is deleted or not",
        description=("Comment is deleted or not. Example: 'true' if deleted, 'false' if not")
    ),
)->dto.CommentFilter:
    comment_filter = dto.CommentFilter()

    if id:
        comment_filter.id = id
    if blog_id:
        comment_filter.blog_id =blog_id
    if is_deleted is not None:
        comment_filter.is_deleted=is_deleted
    return comment_filter

def unsaved_comment_from_payload(
    blog_id: dto.BlogID = Body(
        None,
        title="Id of the blog post",
        description=("Id of the blog post. Example: 1"),
    ),
    comment: dto.NoneEmptyStringField = Body(
        None,
        title="Content of the comment",
        description=("Content of the comment. Example: 'This is a comment'"),
    ),
)->dto.UnsavedComment:
    return dto.UnsavedComment(
        blog_id=blog_id,
        comment=comment.strip(),
    )