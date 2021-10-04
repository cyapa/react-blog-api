from fastapi import FastAPI
from api.view import  blog_view

app = FastAPI(
    title="Blog API",
    description="This API serve's its client react-blog-cyapa",
    version="1.0"
)


app.include_router(blog_view.router)