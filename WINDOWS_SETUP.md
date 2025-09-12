# Windows系统运行roLabelImg指南

## 🚨 重要提示
从您的错误信息看，需要在Windows系统上重新打包，因为macOS打包的文件无法在Windows上运行。

## 📋 完整的Windows设置步骤

### 步骤1：安装Python
1. 访问 https://www.python.org/downloads/
2. 下载最新版Python (3.8或以上)
3. **重要**: 安装时勾选"Add Python to PATH"

### 步骤2：验证Python安装
打开命令提示符 (cmd)，输入：
```cmd
python --version
pip --version
```
如果显示版本号，说明安装成功。

### 步骤3：安装依赖
```cmd
pip install PyQt5 lxml pyinstaller
```

### 步骤4：下载项目文件
将整个roLabelImg项目文件夹复制到Windows电脑。

### 步骤5：运行打包脚本
在项目文件夹中，双击运行：
```
build_windows_exe.bat
```

或者在命令提示符中运行：
```cmd
cd /d "项目文件夹路径"
build_windows_exe.bat
```

## 🔄 手动打包命令
如果批处理文件不工作，可以手动执行：

```cmd
pyinstaller --onefile --windowed --name=roLabelImg --add-data=icons;icons --add-data=data;data --add-data=libs;libs --hidden-import=PyQt5 --hidden-import=lxml roLabelImg.py
```

## 📱 简化版本 - 直接运行Python脚本

如果打包有问题，可以直接运行Python脚本：

1. 安装依赖：
```cmd
pip install PyQt5 lxml
```

2. 运行程序：
```cmd
python roLabelImg.py
```

## 🛠️ 故障排除

### 问题1：Python命令不识别
**解决方案**：
- 重新安装Python，确保勾选"Add to PATH"
- 或者手动添加Python到系统环境变量

### 问题2：pip命令不识别
**解决方案**：
```cmd
python -m pip install PyQt5 lxml pyinstaller
```

### 问题3：PyQt5安装失败
**解决方案**：
```cmd
# 尝试不同的安装方式
pip install PyQt5-tools
# 或者
conda install pyqt5
```

### 问题4：打包后exe无法运行
**解决方案**：
- 检查Windows Defender或杀毒软件
- 尝试在命令行运行exe查看错误信息
- 使用 `--debug` 参数重新打包

## 💡 最佳实践

### 使用虚拟环境（推荐）：
```cmd
# 创建虚拟环境
python -m venv rolabelimg_env

# 激活虚拟环境
rolabelimg_env\Scripts\activate

# 安装依赖
pip install PyQt5 lxml pyinstaller

# 打包
pyinstaller --onefile --windowed roLabelImg.py
```

### 检查系统要求：
- Windows 7/8/10/11
- Python 3.8+
- 至少2GB RAM
- 500MB可用磁盘空间

## 🎯 成功标志

打包成功后，您应该看到：
- `dist/roLabelImg.exe` 文件
- 文件大小约40-80MB
- 双击可以正常启动程序

## 📞 如果仍有问题

请提供以下信息：
1. Windows版本
2. Python版本 (`python --version`)
3. 具体的错误信息截图
4. 是否使用了虚拟环境

---
**注意**：macOS打包的文件(.app)无法在Windows上运行，必须在Windows系统上重新打包。
