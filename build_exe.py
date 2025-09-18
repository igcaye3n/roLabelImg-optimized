#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
roLabelImg打包脚本
使用PyInstaller将roLabelImg打包成可执行文件
支持Windows、macOS、Linux多平台打包
"""

import os
import sys
import platform
import subprocess
import shutil
from datetime import datetime

def get_platform_info():
    """获取平台信息"""
    system = platform.system()
    arch = platform.machine()
    return system, arch

def build_exe():
    """打包roLabelImg为可执行文件"""
    
    system, arch = get_platform_info()
    print(f"🚀 开始打包roLabelImg... (平台: {system} {arch})")
    print(f"🕐 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 清理旧的构建文件
    for directory in ['build', 'dist', '__pycache__']:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"✅ 清理{directory}目录")
    
    # 清理 .spec 文件
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            os.remove(file)
            print(f"✅ 清理{file}")
    
    # 根据平台设置不同的参数
    if system == 'Windows':
        data_separator = ';'
        exe_name = 'roLabelImg.exe'
        icon_file = 'icons/app.ico'
    else:
        data_separator = ':'
        exe_name = 'roLabelImg'
        icon_file = 'icons/app.icns' if system == 'Darwin' else ''
    
    # PyInstaller命令参数
    cmd = [
        'pyinstaller',
        '--onefile',  # 打包成单个文件
        '--windowed',  # 无控制台窗口（GUI应用）
        f'--name=roLabelImg-{system}-{arch}',  # 包含平台信息的文件名
        f'--add-data=icons{data_separator}icons',  # 包含图标文件夹
        f'--add-data=data{data_separator}data',  # 包含数据文件夹  
        f'--add-data=libs{data_separator}libs',  # 包含libs文件夹
        f'--add-data=resources.py{data_separator}.',  # 包含resources.py文件
        '--hidden-import=PyQt5',
        '--hidden-import=resources',
        '--hidden-import=PyQt5.QtCore',
        '--hidden-import=PyQt5.QtGui', 
        '--hidden-import=PyQt5.QtWidgets',
        '--hidden-import=lxml',
        '--hidden-import=lxml.etree',
        '--hidden-import=xml.etree',
        '--hidden-import=xml.etree.ElementTree',
        # 排除不需要的模块以减小文件大小
        '--exclude-module=tkinter',
        '--exclude-module=matplotlib',
        '--exclude-module=numpy',
        '--exclude-module=scipy',
        '--exclude-module=IPython',
        'roLabelImg.py'
    ]
    
    # 添加图标（如果存在）
    if icon_file and os.path.exists(icon_file):
        cmd.insert(-1, f'--icon={icon_file}')
        print(f"✅ 使用图标: {icon_file}")
    
    # 移除空的参数
    cmd = [arg for arg in cmd if arg]
    
    try:
        print("📦 开始PyInstaller打包...")
        print(f"命令: {' '.join(cmd)}")
        
        # 实时显示输出
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                 universal_newlines=True, bufsize=1)
        
        # 实时打印输出
        for line in process.stdout:
            print(f"  {line.rstrip()}")
        
        process.wait()
        
        if process.returncode == 0:
            print("✅ 打包成功！")
            
            # 查找生成的可执行文件
            dist_files = []
            if os.path.exists('dist'):
                dist_files = [f for f in os.listdir('dist') if not f.endswith('.txt')]
            
            if dist_files:
                exe_file = os.path.join('dist', dist_files[0])
                print(f"📁 可执行文件位置: {os.path.abspath(exe_file)}")
                
                # 显示文件大小
                file_size = os.path.getsize(exe_file) / (1024 * 1024)  # MB
                print(f"📊 文件大小: {file_size:.2f} MB")
                
                # 创建版本信息文件
                create_release_info(exe_file, system, arch)
                
                print(f"🕐 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                return True
            else:
                print("❌ 找不到生成的可执行文件")
                return False
        else:
            print(f"❌ 打包失败，返回码: {process.returncode}")
            return False
        
    except Exception as e:
        print(f"❌ 打包过程中出现错误: {e}")
        return False

def create_release_info(exe_file, system, arch):
    """创建发布信息文件"""
    try:
        info_content = f"""roLabelImg {system} {arch} 可执行文件
===============================================

构建信息:
- 构建时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 平台: {system} {arch}
- Python版本: {sys.version.split()[0]}

功能特性:
- ✅ 边界限制已优化，标注框可以超出图像边界
- ✅ 支持中心点在边界时调整标注框大小
- ✅ 支持普通矩形和旋转矩形标注
- ✅ 完整的快捷键支持

