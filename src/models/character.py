from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func, Enum
from sqlalchemy.orm import Mapped, mapped_column
from .database import db

gender_state = Enum('male', 'female', name='gender_enum')


class Character(db.Model):
    __tablename__ = "characters"
    characters_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(250), nullable=False)
    gender: Mapped[str] = mapped_column(gender_state, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    update_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now())


def serialize(self):
    return {
        "id": self.characters_id,
        "name": self.name,
        "birth_year": self.birth_year,
        "gender": self.gender,
    }
