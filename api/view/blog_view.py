from api.domain import blog_domain
from fastapi import APIRouter,Depends
from api.db_provider import AsyncSessionLocal,get_db


router = APIRouter()


@router.get("/blogs")
async def read_blogs(db_session: AsyncSessionLocal = Depends(get_db)):
    return await blog_domain.read_blogs(db_session=db_session)