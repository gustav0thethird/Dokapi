@echo off
:: Set buffer size
mode con: cols=100 lines=30

:: Set actual window size (for newer Windows Terminals)
powershell -command "& { [console]::WindowWidth=100; [console]::WindowHeight=30 }"

:: Clear junk
cls

:: Launch the Python app
python dokapi_shell.py

pause
