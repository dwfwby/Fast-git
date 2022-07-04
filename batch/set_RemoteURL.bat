@echo off
set git="%~dp0..\git\bin\git.exe"
cd /d %1
%git% init
%git% remote remove origin
%git% remote add origin %2