chcp 65001
echo start_win.bat terminated.

rem 仮想環境に入る
echo 'Enter the virtual environment.'
call runtime\Scripts\activate.bat

rem main.pyを実行
echo "Strat program. ------------"
echo.
python main.py

pause
exit /b