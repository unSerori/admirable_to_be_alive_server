#!/bin/bash


# このファイルのディレクトリを保存しておいて移動する
directory_of_this_file=$1
cd $directory_of_this_file

# 仮想環境に入る
echo 'Enter the virtual environment.'
source runtime/bin/activate

# main.pyを実行
echo "Strat program. ------------"
echo -e "\n"  # 改行
python main.py




# 動作確認
# echo "========================"
# echo "+++++++++++"
# echo 1.
# echo $1
# echo 2. 
# text_pwd=`pwd`
# echo $text_pwd
# # 1.
# # python_projects/admirable_to_be_alive_server
# # 2.
# # /home/unserori
# echo "-----------"
