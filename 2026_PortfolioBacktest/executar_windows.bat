@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  set PYTHON=py
) else (
  where python >nul 2>nul
  if %errorlevel% neq 0 (
    echo Python nao encontrado. Instale Python 3.10 ou superior e marque "Add Python to PATH".
    pause
    exit /b 1
  )
  set PYTHON=python
)

if not exist .venv (
  echo Criando ambiente virtual...
  %PYTHON% -m venv .venv
  if %errorlevel% neq 0 goto :erro
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if %errorlevel% neq 0 goto :erro
pip install -r requirements.txt
if %errorlevel% neq 0 goto :erro
python download.py
if %errorlevel% neq 0 goto :erro

echo.
echo Concluido. Veja a pasta output.
pause
exit /b 0

:erro
echo.
echo Ocorreu um erro. Consulte output\log.txt, se ele tiver sido criado.
pause
exit /b 1