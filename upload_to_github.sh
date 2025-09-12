#!/bin/bash

echo "🚀 roLabelImg 自动上传到GitHub并编译EXE"
echo "=========================================="

# 检查Git状态
if [ ! -d ".git" ]; then
    echo "❌ 未找到Git仓库，请先初始化Git"
    exit 1
fi

# 清理不需要的文件
echo "🧹 清理不需要的文件..."
rm -rf dist/
rm -rf build/
rm -rf __pycache__/
rm -rf */__pycache__/
rm -rf */*/__pycache__/
rm -f *.pyc
rm -f */*.pyc
rm -f */*/*.pyc
rm -f *.spec
rm -f roLabelImg-优化版.zip

# 添加所有文件
echo "📁 添加文件到Git..."
git add .

# 提交更改
echo "💾 提交更改..."
commit_msg="Update roLabelImg with boundary optimization - $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_msg" || echo "ℹ️ 没有新的更改需要提交"

# 推送到GitHub
echo "⬆️ 推送到GitHub..."
if git push origin main; then
    echo "✅ 成功推送到GitHub!"
    echo ""
    echo "🎯 接下来的步骤："
    echo "1. 访问您的GitHub仓库"
    echo "2. 点击 'Actions' 标签页"
    echo "3. 等待自动编译完成（约5-10分钟）"
    echo "4. 在Artifacts中下载编译好的Windows EXE文件"
    echo ""
    echo "📱 GitHub仓库地址："
    git remote get-url origin
else
    echo "❌ 推送失败，请检查网络连接或仓库权限"
    exit 1
fi
