# cops_and_robbers_server

# 動作環境
- python 3.11.3
- venv使用

# 環境構築
- pyenvの導入
  - 適当にググって
- pyenv上にpython 3.11.3 の導入
  - `pyenv install 3.11.3`
- 仮想環境の作成(1回やればOK)
  - `python -m venv venv`
- 仮想環境の起動
  - mac/linux: `source venv/bin/activate`
  - windows: `./venv/Scripts/activate`
- パッケージのインストール
  - `pip install -r requirements.txt`

# 開発時
- 仮想環境の起動
  - mac/linux: `source venv/bin/activate`
  - windows: `./venv/Scripts/activate`
- サーバー起動
  - `uvicorn app:app --reload`

