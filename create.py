import sys, os
from github import Github
from config import creds

# get arg from terminal command
projName = str(sys.argv[1])
path = "/mnt/c/Users/gordi/Desktop/CODE/GitHub/"

# create new folder
try:
    os.mkdir(path + projName)
except OSError:
    print ("Creation of the folder: {} failed, this project already exists.".format(path, projName))
else:
    # create new repository on github 
    user = Github(creds['username'], creds['password']).get_user() # login into github
    repo = user.create_repo(projName)
    print('Successfully created repository {}'.format(projName))
