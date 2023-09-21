from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.room_user import RoomUser
    from models.message import Message


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    status: str = Field(index=True)
    gps: str = Field(index=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    room_user: list['RoomUser'] = Relationship(back_populates='user')
    message: list['Message'] = Relationship(back_populates='user')