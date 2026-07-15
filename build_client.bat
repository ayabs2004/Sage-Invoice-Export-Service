@echo off
echo.
echo ========================================
echo   BUILD SAGE CLIENT - EXECUTABLE
echo ========================================
echo.

echo [1/3] Nettoyage...
if exist "build" rmdir /s /q build
if exist "dist\SageClient.exe" del /q dist\SageClient.exe
if exist "SageClient.exe" del SageClient.exe

echo.
echo [2/3] Construction du Client Light...
pyinstaller --clean SageClient.spec

echo.
echo [3/3] Finalisation...
if exist "dist\SageClient.exe" (
    rmdir /s /q build
    echo.
    echo BUILD TERMINE: SageClient.exe est prêt!
) else (
    echo ERREUR LORS DU BUILD!
)


