import uvicorn
from fastapi import FastAPI, Body
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


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid credentials"
        }
