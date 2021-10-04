from api.domain import blog_domain
from fastapi import APIRouter



router = APIRouter()


@router.get("/blogs")
async def read_blogs():
    return await blog_domain.read_blogs()