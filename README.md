# DFEND_work
Follow the steps below for managing your work this year:
  1. install git
  2. Up in the top right corner of the DFEND_work page, you will see a button that says "Fork" with a number next to it. Click this button. Rename the fork to [FirstName_LastName_DFEND_work]. This will create a forked copy of the repo in your personal Github space.
  3. Create a folder on your laptop in your documents folder called "DFEND_work"
  4. Go to the Github page for your forked repo (the one with your name) and click the green "Code" button
  5. copy the URL for "Clone with HTTPS"
  6. open a command prompt/git bash terminal/etc in the "DFEND_work" folder you made in your documents folder.
  7. type git clone and then past the URL you copied from your forked repo. It should look something like git clone https://github.com/YOUR-USERNAME/FirstName_LastName_DFEND_work. If it doesn't have the name of your fork, you're cloning the wrong repo. Go back and make sure you're copying the URL for your forked repo, NOT the baseline DFEND-work repo.
  8. You may be prompted to authenticate. Choose the "browser" option. This will open a browser window. Log in with your username and password and click the green button for Github credential manager.
  9. Download the files for the challenge you are interested in working on and extract it into the DFEND_work folder you made earlier. See refined_github.txt in this repo for some tips on how to make this significantly easier to do.
  10. Use the git add command to add the challenge files to the cloned DFEND_work repo
  11. run the following commands, filling the placeholders with your information. 
  12.  git config --global user.email "you@example.com"
  13.  git config --global user.name "your github username"
  14. Use the git commit command to commit these files to your personal DFEND_work repo. Note, you will need to use git commit -m "COMMIT MESSAGE HERE" [filenames here] when you commit, with your first commit message being something like "initial challenge file commit".
  15. Use git push to push all files up to your forked DFEND_work repo. 
  16. Congratulations! Now you can start working on the challenge. Any additional files you create, including (preferably) some kind of notes file, should be added to your repo using the same git add/git commit/git push process outlined above. Anything you'd like to keep personal you can store elsewhere, or simply don't git add it to the repo and it will not be pushed.
  17. **The expectation this year is that you will commit something nightly to your DFEND work repo, even if it's two sentences in a text file summarizing the things you've worked on, experimented with, or tested that day.**

We understand that this will be a new workflow for some and will be challenging initially. However, git plays a big role in many jobs in the cybersecurity field, so take this opportunity to make mistakes and learn. We are available to help you with any questions you may have.
