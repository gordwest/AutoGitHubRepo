@echo off

If "%1"=="" (
    echo "Enter a project name!"
) 
else ( 
    python "C:/Users/gordi/Desktop/CODE/GitHub/AutoGitHubRepo/create.py" %1
)