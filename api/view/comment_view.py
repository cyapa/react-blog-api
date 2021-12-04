from typing import List

from fastapi import APIRouter, Depends,responses,status

from api import dto
from api.db_provider import AsyncSessionLocal, get_db
from api.domain import comment_domain
from api.view import dependencies
from api.common import exceptions

router = APIRouter()


@router.get("/comments",
    response_model=List[dto.Comment],
    status_code=status.HTTP_200_OK,
    response_model_exclude_unset=True,
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":dto.ErrorResponse,
            "description":"Invalid filter"
        },
        status.HTTP_404_NOT_FOUND:{
            "model":dto.ErrorResponse,
            "description":"Comments not found"
        }
    }
)
async def read_comments(
    db_session: AsyncSessionLocal = Depends(get_db),
    comment_filter:dto.CommentFilter = Depends(dependencies.comment_filter_from_query_params)
    )->List[dto.Comment]:

    if not comment_filter.dict(exclude_none=True):
        raise exceptions.EmptyFilter()

    return await comment_domain.find_comments(db_session=db_session,comment_filter=comment_filter)


@router.post("/comment",
    response_model=dto.CreateResult,
    status_code=status.HTTP_201_CREATED,
)
async def insert_one(
    unsaved_comment: dto.UnsavedComment=Depends(dependencies.unsaved_comment_from_payload),
    db_session: AsyncSessionLocal = Depends(get_db))->dto.CreateResult:
    comment_id = await comment_domain.insert_comment(db_session=db_session,unsaved_comment=unsaved_comment)
    return dto.CreateResult(id=comment_id)


@router.delete("/comments",
    response_model=dto.DeleteResult,
    status_code=status.HTTP_200_OK,
)
async def delete_comments(
    comment_filter:dto.CommentFilter = Depends(dependencies.comment_filter_from_query_params),
    db_session: AsyncSessionLocal = Depends(get_db))->bool:
    is_deleted = await comment_domain.delete_comments(db_session=db_session,comment_filter=comment_filter)
    if not is_deleted:
         return dto.DeleteResult(message="Comments not deleted")
    return dto.DeleteResult(message="Comments deleted successfully")