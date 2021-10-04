from api.model import blog_model
from api.dto import Blog
from typing import List,Optional
from api.db_provider import AsyncSessionLocal
from api import dto


async def read_blogs(db_session: AsyncSessionLocal,blog_filter:Optional[dto.BlogFilter]=None)->List[Blog]:
    return await blog_model.find_many(db_session=db_session,blog_filter=blog_filter)

    
async def insert_one(db_session: AsyncSessionLocal,unsaved_blog:dto.UnsavedBlog)->dto.BlogID:
    blog_id=  await blog_model.insert_one(db_session=db_session,unsaved_blog=unsaved_blog)
    await db_session.commit()
    return blog_id


async def delete_one(db_session: AsyncSessionLocal,blog_filter:dto.BlogFilter)->bool:
    is_deleted = await blog_model.delete_one(db_session=db_session,blog_filter=blog_filter)
    await db_session.commit()
    return is_deleted