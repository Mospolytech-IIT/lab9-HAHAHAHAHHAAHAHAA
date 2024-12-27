"""schemas"""
from pydantic import BaseModel


#модель для вывода пользователя
class UserOut(BaseModel):
    """USerOut"""
    id: int
    username: str
    email: str

    class Config:
        """config"""
        orm_mode = True

#модель для вывода поста
class PostOut(BaseModel):
    """PostOut"""
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        """config"""
        orm_mode = True

#модель для создания пользователя
class UserCreate(BaseModel):
    """UserCreate"""
    username: str
    email: str
    password: str

#модель для создания поста
class PostCreate(BaseModel):
    """PostCreate"""
    title: str
    content: str
    user_id: int
