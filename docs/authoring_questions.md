
# Authoring Questions in Prairie Learn

Welcome to the Open Problem Bank (OPB) in Physics.
This repository contains the source code (including solutions) to the questions available publicly [here](https://firas.moosvi.com/oer/physicsbank).

## How to create questions on the OPB

We will be using a [Branch and Pull Request (PR)](https://guides.github.com/introduction/flow/) method to review contributions to the OPB. This method is illustrated below:

![The GitHub Flow: Branch off main, add commits, create a pull request, discuss, and then merge it in.](images/flow.png)
Image credit for the above flow is from [GitHub Guides](https://guides.github.com/pdfs/githubflow-online.pdf).

First some general guidelines:

1. Feel free to start a draft pull request while you're working on the question. When you're ready, you can click "ready for review". 

2. You should request reviews from at least two different students on the team.

3. Avoid committing anything to this repository in the `output` directory; the files in there are automatically generated with scripts in the `scripts` directory, using the `source` files.

### Links to useful places

- [Topics, Subtopics, and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv)
- [Prarie Learn Login](https://ca.prairielearn.com/pl/login)

### Using Terminal

Some useful terminal commands are listed below. For each of these commands the chevrons ("<>") and the text within must be replaced by your own text. If additional information is needed use `-help` following the command in the Terminal.

To print the absolute pathname of the working directory:
> `pwd`

To list of the contents of the working directory:
> `ls`

To change the working directory to <directory>:
> `cd <directory>`
*Note that <directory> can be an absolute pathname of the desired directory or a directory name within the working directory.*

To change the working directory to the previous working directory:
> `cd ..`

To create a new directory within the working directory named <directory>:
> `mkdir <directory>`
*Note that <directory> can be an absolute pathname of the desired directory or a directory name within the working directory.*

To copy <source_file> to <target_file>:
> `cp <source_file> <target_file>`
*Note that <source_file> and <target_file> must be the absolute pathname of the desired file (including the filename). Files can be renamed by entering a different filename for <target_file> than was specified by <source_file>. If a directory is being copied, the '-R' flag must be used to copy its contents.*

To move <source_file> to <target_file>:
> `mv <source_file> <target_file>`
*Note that <source_file> and <target_file> must be the absolute pathname of the desired file (including the filename). Files can be renamed by entering a different filename for <target_file> than was specified by <source_file>. If a directory is being moved, the '-R' flag must be used to move its contents.*

### Using GitHub

Some useful Git Commands are listed below. For each of these commands the chevrons ("<>") and the text within must be replaced by your own text. If additional information is needed use `-help` following the command in the Terminal.

To create a local copy of a remote repository:
> `git clone <url>`

To update the local repository to the newest commit:
> `git pull`

To switch branches:
> `git switch <branch_name>`
*Note that to create a new branch, use `-c` prior to <branch_name>.*

To add all new changes to the staging area:
> `git add .`

To commit changes:
> `git commit`
*Note that to add a message to the commit, use `-m "<message_text>"` at the end of the above line.*

To push changes to the remote repository:
> `git push`
*Note that if <branch_name> does not exist in the remote repository, use `--set-upstream origin <branch_name>' at the end of the above line.*

### Instructions for Authoring Questions 

For each of these commands the chevrons ("<>") and the text within must be replaced by your own text.

1. In Visual Studio Code open a Terminal by clicking: Terminal > New Terminal

2. In the Terminal, change the working directory to documents:

> `cd ~/Documents`

*Note that any other directory will suffice so long as you know what it is.*

2. Using the Terminal, create a new directory for the Open Educational Resource (OER) Project and change the working directory to the new directory:

> `mkdir OER_Project`
>
> `cd OER_Project`

3. Using the Terminal, clone the instructor physics bank repository locally and change the working directory to 'instructor_physics_bank':

> `git clone https://github.com/open-resources/instructor_physics_bank.git`
>
> `cd instructor_physics_bank`

4. Checkout a new branch (replace <new_branch_name> with your question number or description):

> `git switch -c <new_branch_name>`

*Note that the '-c' flag creates a new branch if it does not already exist.*

5. Choose a question that you want to write in markdown - take note of the source and any attribution you may need to make. Use the [Topics, Subtopics, and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv) file to get the "Topic" and "Subtopic" - you will need to put the question in the correct directory.

6. In the terminal, change the working directory to the appropriate topic and subtopic directory within the [`source`](https://github.com/open-resources/instructor_physics_bank/tree/main/source) directory and create a new subdirectory for your question:

> `cd source/<topic_directory>/<subtopic_directory>`
>
> `mkdir <new_subdirectory>` 

*Note that the directory structure follows the Topic/Subtopic scheme. If your question title is "Distance Travelled", the subdirectory name should be "distance_travelled" and the file containing the questions should be called "distance_travelled.md". If the topic of this question is "003.Kinematics(1D)" and the subtopic of this question is "Position", the final location of `distance_travelled.md` should be 'OER_Project/instructor_pysics_bank/source/003.Kinematics(1D)/Position/distance_travelled/distance_travelled.md'.*

7. Using the terminal, copy one of the question templates from the [`templates`](https://github.com/open-resources/instructor_physics_bank/tree/main/templates/source) directory into the directory you created in the two steps above. Rename the file with the question title. For our example, the new name would be `distance_travelled.md`.

> `cp ~/Documents/instructor_physics_bank/templates/source/<template_directory>/<template>.md ~/Documents/instructor_physics_bank/source/<topic_directory>/<subtopic_directory>/<question_title>.md`

8. Edit the `distance_travelled.md` file to author your question. Feel free to "commit" to the repository as many times as you like. Here are the commands to first add it to the repository, then commit the file, then push it to GitHub:

> `git add .`
> 
> `git commit -m "A message about a change you made`
> 
> `git push`

*Note that if the new branch you have created has no upstream branch, a message will appear suggesting a new command. Copy and paste this command into the Terminal:

> `git push --set-upstream origin <new_nranch_name>`*

[Here's a video of the authoring process](https://vimeo.com/554494220).

9. Create a Pull Request on GitHub.com by holding command key and clicking the link provided in the Terminal. Ask for two reviwers, then click the green button labelled "Compare and Pull Request".

10. Add the "check_syntax" label to trigger an automatic action to check the syntax of your question. Wait for the action to complete.

11. Verify the question looks and works as expected on [Prarie Learn](https://ca.prairielearn.com/pl/login). To do this, first click "Sign in with UBC" and enter your Campus Wide Login information. Then click "OPB 000: DRAFT Open Problem Bank - Physics", "Sync", and "Pull from remote git repository". Next click "Questions", find your question, and click on it's QID. To test the initialization of the question click "Settings" and "Test once with full details" or "Test 100 times with only results". Also click "Preview" and try answering a few versions of the question to ensure that the answers are correct.

12. Add the "ready_to_merge" label to mark the question as ready to merge into the OPB.

13. In the Terminal, change the working directory back to `instructor_physics_bank` and switch back to the `main` branch locally:

> `cd ~/Documents/instructor_physics_bank`
> 
> `git switch main`

14. Using the terminal, pull any changes (if there are any):

> `git pull`

15. Go back to Step 3 to start a new question!
