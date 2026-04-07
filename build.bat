@echo off
echo ============================================
echo Hinglish STT - Build Offline App
echo ============================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -q pyinstaller transformers torch accelerate streamlit scipy

REM Create assets directory
if not exist "assets" mkdir assets

REM Download model to cache
echo.
echo NOTE: The AI model (~3GB) will be downloaded on first run.
echo It will be cached in your HuggingFace cache folder.
echo.

REM Build with PyInstaller
echo Building executable...
pyinstaller --onefile --windowed --name HinglishSTT ^
    --add-data "app.py;." ^
    --add-data "stt_hinglish.py;." ^
    --hidden-import=transformers ^
    --hidden-import=torch ^
    --hidden-import=accelerate ^
    --hidden-import=streamlit ^
    --hidden-import=scipy ^
    --hidden-import=stt_hinglish ^
    --collect-all=transformers ^
    --collect-all=torch ^
    --exclude-module=tensorflow ^
    --exclude-module=keras ^
    --exclude-module=matplotlib ^
    --exclude-module=pandas ^
    --noconfirm

echo.
echo ============================================
echo Build Complete!
echo ============================================
echo.
echo The executable is in: dist\HinglishSTT.exe
echo.
echo First run: Double-click HinglishSTT.exe
echo The model will download automatically on first run.
echo.

pause
