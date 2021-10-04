from api.domain import blog_domain
from fastapi import APIRouter,Depends
from api.db_provider import AsyncSessionLocal,get_db
from api import dto

router = APIRouter()


@router.get("/blogs")
async def read_blogs(db_session: AsyncSessionLocal = Depends(get_db)):
    return await blog_domain.read_blogs(db_session=db_session)


@router.post("/blog")
async def create_blog(unsaved_blog: dto.UnsavedBlog,db_session: AsyncSessionLocal = Depends(get_db)):
    return await blog_domain.create_blog(db_session=db_session,unsaved_blog=unsaved_blog)