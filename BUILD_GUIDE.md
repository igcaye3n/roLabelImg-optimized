# roLabelImg 打包成EXE指南

## 📦 打包结果

**恭喜！** roLabelImg已经成功打包！

### 当前生成的文件：
- **macOS版本**: `dist/roLabelImg` (46.8 MB)
- **macOS应用包**: `dist/roLabelImg.app` (可直接在macOS上运行)

## 🖥️ 不同平台的打包方法

### 1. Windows平台 (生成 .exe文件)

#### 方法A: 在Windows机器上打包
1. 将整个项目文件夹复制到Windows电脑
2. 安装Python和依赖：
   ```cmd
   pip install PyQt5 lxml pyinstaller
   ```
3. 运行打包脚本：
   ```cmd
   build_windows_exe.bat
   ```

#### 方法B: 使用交叉编译（推荐）
```bash
# 安装交叉编译工具
pip install pyinstaller-cross

# 打包Windows版本
pyinstaller --onefile --windowed --target-arch=win_amd64 \
    --name=roLabelImg \
    --add-data=icons:icons \
    --add-data=data:data \
    --add-data=libs:libs \
    --hidden-import=PyQt5 \
    --hidden-import=lxml \
    roLabelImg.py
```

### 2. Linux平台

```bash
# 在Linux系统上运行
pyinstaller --onefile --windowed \
    --name=roLabelImg \
    --add-data=icons:icons \
    --add-data=data:data \
    --add-data=libs:libs \
    --hidden-import=PyQt5 \
    --hidden-import=lxml \
    roLabelImg.py
```

### 3. macOS平台 (已完成)

✅ 已生成：`dist/roLabelImg.app`

## 🚀 使用方法

### macOS用户：
1. 双击 `dist/roLabelImg.app` 即可运行
2. 或者在终端运行：`./dist/roLabelImg`

### Windows用户：
1. 双击 `dist/roLabelImg.exe` 即可运行
2. 第一次运行可能需要允许Windows防火墙

### Linux用户：
1. 在终端运行：`./dist/roLabelImg`
2. 可能需要设置执行权限：`chmod +x dist/roLabelImg`

## ⚙️ 高级打包选项

### 自定义图标
```bash
--icon=path/to/your/icon.ico  # Windows
--icon=path/to/your/icon.icns # macOS
```

### 包含其他文件
```bash
--add-data=source:dest  # 添加数据文件
--add-binary=source:dest  # 添加二进制文件
```

### 优化大小
```bash
--exclude-module=module_name  # 排除不需要的模块
--upx-dir=UPX_DIR  # 使用UPX压缩
```

## 🔧 故障排除

### 常见问题：

1. **PyQt5找不到**
   ```bash
   pip install PyQt5
   ```

2. **lxml找不到**
   ```bash
   pip install lxml
   ```

3. **打包后运行出错**
   - 检查是否包含了所有必要的文件
   - 查看错误日志
   - 尝试使用 `--debug` 参数

4. **文件太大**
   - 使用 `--exclude-module` 排除不需要的模块
   - 使用虚拟环境减少依赖

### Windows特定问题：

1. **杀毒软件误报**
   - 将生成的exe添加到杀毒软件白名单
   - 使用代码签名证书

2. **DLL缺失**
   - 安装Visual C++ Redistributable
   - 使用 `--add-binary` 包含缺失的DLL

## 📋 分发清单

分发给用户时需要包含：
- ✅ `roLabelImg.exe` (Windows) 或 `roLabelImg.app` (macOS)
- ✅ 使用说明文档
- ✅ 示例图片和配置文件（可选）

## 🎯 新功能说明

打包的版本包含了所有优化功能：
- ✅ **无边界限制标注** - 支持标注框超出图像边界
- ✅ **Ctrl+B快捷键** - 快速切换边界限制
- ✅ **状态持久化** - 记住用户的边界限制设置
- ✅ **改进的用户界面** - 更友好的操作体验

## 🔗 相关文件

- `build_exe.py` - 通用打包脚本
- `build_windows_exe.bat` - Windows专用打包脚本
- `roLabelImg.spec` - PyInstaller配置文件
- `BOUNDARY_OPTIMIZATION_SUMMARY.md` - 功能优化说明

---

**注意：** 生成的可执行文件包含了完整的Python环境和所有依赖，因此文件较大（40-50MB）是正常的。这确保了在没有安装Python的机器上也能正常运行。
