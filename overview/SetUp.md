# Setting up our GitHub Repositories


1. Log into GitHub on your browser, and navigate to [https://github.com/deerow22/EscapeEarth](https://github.com/deerow22/EscapeEarth) This will be our main project repository.
2. On the right of the window click on the "Fork" button. This will be your FORKED EscapeEarth repository. It is a new copy of the main repo.

![fork a repo](https://github.com/deerow22/EscapeEarth/blob/main/photos/fork_repo.png)

3. Open Terminal. Use the `cd` command to navigate to your Desktop.
4. Use the `mkdir` command to create a new directory called "Internship". i.e. type `mkdir Internship`
5. Use the `cd` command to navigate into this Internship folder. (Keep the Terminal window open)
6. On your FORKED repo webpage click the green button on the right that says "Code". Copy the URL shown. WARNING: Make sure this url does NOT contain "deerow22" - that means you are not using your FORKED repo.

![clone repo url](https://github.com/deerow22/EscapeEarth/blob/main/photos/clone_url.png)

7. Going back to your Terminal window use `pwd` to verify you are in the correct location: "Desktop/Internship"
8. Type `git clone <url>` where `<url>` is replaced with your copied url
CONGRATS!!  you have completed forking a repository
But we still need to set up a remote so you can pull new content from the main repo but also push to your FORKED repo
9. Use the `ls` command to see the newly cloned "EscapeEarth" folder
10. Use the `cd` command to navigate into the EscapeEarth folder
11. Type `git remote add upstream <main url>` where `<main url>` is replaced by the url for our main project repo - See step 1.
12. Going back to the GitHub website open your FORKED repo webpage and copy the url - see step 6.
13. On your FORKED repo, click the "Settings" tab
14. On the left side menu, click on "Manage Access" - it may open a page asking you to sign in again, sign in

![add collaborator](https://github.com/deerow22/EscapeEarth/blob/main/photos/add_collaborator.png)

15. At the bottom of the page you will see a green button sayings "Invite a collaborator" - click it
16. In the pop-up window type "deerow22" (without quotes). My photo should display as shown in the pic below. Click on my username.

![add me](https://github.com/deerow22/EscapeEarth/blob/main/photos/add_me.png)

17. Click the green button saying "Add deerow22 to this repository"
18. Going back to your Terminal window, type `git pull upstream main`
CONGRATS!! We have successfully connected our main & your forked repos to your local computer!



# Setting up our Google Colab structure


1. go to the main google drive website and sign in
2. click "+ new"-->Folder
3. name the new folder "EE-notebooks-YOURNAME" with YOURNAME replaced to your first name
4. double click this new folder
5. click `+ New` on the top of the left side bar
4. at the bottom of the pop-up menu select `More`-->`Google Colaboratory`
5. click on the name of the notebook and rename this notebook "Cheers-Challenges-function"

