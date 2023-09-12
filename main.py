'''
サバ側のmain

flaskでエンドポイント作る。

プレイヤー情報(レベル, 所持アイテム、各いいねポイントの保存、デイリーミッション進捗状況)を保持
ログイン時に同期
googleアカウントでログイン
googleカレンダー
'''
import os
# from flask import Flask, jsonify, request, render_template
# from flask_cors import CORS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv  # dotenvをインポート
load_dotenv()  # .envファイルの内容を読み込見込む
CLIENT_ID = os.environ.get("CLIENT_ID")  # .envからクライアントIDを持ってくる。
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")  # .envからクライアントシークレットを持ってくる。



#app = Flask(__name__)  # インスタンス生成、これによりアクセスされたURIによって処理を変更する。
app = FastAPI()


origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# index
@app.route('/')  # URIの指定。/のみならドメインorIPaddのみでアクセスされた場合のみ。HTTPメソッドを指定する。
def index():
    return '<p>Index  # index</p>'

# index
@app.route('/send_userInfo', methods=["POST"])
def send_userInfo():
    userInfo = request.get_json(force=True)
    if not userInfo:
        print("データ入ってないやん")
    else:
        print(userInfo)


##




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)