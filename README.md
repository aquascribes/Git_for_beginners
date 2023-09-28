# time_window
Python code to display a clock window on your machine & in process learn about different git commands for beginners
Installation of git in MacOS using homebrew (https://brew.sh/)
Following is the list of handy git commands : 
  1. install git : to install git in MacOS
  2. git --version : to check version of your git in the machine
  3. git config --global user.name " your username" : configuration required after first installation (username for git)
  4. git config --global user.email " your email" : your email id for git account
  5. git config --global core.editor "code" : name of the code editor you are using e.g VS CODE , here written as code. Open command pallette in VS code and search for code path command and run it 
  6. git config --list : to list the config details
  7 .git init: After you create a folder in your local machine, use this command to initialize git in this for tracking & version control
  8. git add /your filename/ : adding a file in the folder using terminal
  9. git status : to check status of different files & commits in git folder
  10. git log : to check log of all actions taken so far
  11. git log --oneline : to display log in one line
  12. git branch branchname : to create a branch named branchname to keep your code edits away from main/master branch.always test new code in branch and then merge it to the master
  13. git commit -m "message" : to commit a file to git with message
  14. git add . : add files or changes to git after you are making changes in code on your VS code editor
  15. code yourfilename.py : In VS Code open the filename named yourfilename.py
  16. git merge yourbranchname : if you are satisfied with the newly added code or improvemnt then you can merge the branch with main
  17. git reset commitnumber: it resets your git version to the commitnumber you suggest
  18. git checkout commitnumber : it takes u to the commit number suggeseted.(going to a particular stage or head)
  19. git remote add origin https://github.com/aquascribes/time_window.git : to add a  online github repository connected to ur local machine
  20. git push -u origin main (https://github.com/aquascribes/time_window/assets/79290133/79f83dbc-d110-4d4c-b261-792a40304b3b) : (to push chnages from local machine to onlien github, origin is the remote/online github & main.master is the master file created in locak machine)
 21.  When pushing files to github, they ask for your username & passowrd auth details. For that you have to downlaod a 
      personal access token key from delevoper tools
 22.  git clone "github url of project your want to clone" : This downloads the github online project to your folder
 23.  HOW TO COLLABORATE ON A PROJECT you dont have access to : We need to first fork the project (which essentially copies the original file to your github account, then you can downlaod it to your local machine, then you can edit/work on it..ideally using a branch, and then push the changes to your github account. Then to merge the changes to the original poster account, you do a 'pull request'. 
  . # SOME  TERMINAL COMMANDS
  1. ls : to list all filenames in a folder
  2. ls -a : to list hidden files in a folder
  3. cd : change directoty
  4. cd.. : go to root directory
  5. mkdir: make a folder or directory
  6. python3 filename.py : to run filename.py from terminal
  7. 

