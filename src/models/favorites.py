from typing import Optional
from sqlalchemy import Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from models import db


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