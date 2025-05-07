from sqlalchemy import String, Integer, ForeignKey
<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column
from .database import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .character import Character
=======
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .character import Character
    from .favorite import Favorite
>>>>>>> origin/main


class Planet(db.Model):
    __tablename__ = "planets"
    planets_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    terrain: Mapped[str] = mapped_column(String(250), nullable=False)
<<<<<<< HEAD
    who_live_here: Mapped[int] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=True)
=======
    # The characters live in planets
    who_live_here: Mapped[int] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=True)
    character: Mapped["Character"] = relationship(
        "Character", back_populates="planets", foreign_keys=[who_live_here])
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates = "planets")

    def serialize(self):
        return {
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "id": self.planets_id
        }
>>>>>>> origin/main
