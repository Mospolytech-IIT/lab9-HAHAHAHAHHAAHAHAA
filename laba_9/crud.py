"""crud"""
from sqlalchemy.orm import Session
from models import User, Post

#Создание нового пользователя
def create_user(db: Session, username: str, email: str, password: str):
    """a"""
    db_user = User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#получение всех пользователей
def get_users(db: Session):
    """a"""
    return db.query(User).all()

#создание поста
def create_post(db: Session, title: str, content: str, user_id: int):
    """a"""
    db_post = Post(title=title, content=content, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

#получение постОВ
def get_posts(db: Session):
    """a"""
    return db.query(Post).all()

#обновление почты
def update_user_email(db: Session, user_id: int, new_email: str):
    """a"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return user
    return None

#обновить содержание
def update_post_content(db: Session, post_id: int, new_content: str):
    """a"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        db.commit()
        db.refresh(post)
        return post
    return None

#удалить пост
def delete_post(db: Session, post_id: int):
    """a"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return post
    return None

#удаление пользователя
def delete_user(db: Session, user_id: int):
    """a"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None
