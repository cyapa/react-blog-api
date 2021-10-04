from pydantic import BaseModel
from datetime import datetime
from typing import NewType,Optional

BlogID = NewType("BlogID", int)

class Blog(BaseModel):
    id: BlogID
    title:str
    content:str
    ctime:datetime
    mtime:datetime

class BlogFilter(BaseModel):
    id: Optional[BlogID]
    title:Optional[str]
    content:Optional[str]
    ctime:datetime
    mtime:datetime