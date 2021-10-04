from fastapi import FastAPI
from api import  blog_view
app = FastAPI()





@app.get("/blogs")
async def get_blogs():
    return await blog_view.read_blogs()