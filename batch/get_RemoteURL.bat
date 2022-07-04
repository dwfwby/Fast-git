@echo off
set git="%~dp0..\git\bin\git.exe"
cd /d %1
%git% remote get-url origin