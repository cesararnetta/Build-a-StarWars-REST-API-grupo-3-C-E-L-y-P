from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models import db




class User(db.Model):
    __tablename__ = "users"
    users_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    def serialize(self):
        return {
            "users_id": self.users_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }