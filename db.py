from sqlmodel import SQLModel, create_engine

from models import Message,Room,RoomUser,User  # NOQA

sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    # migrate
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_db_and_tables()
