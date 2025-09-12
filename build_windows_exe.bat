@echo off
chcp 65001 >nul
REM roLabelImg Windows EXE 打包脚本
REM 在Windows系统上运行此脚本来打包

echo ===========================================
echo    roLabelImg Windows EXE 打包工具
echo ===========================================

REM 显示当前目录
echo 当前目录: %CD%

REM 检查Python是否安装
echo 正在检查Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到Python，请先安装Python
    echo 请访问 https://www.python.org/downloads/ 下载安装
    echo 安装时务必勾选 "Add Python to PATH"
    pause
    exit /b 1
) else (
    echo Python 已安装
    python --version
)

REM 检查依赖是否安装
echo 正在检查依赖...

REM 检查PyQt5
pip show PyQt5 >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装PyQt5...
    pip install PyQt5
)

REM 检查lxml
pip show lxml >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装lxml...
    pip install lxml
)

REM 检查PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
)

echo 所有依赖已准备就绪

REM 清理旧的构建文件
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo 清理旧文件完成

REM 开始打包
echo 开始打包roLabelImg...

pyinstaller ^
    --onefile ^
    --windowed ^
    --name=roLabelImg ^
    --icon=icons/app.ico ^
    --add-data=icons;icons ^
    --add-data=data;data ^
    --add-data=libs;libs ^
    --hidden-import=PyQt5 ^
    --hidden-import=PyQt5.QtCore ^
    --hidden-import=PyQt5.QtGui ^
    --hidden-import=PyQt5.QtWidgets ^
    --hidden-import=lxml ^
    --hidden-import=lxml.etree ^
    roLabelImg.py

if %errorlevel% equ 0 (
    echo.
    echo ===========================================
    echo              打包成功！
    echo ===========================================
    echo 可执行文件位置: dist\roLabelImg.exe
    echo 文件大小: 
    dir dist\roLabelImg.exe | findstr roLabelImg.exe
    echo.
    echo 您可以将dist目录中的roLabelImg.exe分发给其他用户
) else (
    echo.
    echo ===========================================
    echo              打包失败！
    echo ===========================================
    echo 请检查错误信息并重试
)

pause
