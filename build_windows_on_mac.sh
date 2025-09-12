#!/bin/bash
# 在macOS上编译Windows EXE的脚本

echo "============================================"
echo "    在macOS上编译roLabelImg Windows EXE"
echo "============================================"

# 检查依赖
echo "正在检查依赖..."

# 检查pyinstaller
if ! command -v pyinstaller &> /dev/null; then
    echo "正在安装PyInstaller..."
    pip install pyinstaller
fi

# 方法1: 尝试使用PyInstaller直接编译（可能生成macOS可执行文件，但值得一试）
echo "正在尝试编译..."
echo "注意：这可能生成macOS格式的文件，但我们先试试"

# 清理旧文件
if [ -d "build" ]; then
    rm -rf build
    echo "清理build目录"
fi

if [ -d "dist" ]; then
    rm -rf dist
    echo "清理dist目录"
fi

# 编译
echo "开始编译..."
pyinstaller \
    --onefile \
    --windowed \
    --name=roLabelImg \
    --add-data="icons:icons" \
    --add-data="data:data" \
    --add-data="libs:libs" \
    --hidden-import=PyQt5 \
    --hidden-import=PyQt5.QtCore \
    --hidden-import=PyQt5.QtGui \
    --hidden-import=PyQt5.QtWidgets \
    --hidden-import=lxml \
    --hidden-import=lxml.etree \
    roLabelImg.py

if [ $? -eq 0 ]; then
    echo ""
    echo "============================================"
    echo "              编译完成！"
    echo "============================================"
    echo "生成的文件位置："
    ls -la dist/
    echo ""
    echo "注意：在macOS上编译的文件主要用于macOS系统"
    echo "要获得Windows exe文件，建议："
    echo "1. 使用Windows虚拟机"
    echo "2. 使用云服务器"
    echo "3. 使用GitHub Actions自动编译"
else
    echo ""
    echo "============================================"
    echo "              编译失败！"
    echo "============================================"
    echo "请检查错误信息"
fi

echo ""
echo "其他选项："
echo "1. 运行 'bash github_actions_setup.sh' 设置自动编译"
echo "2. 查看 COMPILE_TO_EXE.md 获取详细说明"
