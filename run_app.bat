@echo off
echo.
echo ========================================
echo   Resume Category Predictor
echo   Streamlit Application Launcher
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import streamlit, pandas, numpy, sklearn" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo Checking model files...
if not exist "tfidf.pkl" (
    echo ERROR: tfidf.pkl not found
    pause
    exit /b 1
)
if not exist "clf.pkl" (
    echo ERROR: clf.pkl not found
    pause
    exit /b 1
)
if not exist "encoder.pkl" (
    echo ERROR: encoder.pkl not found
    pause
    exit /b 1
)

echo.
echo Starting Streamlit application...
echo The app will open in your default web browser
echo URL: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run streamlit_app.py --server.port 8501

pause
