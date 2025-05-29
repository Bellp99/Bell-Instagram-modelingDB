from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, Enum
from typing import List 
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    firstname: Mapped[str] = mapped_column(String(120),nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    children: Mapped[List["Comments"]] = relationship() 

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }
    

class Comments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    
    
class Posts(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    #type: Mapped[Enum] = mapped_column(Enum(), nullable=False)
    url: Mapped[str] = mapped_column(String(120), nullable=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column()
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

