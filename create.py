import sys, os
from github import Github
from config import creds

# get arg from terminal command
projName = str(sys.argv[1])
path = "C:/Users/gordi/Desktop/Code/Projects/"

commands = [f'echo # {projName} >> README.md',
            'git init',
            f'git remote add origin https://github.com/gordwest/{projName}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

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

    # change dir to new porject folder
    os.chdir(path + projName)

    # perform git commands
    for c in commands:
        os.system(c)

    print(f'{projName} created locally')
    os.system('code .')
    