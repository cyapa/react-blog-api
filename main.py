from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.view import blog_view

app = FastAPI(
    title="Blog API",
    description="This API serve's its client react-blog-cyapa",
    version="1.0"
)

app = FastAPI()

origins = [
    "https://react-blog-cyapa.herokuapp.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog_view.router)