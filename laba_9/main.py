"""main"""
from typing import List   #Добавить импорт List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, init_db
from schemas import UserOut, PostOut, UserCreate, PostCreate

app = FastAPI()

init_db()  #Инициализация базы данных при старте

@app.get("/") 
def kuku():
    """gau"""
    return "hello emae"

#получение сессии базы данных
def get_db():
    """get"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#cоздание юзера
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """c"""
    return crud.create_user(db, user.username, user.email, user.password)

#список всех пользователй
@app.get("/users", response_model=List[UserOut])  #list определен тут
def get_all_users(db: Session = Depends(get_db)):
    """gau"""
    users = crud.get_users(db)
    return users

#создать новый пост
@app.post("/posts", response_model=PostOut)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """cp"""
    return crud.create_post(db, post.title, post.content, post.user_id)

#список всех постов
@app.get("/posts", response_model=List[PostOut])
def get_all_posts(db: Session = Depends(get_db)):
    """gap"""
    posts = crud.get_posts(db)
    return posts

#обновить почту
@app.put("/users/{user_id}", response_model=UserOut)
def update_user_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    """uue"""
    user = crud.update_user_email(db, user_id, new_email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#обновить контент
@app.put("/posts/{post_id}", response_model=PostOut)
def update_post_content(post_id: int, new_content: str, db: Session = Depends(get_db)):
    """upc"""
    post = crud.update_post_content(db, post_id, new_content)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

#удалить пост
@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """dp"""
    post = crud.delete_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

#удаление пользователя с его постами
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """du"""
    user = crud.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User and their posts deleted successfully"}
