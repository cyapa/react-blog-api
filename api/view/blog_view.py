from api.domain import blog_domain
from fastapi import APIRouter,Depends
from api.db_provider import AsyncSessionLocal,get_db
from api import dto

router = APIRouter()


@router.get("/blogs")
async def read_blogs(db_session: AsyncSessionLocal = Depends(get_db)):
    return await blog_domain.read_blogs(db_session=db_session)


@router.post("/blog")
async def insert_one(unsaved_blog: dto.UnsavedBlog,db_session: AsyncSessionLocal = Depends(get_db)):
    return await blog_domain.insert_one(db_session=db_session,unsaved_blog=unsaved_blog)

@router.delete("/blog/{blog_id}")
async def delete_one(blog_id:dto.BlogID,db_session: AsyncSessionLocal = Depends(get_db)):
    blog_filter = dto.BlogFilter(
        id=blog_id
    )
    return await blog_domain.delete_one(db_session=db_session,blog_filter=blog_filter)