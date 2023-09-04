# admirable_to_be_alive_server

## 導入
### 鍵の生成
raspiとのsshではid_ed25519_ssh_raspiという名前の鍵ファイルを作成した。
```bash: windows
ssh-keygen -t <鍵の種類> -f <ファイル名>
ssh-keygen -t ed25519 -f id_ed25519_ssh_raspi
```

### IPとかを省略
.ssh直下にconfigというファイルを作って以下を書き込む。IPとかも順次書く。
```config: config
Host raspi
    HostName <ip>
    	User <username>
```
と記載。

### ラズパイのSSH許可設定
設定からインターフェース、SSHをONに。
もしくは
```bash: raspi
$ sudo raspi-config
```
で同じく設定。

### sshの疎通
IPを確認。
```bash: raspi
$ ip a
$ ip addr
```
出力結果の inet という項目。
または
```bash:
hostname -I
```

### 鍵を渡す。
最初に作った公開鍵をラズパイにも渡す。
ssh用の隠しフォルダを作る。
```bash: raspi
# 隠しフォルダを作る
$ mkdir ~/.ssh
```
scpで公開鍵を送る
```bash: windows
scp <ファイル名> <raspiのユーザ名>@<IPアドレス>:<送信先のディレクトリ>
scp id_ed25519_ssh_raspi.pub pi@xxxx.xxxx.xxxx.xxxx:~/.ssh
```
公開鍵のパーミッションを変更
```bash: raspi
# 鍵の内容をauthorized_keysに追加
$ cat ~/.ssh/id_ed25519_ssh_raspi.pub >> ~/.ssh/authorized_keys
# authorized_keysのパーミッションを600に。600管理者のみが読み書きできる
$ chmod 600 ~/.ssh/authorized_keys
# .sshフォルダのパーミッションを700に。700管理者のみが読み書き実行できる
chmod 700 ~/.ssh
# 公開鍵ファイルを削除
$ rm ~/.ssh/id_ed25519_ssh_raspi.pub
```

### WinSCP
開発はwindowsPCで行った。その際WinSCPを利用した。以下を設定した。
1. 環境設定 -> パネル -> 隠しファイルを表示
2. 同期 -> ディレクトリを設定、方向をローカルリモートに、異なるファイルをミラー、比較基準を全部、同じオプションで使いまわし
3. 環境設定 -> 転送 -> デフォルト -> 編集 -> ファイルマスクに同期除外したいファイルディレクトリを追加