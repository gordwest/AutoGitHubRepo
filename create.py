import sys, os
from github import Github
from config import creds

# get arg from terminal command
projName = str(sys.argv[1])
path = "/Users/gord/Documents/Code/Projects/"

commands = ['touch README.md',
            'git init',
            'git remote add origin https://github.com/gordwest/{}.git'.format(projName),
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

# create new folder
try:
    os.mkdir(path + projName) # if folder creation succeeds, continue

    # create new repository on github 
    user = Github(creds['username'], creds['password']).get_user() # login into github
    repo = user.create_repo(projName)
    print('Successfully created repository {}'.format(projName))

    # change dir to new porject folder
    os.chdir(path + projName)

    # perform git commands
    for c in commands:
        os.system(c)

    print('{} created locally'.format(projName))

except OSError:
    print ("Creation of the folder: {} failed, this project already exists.".format(projName))

    
    