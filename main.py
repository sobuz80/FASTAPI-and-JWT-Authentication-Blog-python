import uvicorn
from fastapi import FastAPI, Body, Depends

from app.model import PostSchema, UserSchema, UserLoginSchema, CommentSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT


posts = []
users = []

app = FastAPI()


##Login Check User
def check_user(data: UserLoginSchema):
    for user in users:
        if user.Email == data.Email and user.Password == data.Password:
            return True
    return False


# Get Blog Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return { "data": posts }

## Get Single Blog by ID Posts
@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

## Blog Post add
@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "Posts created successfully."
    }

## Delete Blog Post
@app.post("/posts/{id}", tags=["posts"])
def delete_post(id: int):
    global posts

    post_index = None
    for idx, post in enumerate(posts):
        if post["id"] == id:
            post_index = idx
            break

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    # Remove the post from the list of posts
    deleted_post = posts.pop(post_index)

    return {
        "data": deleted_post,
        "message": "Post deleted successfully."
    }


## Comments Blog for Post
@app.post("/comments/")
async def create_comment(comment: CommentSchema):
    return {"message": "Comment created successfully"}


## signup with jwt token
@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) 
    return signJWT(user.Email)


## user login  check use then respons jwt token
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.Email)
    return {
        "error": "Wrong login details!"
    }

## Get All user 
@app.get("/users", tags=["users"])
def get_users():
    return { "data": users }

## Get spacific Id by  users then delete 
@app.post("/users/{user_id}", tags=["users"])
def delete_user(user_id: int):
    global users

    user_index = None
    for idx, user in enumerate(users):
        if user.id == user_id:
            user_index = idx
            break

    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users.pop(user_index)

    return {
        "data": deleted_user,
        "message": "User deleted successfully."
    }
