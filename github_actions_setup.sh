#!/bin/bash
# GitHub Actions 自动编译设置脚本

echo "============================================"
echo "    GitHub Actions 自动编译EXE设置"
echo "============================================"

echo "这个脚本将帮助您设置GitHub Actions来自动编译Windows EXE文件"
echo ""

# 检查git
if ! command -v git &> /dev/null; then
    echo "错误：未找到git，请先安装git"
    exit 1
fi

echo "步骤说明："
echo "1. 将代码推送到GitHub仓库"
echo "2. GitHub Actions会自动编译Windows EXE"
echo "3. 下载编译好的EXE文件"
echo ""

read -p "是否继续设置GitHub Actions？(y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # 初始化git仓库（如果还没有）
    if [ ! -d ".git" ]; then
        echo "初始化git仓库..."
        git init
        echo "dist/" >> .gitignore
        echo "build/" >> .gitignore
        echo "__pycache__/" >> .gitignore
        echo "*.pyc" >> .gitignore
        echo "*.spec" >> .gitignore
    fi
    
    echo "GitHub Actions工作流已创建在: .github/workflows/build-exe.yml"
    echo ""
    echo "接下来的步骤："
    echo "1. 在GitHub上创建新仓库"
    echo "2. 运行以下命令推送代码："
    echo "   git add ."
    echo "   git commit -m 'Add roLabelImg with boundary optimization'"
    echo "   git remote add origin https://github.com/您的用户名/仓库名.git"
    echo "   git push -u origin main"
    echo ""
    echo "3. 推送后，在GitHub仓库的Actions标签页查看编译进度"
    echo "4. 编译完成后，在Actions页面下载roLabelImg.exe文件"
    
    # 询问是否现在就提交
    echo ""
    read -p "是否现在就添加文件到git？(y/n): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add .
        echo "文件已添加到git暂存区"
        echo "接下来请运行："
        echo "git commit -m 'Add roLabelImg with boundary optimization and auto-build'"
        echo "然后推送到GitHub仓库"
    fi
else
    echo "设置已取消"
fi

echo ""
echo "您也可以手动编译："
echo "1. 在macOS上运行: bash build_windows_on_mac.sh"
echo "2. 在Windows机器上运行: build_windows_exe.bat"
