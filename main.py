'''
サバ側のmain

flaskでエンドポイント作る。

プレイヤー情報(レベル, 所持アイテム、各いいねポイントの保存、デイリーミッション進捗状況)を保持
ログイン時に同期
googleアカウントでログイン
googleカレンダー
'''
import os
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv  # dotenvをインポート
load_dotenv()  # .envファイルの内容を読み込見込む
CLIENT_ID = os.environ.get("CLIENT_ID")  # .envからクライアントIDを持ってくる。
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")  # .envからクライアントシークレットを持ってくる。




app = Flask('__name__')  # インスタンス生成、これによりアクセスされたURIによって処理を変更する。

print(CLIENT_ID)
print (CLIENT_SECRET)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)