@echo off
echo ========================================
echo roLabelImg Windows EXE Builder
echo ========================================

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Error: Python not found! Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo Installing required packages...
pip install PyQt5 lxml pyinstaller

echo Building executable...
pyinstaller --onefile --windowed ^
  --name=roLabelImg ^
  --add-data="icons;icons" ^
  --add-data="data;data" ^
  --add-data="libs;libs" ^
  --add-data="resources.py;." ^
  --hidden-import=PyQt5 ^
  --hidden-import=PyQt5.QtCore ^
  --hidden-import=PyQt5.QtGui ^
  --hidden-import=PyQt5.QtWidgets ^
  --hidden-import=lxml ^
  --hidden-import=resources ^
  --exclude-module=tkinter ^
  --exclude-module=matplotlib ^
  roLabelImg.py

if exist "dist\roLabelImg.exe" (
    echo ========================================
    echo Success! roLabelImg.exe created in dist folder
    echo File size:
    for %%I in ("dist\roLabelImg.exe") do echo %%~zI bytes
    echo ========================================
    echo.
    echo The executable is ready to use!
    echo Location: %cd%\dist\roLabelImg.exe
    echo.
    echo You can now:
    echo 1. Run the executable directly
    echo 2. Copy it to any Windows computer
    echo 3. No Python installation required on target machines
    echo.
) else (
    echo ========================================
    echo Error: Failed to create executable!
    echo Please check the error messages above.
    echo ========================================
)

pause
