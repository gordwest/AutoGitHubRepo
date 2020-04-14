#!/bin/bash

function create(){
    cd
    python "/mnt/c/Users/gordi/Desktop/CODE/GitHub/AutoGitHubRepo/create.py" $1
    cd "/mnt/c/Users/gordi/Desktop/CODE/GitHub/$1"
    git init
    touch README.md
    git add .
    git commit -m 'Initial commit'
    git remote add origin https://github.com/gordwest/$1.git
    git push -u origin master
    code .
    
}