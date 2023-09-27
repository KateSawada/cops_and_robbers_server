"""FastAPIによるバックエンドサーバーの定義プログラム

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uuid
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
from models import Room
from models import RoomUser
app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

#requestbodyを定義する
class RoomId(BaseModel):
    room_id: int
    user_id:int
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/room/create/{roomName}")
def create_room(roomName: str):
    #RoomテーブルにroomNameとroomのidを入れる
    with Session(engine) as session:
        db_room = Room(name=roomName)
        session.add(db_room)
        session.commit() #DBへ反映
        session.refresh(db_room)
        response:int = db_room.id
     
    return response

@app.post("/room/join")
#room_id,加わる人の名前,を受け取る
def join_room(join_data:RoomId):
    room_user1 = RoomUser(user_id=join_data.user_id,room_id=join_data.room_id)
    #RoomUserテーブルにデータを入れる
    with Session(engine) as session:
        session.add(room_user1)
        session.commit()
        session.refresh(room_user1)
    

    # response: object = {
    #     "id": 100000,
    #     "name": "string",
    #     "member": {
    #         "id": 10,
    #         "user_name": "theUser",
    #         "user_status": "police"
    #     }
    # }
        return None

@app.post("/team/check")
def team_check():
    response = [
        {
            "id": 100000,
            "name": "string",
            "member": {
                "id": 10,
                "user_name": "theUser",
                "user_status": "police"
            }
        },
    ]

@app.get("/update/position")
def get_update_position():
    response: object = {
        "id": 0,
        "user_name": "string"
    }
    return response

@app.post("/update/position/{user_name}/{gps}")
def post_update_position(user_name: str, gps: str):
    return None

@app.get("/chat/all")
def get_chat_all():
    response: object = {
        "id": 0,
        "name": "string",
        "messages": "string"
    }
    return response

@app.post("/chat/all/{user_name}/{message}/{gps}")
def post_chat_all(user_name: str, message: str, gps: str):
    response: object = {
        "id": 0,
        "name": "string",
        "messages": "string"
    }
    return response