from typing import List

from fastapi import APIRouter, Depends

from api import dto
from api.db_provider import AsyncSessionLocal, get_db
from api.domain import blog_domain
from api.view import dependencies
router = APIRouter()


@router.get("/blogs")
async def read_blogs(
    db_session: AsyncSessionLocal = Depends(get_db),
    blog_filter:dto.BlogFilter = Depends(dependencies.blog_filter_from_query_params)
    )->List[dto.Blog]:
    print(blog_filter)
    return await blog_domain.read_blogs(db_session=db_session,blog_filter=blog_filter)


@router.post("/blog")
async def insert_one(unsaved_blog: dto.UnsavedBlog,db_session: AsyncSessionLocal = Depends(get_db))->dto.BlogID:
    return await blog_domain.insert_one(db_session=db_session,unsaved_blog=unsaved_blog)

@router.delete("/blog/{blog_id}")
async def delete_one(blog_id:dto.BlogID,db_session: AsyncSessionLocal = Depends(get_db))->bool:
    blog_filter = dto.BlogFilter(
        id=blog_id
    )
    return await blog_domain.delete_one(db_session=db_session,blog_filter=blog_filter)