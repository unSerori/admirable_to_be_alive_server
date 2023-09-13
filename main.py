'''
サバ側のmain

flaskでエンドポイント作る。

ログイン処理(post_login)にgoogle垢認証を使い、プレイヤー情報(レベル, 所持アイテム、各いいねポイントの保存、デイリーミッション進捗状況)をgetして同期。
googleカレンダー(home読み込み時)
プレイヤー情報が更新されたらpostして鯖にも同期
'''
import os
from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin
from dotenv import load_dotenv  # dotenvをインポート
load_dotenv()  # .envファイルの内容を読み込見込む
CLIENT_ID = os.environ.get("CLIENT_ID")  # .envからクライアントIDを持ってくる。
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")  # .envからクライアントシークレットを持ってくる。




app = Flask(__name__)  # インスタンス生成、これによりアクセスされたURIによって処理を変更する。

# フォルダの初期化
users_data_dir = os.path.abspath("./users_data")
if not os.path.isdir(users_data_dir):  # フォルダがなければ作る
    os.mkdir(users_data_dir)


# # エンドポイント index
# @app.route('/')  # 送られてくるURLとHTTPメソッド @~~はデコレータ。関数の上に書くと~~でラップできる。# URIの指定。/のみならドメインorIPaddのみでアクセスされた場合のみ。HTTPメソッドを指定する。
# @cross_origin()  # これでCORS認証をパスしてる
# def index():
#     return '<p>Index  # index</p>'


# ログイン post_login
@app.route('/post_login', methods=["POST"])  # 送られてくるURLとHTTPメソッド
@cross_origin()  # これでCORS認証をパスしてる
def post_login():
    req = request.get_json(force=True)
    # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
    # ログイン済みか判定して初回ならgoogle login 関連の処理に飛ばす...ってコト？！


# get_userInfo
@app.route('/get_userInfo', methods=["GET"])
@cross_origin()
def get_userInfo():
    req = request.get_json(force=True)
    print(req) # debug
    # 送られてきてたらそれそうおうの処理を下に書く
    # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
    # ここにsqlite
    # ユーザー情報を返してあげる
    return "data" # spliteからパクってくる


# post_userInfo
@app.route('/post_userInfo', methods=["POST"])  # 送られてくるURLとHTTPメソッド @~~はデコレータ。関数の上に書くと~~でラップできる。
@cross_origin()  # これでCORS認証をパスしてる
def post_userInfo():
    req = request.get_json(force=True)
    if not req:  # なんも送られてこやんばあい
        print("データ入ってないやん")
        return "no-data"
    else:  # 送られてきてたらそれそうおうの処理を下に書く
        print(req)
        # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
        # ここにsqlite
        # spliteに書き込む。




        return "data"


# get_google_cal
@app.route('/get_google_cal', methods=["GET"])  # 送られてくるURLとHTTPメソッド
@cross_origin()  # これでCORS認証をパスしてる
def get_google_cal():
    req = request.get_json(force=True)
    # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
    return "calend"



##処理ここまで




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)