<<<<<<< HEAD
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .database import db

=======
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .favorite import Favorite
>>>>>>> origin/main

class User(db.Model):
    __tablename__ = "users"
    users_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
<<<<<<< HEAD

    def serialize(self):
        return {
            "id": self.users_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password
        }
=======
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates = "user")

    def serialize(self):
        return {
            "name" : self.first_name,
            "email" : self.email,
            "id" : self.users_id
        }
>>>>>>> origin/main
