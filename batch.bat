@echo off
Echo Deleting files older than 14 days...
cd /d C:\Windows\System32
copy /b forfiles.exe "[file path...]\IDOC_ARCHIVE" >nul
FORFILES /P "[C:\Windows\Temp]\IDOC_ARCHIVE" /M *.* /D -14 /C "cmd /c del @file"

rem Forfiles /p "" /s /m *.* -d -1 /c "cmd /c del /q @path"

rem Forfiles /p "C:\Windows\Temp" /s /m *.* -d -1 /c "cmd /c del /q @path"
