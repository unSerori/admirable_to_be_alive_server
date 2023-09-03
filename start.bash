#!/bin/bash

# このファイルのディレクトリを保存しておいて移動する
directory_of_this_file=$1
cd $directory_of_this_file

# 仮想環境に入る
echo 'Enter the virtual environment.'
source runtime/bin/activate
# main.pyを実行
echo "Strat program."
python main.py