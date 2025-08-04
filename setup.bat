@echo off
echo Starting TherapyHub...
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Running TherapyHub application...
python app.py

pause
