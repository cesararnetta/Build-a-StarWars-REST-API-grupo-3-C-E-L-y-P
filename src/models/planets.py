from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models import db


class Planet(db.Model):
    __tablename__ = "planets"
    planets_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    terrain: Mapped[str] = mapped_column(String(250), nullable=False)

    who_live_here: Mapped[int] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=True)
    
    @classmethod
    def get_all_planets(cls):
        return cls.query.all()

    def serialize(self):
        return {
            "name" : self.planets_id,
            "population" : self.population,
            "terrain" : self.terrain
        }
    
    def serialize_with_relations():
        return