快捷键:
- Ctrl+B 或 O键: 切换边界限制
- W键: 创建普通矩形
- E键: 创建旋转矩形
- Ctrl+O: 打开图像
- Ctrl+S: 保存标注

使用说明:
1. 双击运行可执行文件
2. 使用"View -> Toggle Boundary Constraint"菜单或快捷键切换边界限制
3. 默认情况下边界限制已禁用，可以自由标注

注意事项:
- 首次运行可能需要几秒钟加载时间
- 如遇到杀毒软件误报，请添加到白名单
- 支持所有常见图像格式(JPG, PNG, BMP等)

版本信息:
- 基于roLabelImg项目优化版本
- 包含边界限制解除功能
- 优化了用户体验
"""
        
        info_file = os.path.join('dist', 'README.txt')
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(info_content)
        
        print(f"✅ 创建版本信息文件: {info_file}")
        
    except Exception as e:
        print(f"⚠️ 创建版本信息文件失败: {e}")

def check_dependencies():
    """检查必要的依赖"""
    required_modules = [
        ('PyQt5', 'PyQt5'),
        ('lxml', 'lxml'), 
        ('PyInstaller', 'PyInstaller')  # 正确的模块名
    ]
    missing_modules = []
    
    for display_name, module_name in required_modules:
        try:
            __import__(module_name)
            print(f"✅ {display_name} - 已安装")
        except ImportError:
            missing_modules.append(display_name.lower())
            print(f"❌ {display_name} - 未安装")
    
    if missing_modules:
        print(f"\n❌ 缺少以下依赖模块: {', '.join(missing_modules)}")
        print("请运行以下命令安装:")
        print(f"pip install {' '.join(missing_modules)}")
        return False
    
    print("✅ 所有依赖检查通过")
    return True

def create_spec_file():
    """创建.spec文件用于自定义打包"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['roLabelImg.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icons', 'icons'),
        ('data', 'data'),
        ('libs', 'libs'),
        ('resources.py', '.'),
    ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'lxml',
        'lxml.etree',
        'xml.etree',
        'xml.etree.ElementTree',
        'resources',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='roLabelImg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('roLabelImg.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("✅ 创建roLabelImg.spec文件")

def main():
    """主函数"""
    print("🏷️  roLabelImg 打包工具")
    print("=" * 50)
    
    system, arch = get_platform_info()
    print(f"🖥️  检测到平台: {system} {arch}")
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 检查是否在项目根目录
    if not os.path.exists('roLabelImg.py'):
        print("❌ 错误: 请在项目根目录下运行此脚本")
        print("   当前目录应包含roLabelImg.py文件")
        sys.exit(1)
    
    print("\n📦 打包选项:")
    print("1. 快速打包（推荐）")
    print("2. 使用spec文件打包（自定义选项）") 
    print("3. 退出")
    
    while True:
        choice = input("\n请选择打包方式 (1/2/3): ").strip()
        
        if choice == '1':
            success = build_exe()
            break
        elif choice == '2':
            print("📄 创建spec文件...")
            create_spec_file()
            
            spec_file = 'roLabelImg.spec'
            cmd = ['pyinstaller', spec_file]
            
            try:
                print(f"📦 使用spec文件打包: {spec_file}")
                subprocess.run(cmd, check=True)
                print("✅ 使用spec文件打包成功！")
                success = True
            except subprocess.CalledProcessError as e:
                print(f"❌ 打包失败: {e}")
                success = False
            break
        elif choice == '3':
            print("👋 退出打包工具")
            sys.exit(0)
        else:
            print("❌ 无效选择，请输入 1、2 或 3")
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 打包完成！")
        print("\n📋 使用说明:")
        print("- 🗂️  可执行文件在 dist/ 目录中")
        print("- 📤 可以将dist目录中的文件分发给其他用户")
        print("- 💻 双击可执行文件即可运行")
        print("- 📖 查看README.txt了解详细使用说明")
        
        if system == 'Windows':
            print("- 🛡️  Windows可能会有安全提示，请选择'仍要运行'")
        elif system == 'Darwin':
            print("- 🍎 macOS可能需要在系统偏好设置中允许运行")
        
        print(f"\n🚀 在{system}平台上生成的可执行文件可以在相同平台上运行")
        if system != 'Windows':
            print("💡 要生成Windows .exe文件，请使用GitHub Actions或在Windows机器上运行")
    else:
        print("❌ 打包失败！请检查错误信息并重试")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 用户中断，退出打包工具")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生未预期的错误: {e}")
        sys.exit(1)
