from api.model import blog_model

async def read_blogs():
    return await blog_model.find_many()