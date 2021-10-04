from pydantic import BaseModel
from datetime import datetime
from typing import NewType

BlogID = NewType("BlogID", int)

class Blog(BaseModel):
    id: BlogID
    title:str
    content:str
    ctime:datetime
    mtime:datetime