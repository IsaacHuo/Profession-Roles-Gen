#!/bin/bash

echo "正在检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "未检测到Python环境，请先安装Python 3.x"
    echo "您可以从 https://www.python.org/downloads/ 下载安装"
    read -p "按任意键退出..."
    exit 1
fi

echo "正在安装依赖包..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "依赖包安装失败"
    read -p "按任意键退出..."
    exit 1
fi

echo "正在启动程序..."
python3 main.py

read -p "按任意键退出..."