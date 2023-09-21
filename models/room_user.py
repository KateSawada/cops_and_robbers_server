from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.user import User
    from models.room import Room

class RoomUser(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key='user.id')
    room_id: Optional[int] = Field(default=None, foreign_key='room.id')
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    user: Optional['User'] = Relationship(back_populates='room_user')
    room: Optional['Room'] = Relationship(back_populates='room_user')
    