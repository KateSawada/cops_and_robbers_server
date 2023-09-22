# このファイルは例です。参考にしてね。

from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select # ここに必要なモノを追加。今回はselectを追加した。

from models import Room # ここに扱いたいテーブル名を記載する。今回はRoomテーブルを使う。

# 初期化
sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def test():
    room_1 = Room(name="hoge") # 基本的にprimary keyはここに指定しなくていい
    
    # Roomテーブルにテストデータを入れてみる
    with Session(engine) as session:
        session.add(room_1)
        session.commit()
    
    # Roomテーブルの情報を取得してみる。
    with Session(engine) as session:
        room_data = session.exec(select(Room)).all()
        # このroom_dataにルームの情報が入った。
        print(room_data)
    
    # Room検索時に、idを指定してみる
    room_id = 1
    room_data_2 = session.get(Room, room_id)
    print(room_data_2) # ここにidが1のRoomテーブルの中身が返ってきてる

    # Roomテーブルから指定のものを削除する
    room_data_3 = session.get(Room, room_id)
    session.delete(room_data_3)
    session.commit()
    
    return None