from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: str
    password: EmailStr

class UserResponse(BaseModel):
    id: int 
    email: EmailStr

    class Config:
        orm_mode = True
