@echo off
REM ========================================
REM Script de Build pour Sage Export
REM ========================================

echo.
echo ========================================
echo   BUILD SAGE EXPORT - EXECUTABLE
echo ========================================
echo.

REM Vérifier si PyInstaller est installé
echo [1/4] Verification de PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller n'est pas installe. Installation en cours...
    pip install pyinstaller
) else (
    echo PyInstaller est deja installe.
)

echo.
echo [2/4] Nettoyage des anciens builds...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "SageExport.exe" del SageExport.exe

echo.
echo [3/4] Construction de l'executable...
echo Cela peut prendre quelques minutes...
pyinstaller --clean SageExport.spec

echo.
echo [4/4] Finalisation...
if exist "dist\SageExport.exe" (
    rmdir /s /q build
    echo.
    echo ========================================
    echo   BUILD TERMINE AVEC SUCCES!
    echo ========================================
    echo.
    echo Fichier cree: SageExport.exe
    echo.
    echo PROCHAINES ETAPES:
    echo 1. Testez l'executable avec: SageExport.exe
    echo 2. Creez un dossier de distribution avec:
    echo    - SageExport.exe
    echo    - .env.example (a renommer en .env chez le client)
    echo    - GUIDE_INSTALLATION.txt
    echo.
) else (
    echo.
    echo ========================================
    echo   ERREUR LORS DU BUILD!
    echo ========================================
    echo Verifiez les messages d'erreur ci-dessus.
    echo.
)


