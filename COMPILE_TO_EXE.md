# roLabelImg 编译成 EXE 完整指南

## 🎯 编译成EXE的三种方法

### 方法1：在Windows机器上编译（最佳）

#### 步骤1：准备Windows环境
1. 在Windows电脑上安装Python 3.8+
   - 下载：https://www.python.org/downloads/
   - 安装时勾选"Add Python to PATH"

2. 安装依赖包：
```cmd
pip install PyQt5 lxml pyinstaller
```

#### 步骤2：复制项目文件
将整个roLabelImg-master文件夹复制到Windows电脑

#### 步骤3：运行编译脚本
双击运行：`build_windows_exe.bat`

或手动执行：
```cmd
pyinstaller --onefile --windowed --name=roLabelImg --add-data=icons;icons --add-data=data;data --add-data=libs;libs --hidden-import=PyQt5 --hidden-import=lxml roLabelImg.py
```

#### 步骤4：获取EXE文件
编译完成后，在`dist/`目录下找到`roLabelImg.exe`

---

### 方法2：使用云服务编译

#### GitHub Actions（免费）
1. 创建`.github/workflows/build.yml`文件
2. 推送到GitHub仓库
3. 自动编译并下载exe文件

#### 云服务器
1. 租用Windows云服务器
2. 按方法1步骤编译
3. 下载编译好的exe文件

---

### 方法3：交叉编译（实验性）

#### 使用Wine + PyInstaller
```bash
# 在macOS/Linux上安装Wine
brew install wine

# 安装Windows版Python到Wine环境
wine python-installer.exe

# 在Wine环境中编译
wine pip install PyQt5 lxml pyinstaller
wine pyinstaller --onefile --windowed roLabelImg.py
```

**注意：此方法较复杂，成功率不高**

---

## 📦 编译选项说明

### 基本编译命令
```cmd
pyinstaller roLabelImg.py
```

### 高级编译选项
```cmd
pyinstaller ^
    --onefile ^                    # 打包成单个文件
    --windowed ^                   # 无控制台窗口
    --name=roLabelImg ^           # 指定exe文件名
    --icon=icons/app.ico ^        # 添加图标
    --add-data=icons;icons ^      # 包含图标文件夹
    --add-data=data;data ^        # 包含数据文件
    --add-data=libs;libs ^        # 包含库文件
    --hidden-import=PyQt5 ^       # 确保包含PyQt5
    --hidden-import=lxml ^        # 确保包含lxml
    --upx-dir=path/to/upx ^      # 压缩（可选）
    roLabelImg.py
```

### 大小优化选项
```cmd
--exclude-module=tkinter          # 排除不需要的模块
--exclude-module=matplotlib       # 排除matplotlib
--onefile                         # 单文件模式
--upx-dir=UPX_PATH               # 使用UPX压缩
```

---

## 🔧 常见问题解决

### 问题1：PyQt5找不到
```cmd
pip install PyQt5-tools
# 或者
conda install pyqt5
```

### 问题2：编译后文件过大
```cmd
# 使用虚拟环境减少依赖
python -m venv clean_env
clean_env\Scripts\activate
pip install PyQt5 lxml pyinstaller
pyinstaller roLabelImg.py
```

### 问题3：exe运行时缺少DLL
```cmd
# 添加缺少的库
--add-binary=path/to/dll;.
```

### 问题4：杀毒软件误报
- 将exe添加到杀毒软件白名单
- 使用代码签名证书

---

## 📋 编译检查清单

编译前确认：
- [ ] Python环境正常
- [ ] 所有依赖已安装
- [ ] 项目可以正常运行
- [ ] 有足够的磁盘空间（至少1GB）

编译后测试：
- [ ] exe文件可以正常启动
- [ ] 所有功能正常工作
- [ ] 边界限制切换功能正常
- [ ] 可以加载和保存文件

---

## 🎯 推荐编译配置

### 标准配置（平衡大小和兼容性）
```cmd
pyinstaller --onefile --windowed --name=roLabelImg --add-data=icons;icons --add-data=data;data --add-data=libs;libs roLabelImg.py
```

### 最小化配置（最小文件大小）
```cmd
pyinstaller --onefile --windowed --name=roLabelImg_mini --exclude-module=tkinter roLabelImg.py
```

### 调试配置（便于排错）
```cmd
pyinstaller --onedir --console --name=roLabelImg_debug roLabelImg.py
```

---

## 📞 获取帮助

如果编译遇到问题，请提供：
1. Windows版本
2. Python版本
3. 完整的错误信息
4. 使用的编译命令

推荐使用方法1在Windows机器上编译，成功率最高！
