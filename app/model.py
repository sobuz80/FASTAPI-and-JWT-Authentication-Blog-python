from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }


class CommentSchema(BaseModel):
    id: int = Field(default=None)
    post_id: int
    content: str

    class Config:
        schema_extra = {
            "example": {
                "post_id": 1,
                "content": "This is a great post!"
            }
        }


class UserSchema(BaseModel):
    FirstName: str = Field(...)
    LastName: str = Field(...)
    Email: EmailStr = Field(...)
    UserName: str = Field(...)
    Password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "FirstName": "Md.Mizanur Rahaman2 ",
                "LastName": "(Sobuz)",
                "Email": "sobuz80@gmail.com",
                "UserName": "chowdhury",
                "Password": "12345678"
            }
        }

class UserLoginSchema(BaseModel):
    Email: EmailStr = Field(...)
    Password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Email": "sobuz80@gmail.com",
                "Password": "12345678"
            }
        }
