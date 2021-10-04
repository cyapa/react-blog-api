from fastapi import FastAPI
from api.view import  blog_view

app = FastAPI(
    title="job_entry",
    description="Lionbridge AI Job Management Service",
    version="1.0"
)


app.include_router(blog_view.router)