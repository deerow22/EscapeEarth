
# FOR FILES ON GOOGLE COLAB

main google [colab webpage](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiGuLzqkpfsAhU9lHIEHZZsDCwQFjAAegQIBhAD&url=https%3A%2F%2Fcolab.research.google.com%2F&usg=AOvVaw3A5aPK2kLFzKOzb6sOckVw)

## _to create a new colab notebook_

1. go to your google drive webpage
2. double click the `EE-notebooks-YOURNAME` folder
3. click `+ New` on the top of the left side bar
4. at the bottom of the pop-up menu select `More`-->`Google Colaboratory`
5. click on the name of the notebook and rename descriptively


## _to open a colab notebook from a previous session_

1. go to google drive website
2. press the `control`key and click on your `EE-notebooks-YOURNAME` folder
3. on the popup menu select `Open with`-->`Google Colaboratory`


## _to open a notebook pulled from the MAIN EscapeEarth repo_

1. go to the main google colab webpage
2. on the pop-up menu select the `GitHub` tab
3. enter the url for your FORKED EscapeEarth repo in the `Enter a GitHub URL or search by organization or user` section
4. press `Enter` or click the 'search' icon
5. make sure you select the correct repository & branch
6. click on the name of the notebook you want to open
note: when running cells you may get a "Warning: This notebook was not authored by Google."--click `RUN ANYWAY`


## _to add a notebook to your FORKED EscapeEarth repo_

note: colab notebooks will autosave
1. On the top webpage menu bar click `File`
2. In the drop down menu click on `Save a copy in GitHub`
3. If pop-up blockers are on, you will get a message to turn them off -turn them off, then click `try again`
4. Enter the url for your FORKED EscapeEarth repo, press `Enter` or click the 'search' icon 
5. Make sure you select the correct repository & branch
6. ADD `Interns/YOURNAME/` (replace `YOURNAME` with your first name) in front of the notebook name listed under `File path`
7. Change the `Commit message` to describe the version of or changes made to the notebook
8. Click `OK`
9. Verify your changes by checking your FORKED EscapeEarth repo on the GitHub website


# ########################################################

# FOR FILES ON YOUR COMPUTER


## _to add a file to your FORKED EscapeEarth repo_

1. open terminal & `cd` to the folder where your notebook is
2. type `git status` this will list all the files that git is tracking for you and their status
3. type `git add path/filename.ipynb` (replace filename with the name of your notebook, add path as well if necessary)
4. type `git status` now you should see the file you added in green, it is now staged to commit
5. type `git commit -m 'make a comment here in quotes describing file version/changes you made'` 
6. type `git status` look for the comment that says your branch is ahead of the origin/master, this confirms the file was committed
7. type `git push origin main` this pushes the file commit to the git hub website VERY IMPORTANT!


## _to download (pull) files that have changed in our MAIN EscapeEarth repo_

1. open terminal & `cd` into the folder EscapeEarth 
2. type `git status` and check for the message `Your branch is up to date with 'origin/main'.`
3. if you are not up to date type `git pull upsteam main`


## _to pull files from your FORKED EscapeEarth repo (usually done if we pushed file from google colab first)_
1. open terminal & `cd` into the folder EscapeEarth
2. type `git pull`





# HANDLING MERGE CONFLICTS

### _if you forget to pull before you push something this can happen_

1. git on the command line will tell you about a merge conflict -- EXAMINE THIS CAREFULLY: if conflict is due to missing files, proceed below; if conflict is due to different versions of the same file - tell me, we'll need an individual solution
2. emacs will open within the terminal window asking for a reason the merge is needed
3. type a "message" that explains what caused the merge conflict
4. press the `control` and `x` keys simultaneously (this saves your message)
5. press the `control` and `c` keys simultaneously (this exits emacs & returns the window)
6. type `git pull` to pull the missing files 
7. type `git status` to verify you are not up-to-date. i.e. you should see something like this: `Your branch is ahead of 'origin/main' by 2 commits.`
8. type `git push` to finish your original commit