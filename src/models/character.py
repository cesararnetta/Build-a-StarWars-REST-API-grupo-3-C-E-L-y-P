from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func, Enum
<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column
from .database import db

gender_state = Enum('male', 'female', name='gender_enum')


=======
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .planet import Planet
    from .favorite import Favorite

# For use a selective value, this case, male y female, we the imported method Enum, from my sqlalchemy
gender_state = Enum('male', 'female', name='gender_enum')

>>>>>>> origin/main
class Character(db.Model):
    __tablename__ = "characters"
    characters_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(250), nullable=False)
    gender: Mapped[str] = mapped_column(gender_state, nullable=False)
<<<<<<< HEAD
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
=======
    # That's how we created an automated date. For Create and update datetime record.
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    update_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now())
    planets: Mapped[List["Planet"]] = relationship("Planet", back_populates = "character")
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates = "character")
    
    def serialize(self):
        return {
            "characters_id": self.characters_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

>>>>>>> origin/main
