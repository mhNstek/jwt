import uvicorn
from fastapi import FastAPI
from app.model import PostSchema
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT

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

@app.get("/posts", tags=["posts"])
def get_posts():
    return{"data": posts}


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

@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post added successfully"
    }

