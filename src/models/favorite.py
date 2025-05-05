from typing import Optional
from sqlalchemy import Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .planet import Planet
    from .character import Character


class Favorite(db.Model):
    __tablename__ = "favorites"
    favorites_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # The user can save as favorite planets and characteres. In order to get a good record the user only can save 1 planet or 1 characteer
    users_id: Mapped[int] = mapped_column(
        ForeignKey('users.users_id'), nullable=False)
    # The typing Optional allows you to put another type of data instead of int. We switch nullable to true in order
    # to accept the argument value null or not after these lines
    planets_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('planets.planets_id'), nullable=True)
    characters_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('characters.characters_id'), nullable=True)
    __table_args__ = (
        # In these lines we define where character and planet are null or not, in order to choose one option
        CheckConstraint(
            '(characters_id IS NOT NULL AND planets_id IS NULL) OR (characters_id IS NULL AND planets_id IS NOT NULL)',
            name='check_one_favorite_type'
        ),
    )
    user: Mapped["User"] = relationship(
        "User", back_populates="favorites", foreign_keys=[users_id])
    character: Mapped["Character"] = relationship(
        "Character", back_populates="favorites", foreign_keys=[characters_id])
    planet: Mapped["Planet"] = relationship(
        "Planet", back_populates="favorites", foreign_keys=[planets_id])

    def serialize(self):
        return {
            'favorites_id': self.favorites_id,
        }

    def serialize_with_relations(self):
        data = self.serialize()
        data['user'] = self.user.serialize()
        data['character'] = self.character.serialize() if self.character else {}
        data['planet'] = self.planet.serialize() if self.planet else {}
        return data


