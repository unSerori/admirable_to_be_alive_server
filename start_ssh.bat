chcp 65001
echo start_ssh.bat terminated.

rem SSH接続する。仮想環境に入って実行するbashを呼び出す。
ssh raspberrypi.local "source ~/python_projects/admirable_to_be_alive_server/start.bash python_projects/admirable_to_be_alive_server"

pause
exit /b