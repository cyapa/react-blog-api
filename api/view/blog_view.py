from typing import List

from fastapi import APIRouter, Depends,responses,status

from api import dto
from api.db_provider import AsyncSessionLocal, get_db
from api.domain import blog_domain
from api.view import dependencies
from api.common import exceptions
router = APIRouter()


@router.get("/blogs",
    response_model=List[dto.Blog],
    status_code=status.HTTP_200_OK,
    response_model_exclude_unset=True,
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":dto.ErrorResponse,
            "description":"Invalid filter"
        },
        status.HTTP_404_NOT_FOUND:{
            "model":dto.ErrorResponse,
            "description":"Blogs not found"
        }
    }
)
async def read_blogs(
    db_session: AsyncSessionLocal = Depends(get_db),
    blog_filter:dto.BlogFilter = Depends(dependencies.blog_filter_from_query_params)
    )->List[dto.Blog]:

    if not blog_filter.dict(exclude_none=True):
        raise exceptions.EmptyFilter()

    return await blog_domain.read_blogs(db_session=db_session,blog_filter=blog_filter)


@router.post("/blog",
    response_model=dto.CreateResult,
    status_code=status.HTTP_201_CREATED,
)
async def insert_one(unsaved_blog: dto.UnsavedBlog=Depends(dependencies.unsaved_blog_from_payload),db_session: AsyncSessionLocal = Depends(get_db))->dto.CreateResult:
    blog_id = await blog_domain.insert_one(db_session=db_session,unsaved_blog=unsaved_blog)
    return dto.CreateResult(id=blog_id)

@router.delete("/blog/{blog_id}",
    response_model=dto.DeleteResult,
    status_code=status.HTTP_200_OK,
)
async def delete_one(blog_id:dto.BlogID,db_session: AsyncSessionLocal = Depends(get_db))->bool:
    blog_filter = dto.BlogFilter(
        id=blog_id
    )
    await blog_domain.delete_one(db_session=db_session,blog_filter=blog_filter)
    return dto.DeleteResult(message="Blog deleted successfully")