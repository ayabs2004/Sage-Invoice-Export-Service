@echo off
echo ========================================
echo   BUILD SAGE EXPORT - ROBUSTE
echo ========================================

echo [1/4] Fermeture des instances existantes...
taskkill /f /im SageExport.exe >nul 2>&1
timeout /t 2 /nobreak >nul

echo [2/4] Nettoyage...
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build

echo [3/4] Build PyInstaller...
pyinstaller --clean SageExport.spec

echo [4/4] Verification...
if exist "dist\SageExport.exe" (
    echo Build reussi !
    copy "dist\SageExport.exe" ".\SageExport.exe" /y
) else if exist "dist\SageExport.exe.notanexecutable" (
    echo Rename fallback...
    move "dist\SageExport.exe.notanexecutable" "dist\SageExport.exe"
    copy "dist\SageExport.exe" ".\SageExport.exe" /y
    echo Build recupere !
) else (
    echo Echec du build.
    exit /b 1
)
echo TERMINE.
