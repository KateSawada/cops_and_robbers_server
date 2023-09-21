"""FastAPIによるバックエンドサーバーの定義プログラム

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/room/create/{roomName}")
def create_room(roomName: str):
    response: object = {
        "id": 100000,
        "name": "hoge",
        "member": {
            "id": 10,
            "user_name": "hoge",
            "user_status": "police"
        }
    }
    return response

@app.post("/room/join")
def join_room():
    response: object = {
        "id": 100000,
        "name": "string",
        "member": {
            "id": 10,
            "user_name": "theUser",
            "user_status": "police"
        }
    }
    return response

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