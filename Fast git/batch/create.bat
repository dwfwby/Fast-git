@echo off
set gitCLI="%~dp0..\gitCLI\gh.exe"
set git="%~dp0..\git\bin\git.exe"
%gitCLI% auth login --with-token "< secret_token"
%gitCLI% repo create "%1" --private
