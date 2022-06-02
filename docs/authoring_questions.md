
# Authoring Questions in Prairie Learn

Welcome to the Open Problem Bank (OPB) in Physics.
This repository contains the source code (including solutions) to the questions available publicly [here](https://firas.moosvi.com/oer/physicsbank).

## How to create questions on the OPB

First some general guidelines:

1. We will be using a [Branch and Pull Request (PR)](https://guides.github.com/introduction/flow/) method to review contributions to the OPB.

![The GitHub Flow: Branch off main, add commits, create a pull request, discuss, and then merge it in.](images/flow.png)
Image credit for the above flow is from [GitHub Guides](https://guides.github.com/pdfs/githubflow-online.pdf).

1. Feel free to start a draft pull request while you're working on the question. When you're ready, you can click "ready for review". 

1. You should request reviews from at least two different students on the team.

1. Avoid committing anything to this repository in the `output` directory; the files in there are automatically generated with scripts in the `scripts` directory, using the `source` files.

### Links to useful places

- [Topics, Subtopics, and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv)
- [Public version of the OPB](https://firas.moosvi.com/oer/physicsbank)

### Instructions

1. Using the Terminal on your computer, clone this repository locally (i.e. on your computer):

> `git clone https://github.com/open-resources/instructor_physics_bank.git`

2. Change directory into the `instructor_physics_bank`:

> `cd instructor_physics_bank`

3. Checkout a new branch (replace `newbranchname` with your question number or description):

> `git switch -c newbranchname` (the `-c` flag creates a new branch if it does not already exist)

4. Choose a problem that you want to write in markdown, take note of the source, and any attribution you may need to make. Use the [Topics, Subtopics, and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv) file to get the "Topic" and "Subtopic" - you will need to put the question in the correct directory.

5. Create a subdirectory for the question you want to create inside the [`source`](https://github.com/open-resources/instructor_physics_bank/tree/main/source) directory.

*Note that the directory structure follows the Topic/Subtopic scheme.*

*If your question title is "Distance Travelled", the equivalent directory name is "distance_travelled" and the file containing the questions should be called "distance_travelled.md".*

*So the final location of the `distance_travelled.md` should be:*

> `source/003.Kinematics(1D)/Position/distance_travelled/distance_travelled.md`

6. Copy one of the question templates from the [templates](https://github.com/open-resources/instructor_physics_bank/tree/main/templates) directory into the directory you created in the two steps above. It seems the best way to do this is to copy and paste the file, and then rename it. For our example, that would be the `distance_travelled.md` file.

7. Edit the `distance_travelled.md` file to author your question. Feel free to "commit" to the repository as many times as you like. Here are the commands to first add it to the repository, then commit the file, then push it to GitHub:

> `git add source/003.Kinematics(1D)/Position/`
> 
> `git commit -m "A message about a change you made`
> 
> `git push`.

[Here's a video of the authoring process](https://vimeo.com/554494220).

8. Create a Pull Request and ask for two reviewers by logging into GitHub.com; you will see a green button called "Compare and Pull Request".

9. Add the `syntax check` label to trigger an automatic action to check the syntax of your question. Wait for the action to complete.

10. Verify the question looks and works as expected on [PrairieLearn](https://ca.prairielearn.org/pl/course_instance/2320/instructor/course_admin/questions).

11. Verify the question looks as expected on the [Public version of the OPB](https://firas.moosvi.com/oer/physicsbank).

12. Add the `final review` label to mark the question as ready to merge into the OPB.

13. Switch back to the `main` branch locally:

> `git switch main`

14. Pull any changes (if there are any):

> `git pull`

15. Go back to Step 3 to start a new question!
