@echo off
chcp 65001 >nul
REM roLabelImg 直接运行脚本（不打包）
REM 适用于Windows系统

echo ===========================================
echo          roLabelImg 快速启动
echo ===========================================

REM 检查Python
echo 正在检查Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到Python
    echo 请先安装Python: https://www.python.org/downloads/
    echo 安装时勾选 "Add Python to PATH"
    pause
    exit /b 1
)

REM 安装必要依赖
echo 正在安装/检查依赖...
pip install PyQt5 lxml

REM 运行程序
echo 正在启动roLabelImg...
python roLabelImg.py

REM 如果程序意外退出，暂停显示错误信息
if %errorlevel% neq 0 (
    echo.
    echo 程序运行出现错误，错误代码: %errorlevel%
    echo 请检查上方的错误信息
    pause
)
