from api.domain import blog_domain

async def read_blogs():
    return await blog_domain.read_blogs()