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

    return await comment_domain.read_comments(db_session=db_session,comment_filter=comment_filter)