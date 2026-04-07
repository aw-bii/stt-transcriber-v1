@echo off
chcp 65001 >nul
echo ============================================
echo   Hinglish STT - Build Offline App
echo ============================================
echo.

REM Get script directory
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.9+ from python.org
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Install dependencies
echo [1/3] Installing dependencies...
echo This may take 5-10 minutes on first run...
echo.

pip install -q pyinstaller transformers torch accelerate streamlit scipy

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.

REM Create assets folder
if not exist "assets" mkdir assets

REM Build executable
echo [2/3] Building executable...
echo This may take 10-20 minutes...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

REM Build with PyInstaller
pyinstaller build_app.spec --noconfirm

if errorlevel 1 (
    echo [ERROR] Build failed!
    echo Check the error messages above.
    pause
    exit /b 1
)

echo.
echo [3/3] Build complete!
echo.

echo ============================================
echo   BUILD SUCCESSFUL
echo ============================================
echo.
echo Executable location:
echo   dist\HinglishSTT\HinglishSTT.exe
echo.
echo Run the app:
echo   dist\HinglishSTT\HinglishSTT.exe
echo.
echo First run: App will open in browser at localhost:8501
echo The AI model (~3GB) will download automatically.
echo.
echo IMPORTANT: Keep the executable folder intact.
echo Do not move just the .exe file alone.
echo.

pause
