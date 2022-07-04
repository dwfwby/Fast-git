@echo off
set clone_link=%2
set git="%~dp0..\git\bin\git.exe"
cd /d %1
echo %git%
%git% clone %2 .