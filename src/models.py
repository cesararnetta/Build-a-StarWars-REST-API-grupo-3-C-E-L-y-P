from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Boolean, Integer, DateTime, func, ForeignKey, Enum, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
db = SQLAlchemy()

gender_state = Enum('male', 'female', name='gender_enum')


class User(db.Model):
    __tablename__ = "users"
    users_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)


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

        }
    
    def serialize_with_connections(self):
        return {
            
        }


class Planet(db.Model):
    __tablename__ = "planets"
    planets_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    terrain: Mapped[str] = mapped_column(String(250), nullable=False)

    who_live_here: Mapped[int] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=False)

    def serialize(self):
        return {
            "name" : self.planets_id,
            "population" : self.population,
            "terrain" : self.terrain
        }
    
    def serialize_with_connections():
        return

class Favorite(db.Model):
    __tablename__ = "favorites"
    favorites_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    users_id: Mapped[int] = mapped_column(
        ForeignKey('users.users_id'), nullable=False)
    
    planets_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('planets.planets_id'), nullable=True)
    characters_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=True)
    __table_args__ = (
        CheckConstraint(
            '(characters_id IS NOT NULL AND planets_id IS NULL) OR (characters_id IS NULL AND planets_id IS NOT NULL)',
            name='check_one_favorite_type'
        ),
    )
