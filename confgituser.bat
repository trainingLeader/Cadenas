@echo off
SETLOCAL EnableDelayedExpansion
set condition=true
git config --global user.name "trainingLeader" 
git config --global user.email "131613955+trainingLeader@users.noreply.github.com"
git config --global core.editor “code --wait”
git config --global init.defaultBranch main
ENDLOCAL