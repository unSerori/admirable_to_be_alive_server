'''
サバ側のmain。Webサーバ起動タスク

flaskでエンドポイント作る。

ログイン処理(post_login)にgoogle垢認証を使い、プレイヤー情報(レベル, 所持アイテム、各いいねポイントの保存、デイリーミッション進捗状況)をgetして同期。
googleカレンダー(home読み込み時)
プレイヤー情報が更新されたらpostして鯖にも同期
'''
import os
from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin  # http通信のCORS制限
from flask_sqlalchemy import SQLAlchemy
# from aqlalchemy import create_engine
# engine = create_engine("sqlite://:memory:")
from dotenv import load_dotenv  # dotenvをインポート
load_dotenv()  # .envファイルの内容を読み込見込む
CLIENT_ID = os.environ.get("CLIENT_ID")  # .envからクライアントIDを持ってくる。
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")  # .envからクライアントシークレットを持ってくる。




app = Flask(__name__)  # インスタンス生成、これによりアクセスされたURIによって処理を変更する。
# alchemyの動作設定
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)  #sqlalchemyのインスタンス


# てーぶるをつくる
class UserInfo(db.Model):
    __tablename__ = 'UserInfo'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.Text)
    name = db.Column(db.Text)
    rank = db.Column(db.Text)
    json_points = db.Column(db.JSON)
    json_stamp = db.Column(db.JSON)


# ディレクトリかんれんの初期化
users_data_dir = os.path.abspath("./users_data")
if not os.path.isdir(users_data_dir):  # フォルダがなければ作る
    os.mkdir(users_data_dir)


# ログイン post_login
@app.route('/post_login', methods=["POST"])  # 送られてくるURLとHTTPメソッド
@cross_origin()  # これでCORS認証をパスしてる
def post_login():
    req = request.get_json(force=True)
    # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
    # ログイン済みか判定して初回ならgoogle login 関連の処理に飛ばす...ってコト？！


# get_userInfo
@app.route('/get_userInfo', methods=["GET"])
@cross_origin()  # これでCORS認証をパスしてる
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




        return req


# get_google_cal
@app.route('/get_google_cal', methods=["GET"])  # 送られてくるURLとHTTPメソッド
@cross_origin()  # これでCORS認証をパスしてる
def get_google_cal():
    req = request.get_json(force=True)
    # ここにしょりかきたい++++++++++++++++++++++++++++++++++++++++++++++++
    return "calend"


# データベース内で重複したmailがあるか確認。返り血はid
def check_mail_exists(model_name, check_existence):  # mail
    row = model_name.query.filter_by(mail=check_existence).first()  # 一致する行を検索して取り出す
    print("check row: " + str(row))
    if row:
        return row.id
    else:
        return None
##処理ここまで




# mainとして実行したときのみ
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# httpとsqliteのひな形
@app.route('/result', methods=['POST'])
@cross_origin()  # これでCORS認証をパスしてる
def insert():
    req_data = request.get_json(force=True)  # リクエストを保存
    print("req_dat: " + str(req_data)) # debug
    # データベース内をに存在するか検索
    id = check_mail_exists(Shohin, req_data["mail"]) # 名前が一致するデータがあるなら更新、ないなら新規さくせい
    print("id: " + str(id)) # debug
    if not id:
        print("ないから新規作成") # debug
        # キーから取り出す req_Data = request.get_json(force=True)
        mail = req_data["mail"]
        name = req_data["name"]
        rank = req_data["rank"]
        json_points = req_data["points"]
        json_stamp = req_data["stamp"]
        # エントリを作成
        userInfo = UserInfo(mail = mail, name = name, rank = rank, json_points = json_points, json_stamp = json_stamp)#
        # 新しいデータベースエントリを作成(add)し、セッション内の変更をデータベースに永続保存(commit)する
        db.session.add(userInfo)
        db.session.commit()
        # # エントリを作成
        # userInfo = UserInfo()
        # # キーから取り出す req_Data = request.get_json(force=True)
        # userInfo.name_txt = req_data["name"]
        # userInfo.price_txt = req_data["price"]
        # # 新しいデータベースエントリを作成(add)し、セッション内の変更をデータベースに永続保存(commit)する
        # db.session.add(userInfo)
        # db.session.commit()
    else:
        print(f"あるから更新{id}") # debug
        # テーブルとidとそのcolumnをしていして上書き
        UserInfo.query.get(id).mail = req_data["mail"]
        UserInfo.query.get(id).name = req_data["name"]
        UserInfo.query.get(id).rank = req_data["rank"]
        UserInfo.query.get(id).json_points = req_data["points"]
        UserInfo.query.get(id).json_stamp = req_data["stamp"]
        # セッション内の変更をデータベースに永続保存(commit)する
        db.session.commit()
    return req_data