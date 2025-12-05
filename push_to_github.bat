@echo off
REM Quick GitHub Push Script for Questions
REM Replace YOUR_USERNAME with your actual GitHub username

cd "c:\Users\DEll\Desktop\3000 question"

echo.
echo =========================================
echo  3050 Programming Questions to GitHub
echo =========================================
echo.

echo Checking git status...
git status

echo.
echo To push to GitHub, run these commands:
echo.
echo 1. Add remote (do this once):
echo    git remote add origin https://github.com/YOUR_USERNAME/3000-programming-questions.git
echo.
echo 2. Rename branch to main:
echo    git branch -m main
echo.
echo 3. Push all questions:
echo    git push -u origin main
echo.
echo =========================================
echo After pushing, verify at:
echo https://github.com/YOUR_USERNAME/3000-programming-questions
echo =========================================
echo.
pause
