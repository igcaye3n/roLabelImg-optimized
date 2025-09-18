# roLabelImg 可执行文件构建指南

## 🎯 三种构建方法

### 方法1: 使用GitHub Actions自动构建 (推荐)

这是最简单的方法，可以自动构建Windows、macOS和Linux版本。

#### 步骤:
1. **Fork或Clone本项目到GitHub**
2. **推送代码到GitHub仓库**
3. **自动构建触发**:
   - 推送到main/master分支时自动触发
   - 也可以在GitHub仓库的Actions页面手动触发
4. **下载构建结果**:
   - 进入GitHub仓库的Actions页面
   - 找到最新的构建任务
   - 下载构建的可执行文件

#### 优势:
- ✅ 完全自动化
- ✅ 支持多平台构建
- ✅ 无需本地环境配置
- ✅ 免费使用GitHub Actions

---

### 方法2: 本地构建

#### 前置要求:
- Python 3.8+
- pip包管理器

#### Windows用户:
1. **使用简化批处理脚本**:
   ```cmd
   双击运行: build_windows_simple.bat
   ```

2. **或使用Python脚本**:
   ```cmd
   python build_exe.py
   ```

#### macOS/Linux用户:
```bash
# 安装依赖
pip install PyQt5 lxml pyinstaller

# 运行构建脚本
python build_exe.py
```

#### 高级用户:
```bash
# 直接使用PyInstaller命令
pyinstaller --onefile --windowed \
  --name=roLabelImg \
  --add-data="icons:icons" \
  --add-data="data:data" \
  --add-data="libs:libs" \
  --hidden-import=PyQt5 \
  --hidden-import=lxml \
  roLabelImg.py
```

---

### 方法3: 使用Docker构建 (高级)

创建Dockerfile进行跨平台构建：

```dockerfile
FROM python:3.9-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    qt5-default \
    && rm -rf /var/lib/apt/lists/*

# 安装Python依赖
COPY requirements.txt .
RUN pip install -r requirements.txt

# 复制项目文件
COPY . /app
WORKDIR /app

# 构建可执行文件
RUN python build_exe.py
```

---

## 📦 构建选项说明

### 基本构建
- 创建单个可执行文件
- 包含所有必要的依赖
- 无需目标机器安装Python

### 优化构建
- 排除不必要的模块
- 压缩可执行文件
- 减小文件大小

### 调试构建
- 保留控制台输出
- 便于问题诊断
- 开发者使用

---

## 🔧 常见问题解决

### 问题1: "找不到PyQt5"
```bash
# 解决方案
pip install PyQt5
# 或使用conda
conda install pyqt5
```

### 问题2: "编译后文件过大"
```bash
# 使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows

pip install PyQt5 lxml pyinstaller
python build_exe.py
```

### 问题3: "运行时缺少文件"
确保包含所有必要的数据文件：
```bash
--add-data="icons:icons"
--add-data="data:data"
--add-data="libs:libs"
```

### 问题4: "杀毒软件误报"
- 将可执行文件添加到杀毒软件白名单
- 使用代码签名证书（高级用户）

---

## 📋 构建检查清单

### 构建前确认:
- [ ] Python环境正常 (python --version)
- [ ] 依赖已安装 (pip list | grep PyQt5)
- [ ] 项目可以正常运行 (python roLabelImg.py)
- [ ] 有足够磁盘空间 (至少2GB)

### 构建后测试:
- [ ] 可执行文件存在于dist/目录
- [ ] 双击可以正常启动
- [ ] 能够加载和保存图像
- [ ] 边界限制功能正常工作
- [ ] 所有快捷键功能正常

---

## 🎯 推荐构建配置

### 标准配置 (平衡大小和兼容性)
```bash
pyinstaller --onefile --windowed \
  --name=roLabelImg \
  --add-data="icons:icons" \
  --add-data="data:data" \
  --add-data="libs:libs" \
  roLabelImg.py
```

### 最小化配置 (最小文件大小)
```bash
pyinstaller --onefile --windowed \
  --name=roLabelImg-mini \
  --exclude-module=tkinter \
  --exclude-module=matplotlib \
  roLabelImg.py
```

### 调试配置 (便于排错)
```bash
pyinstaller --onedir --console \
  --name=roLabelImg-debug \
  roLabelImg.py
```

---

## 📊 文件大小参考

| 配置 | 大小范围 | 说明 |
|------|----------|------|
| 标准构建 | 150-200MB | 包含完整功能 |
| 优化构建 | 100-150MB | 排除不必要模块 |
| 最小构建 | 80-120MB | 基础功能 |

---

## 🚀 发布流程

### 自动发布 (GitHub Actions)
1. 创建Git标签: `git tag v1.0.0`
2. 推送标签: `git push origin v1.0.0`
3. 自动触发构建和发布

### 手动发布
1. 运行构建脚本
2. 测试可执行文件
3. 打包发布文件
4. 上传到发布平台

---

## 📞 获取帮助

如果遇到构建问题，请提供：
1. 操作系统版本
2. Python版本 (`python --version`)
3. 完整的错误信息
4. 使用的构建命令

### 推荐顺序:
1. 🥇 **GitHub Actions** - 最简单可靠
2. 🥈 **本地Windows构建** - Windows .exe
3. 🥉 **本地其他平台构建** - 对应平台可执行文件

---

## ✨ 特别说明

本项目已优化以下功能：
- ✅ 解除了标注框的边界限制
- ✅ 支持中心点在边界时调整大小
- ✅ 优化了用户操作体验
- ✅ 保持了原有的所有功能

构建的可执行文件包含了所有这些优化功能！
