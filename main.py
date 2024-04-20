import uvicorn
from fastapi import FastAPI
from app.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "Afghanistan",
        "text": "Land of jingle trucks"
    },
    {
        "id": 2,
        "title": "Albania",
        "text": "Land of dordolecs"
    },
    {
        "id": 3,
        "title": "Algeria",
        "text": "Land of ergs"
    },
]

users = []

app = FastAPI()

#Test
@app.get("/", tags=["test"])
def greet():
    return{"hello": "world"}

#Get all posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return{"data": "posts"}


#Get one post
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "Posts with this ID does not exist!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
