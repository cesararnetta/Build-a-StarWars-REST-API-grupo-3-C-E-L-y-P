from typing import Optional
from sqlalchemy import Boolean, Integer, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .planet import Planet
    from .character import Character


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

    def serialize(self):
        return {
            'favorites_id': self.favorites_id,
        }

    def serialize_with_relations(self):
        data = self.serialize()
        data['users_id'] = [user.serialize() for user in self.users_id]
        data['planets_id'] = [planet.serialize() for planet in self.planets_id]
        data['characters_id'] = [character.serialize()
                                 for character in self.characters_id]
        return data
