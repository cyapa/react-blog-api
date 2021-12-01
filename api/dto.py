from datetime import datetime
from typing import NewType, Optional

from pydantic import BaseModel,constr

BlogID = NewType("BlogID", int)
NoneEmptyStringField =constr(strip_whitespace=True,min_length=1)

class ErrorResponse(BaseModel):
    errors:NoneEmptyStringField


class Blog(BaseModel):
    id: BlogID
    title:NoneEmptyStringField
    content:NoneEmptyStringField
    ctime:datetime
    mtime:datetime

class UnsavedBlog(BaseModel):
    title:NoneEmptyStringField
    content:NoneEmptyStringField

class BlogFilter(BaseModel):
    id: Optional[BlogID]
    title:Optional[NoneEmptyStringField]
    is_deleted: Optional[bool]