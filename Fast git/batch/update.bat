@echo off
set git="%~dp0..\git\bin\git.exe"
cd /d %1
%git% add .
%git% commit --allow-empty-message -m ''
%git% push %2