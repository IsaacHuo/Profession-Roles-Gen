@echo off

echo 正在检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 未检测到Python环境，请先安装Python 3.x
    echo 您可以从 https://www.python.org/downloads/ 下载安装
    pause
    exit /b 1
)

echo 正在安装依赖包...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo 依赖包安装失败
    pause
    exit /b 1
)

echo 正在启动程序...
python main.py

pause