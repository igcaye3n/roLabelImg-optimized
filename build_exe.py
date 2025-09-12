#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
roLabelImg打包脚本
使用PyInstaller将roLabelImg打包成可执行文件
"""

import os
import sys
import subprocess
import shutil

def build_exe():
    """打包roLabelImg为可执行文件"""
    
    print("🚀 开始打包roLabelImg...")
    
    # 清理旧的构建文件
    if os.path.exists('build'):
        shutil.rmtree('build')
        print("✅ 清理build目录")
    
    if os.path.exists('dist'):
        shutil.rmtree('dist')
        print("✅ 清理dist目录")
    
    # PyInstaller命令参数
    cmd = [
        'pyinstaller',
        '--onefile',  # 打包成单个文件
        '--windowed',  # 无控制台窗口（GUI应用）
        '--name=roLabelImg',  # 可执行文件名
        '--icon=icons/app.ico' if os.path.exists('icons/app.ico') else '',  # 图标
        '--add-data=icons:icons',  # 包含图标文件夹
        '--add-data=data:data',  # 包含数据文件夹
        '--hidden-import=PyQt5',
        '--hidden-import=PyQt5.QtCore',
        '--hidden-import=PyQt5.QtGui', 
        '--hidden-import=PyQt5.QtWidgets',
        '--hidden-import=lxml',
        '--hidden-import=lxml.etree',
        'roLabelImg.py'
    ]
    
    # 移除空的icon参数
    cmd = [arg for arg in cmd if arg]
    
    try:
        print("📦 开始PyInstaller打包...")
        print(f"命令: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("✅ 打包成功！")
        print(f"可执行文件位置: {os.path.abspath('dist/roLabelImg')}")
        
        # 检查文件是否存在
        if os.path.exists('dist/roLabelImg'):
            file_size = os.path.getsize('dist/roLabelImg') / (1024 * 1024)  # MB
            print(f"文件大小: {file_size:.2f} MB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 打包失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ 打包过程中出现错误: {e}")
        return False

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
    ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'lxml',
        'lxml.etree',
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

if __name__ == '__main__':
    print("roLabelImg 打包工具")
    print("=" * 50)
    
    # 检查依赖
    try:
        import PyQt5
        import lxml
        print("✅ 依赖检查通过")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        sys.exit(1)
    
    # 选择打包方式
    choice = input("选择打包方式:\n1. 快速打包（推荐）\n2. 使用spec文件打包\n请输入选择 (1/2): ").strip()
    
    if choice == '2':
        create_spec_file()
        cmd = ['pyinstaller', 'roLabelImg.spec']
        try:
            subprocess.run(cmd, check=True)
            print("✅ 使用spec文件打包成功！")
        except subprocess.CalledProcessError as e:
            print(f"❌ 打包失败: {e}")
    else:
        build_exe()
    
    print("\n📋 打包完成说明:")
    print("- 可执行文件在 dist/ 目录中")
    print("- 可以将整个dist目录分发给其他用户")
    print("- 在Windows上运行需要相应的可执行文件")
