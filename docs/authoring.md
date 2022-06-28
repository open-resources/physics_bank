# Authoring a markdown question

This guide specifically applies to `.md` files which will be converted to the PrairieLearn (PL) format and uploaded to PL.
The file will be converted to the public version and be uploaded to the public version of the Open Problem Bank.

## Video Resources

### Introduction

- [Video 1 - Next Generation Problem Bank](https://vimeo.com/559780900)
- [Video 2 - Introduction to Prairie Learn](https://vimeo.com/554493760)
- [Video 3 - Authoring questions for Prairie Learn in Markdown](https://vimeo.com/554494220)

### Authoring Questions Details

- [Video 1 - Overview of Creating PL problems](https://www.youtube.com/watch?v=hFYwxmLDORw&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wamz)
- [Video 2 - Randomizing and solving physics problem in Python](https://www.youtube.com/watch?v=CCnc7bspuZg&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wam&index=2)
- [Video 3 - Writing a Markdown file for a numerical-entry problem](https://www.youtube.com/watch?v=ZoZYZlmvh_Y&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wam&index=3)
- [Video 4 - Fully implemented numeric entry problem](https://www.youtube.com/watch?v=ujCbACEbizA&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wam&index=4)
- [Video 5 - Wrting a symbolic PL problem](https://www.youtube.com/watch?v=P0sK1WS2p98&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wam&index=5)
- [Video 6 - Making a multi-part problem](https://www.youtube.com/watch?v=ftPXBcMCROc&list=PLfhjdV-pwMOa7HeYtI4Qd9QRMPfv77Wam&index=6)

## Overview of the steps for authoring questions

This is an overview of the steps you need to follow to author each question once you have completed the initial setup.

1. Make a `new branch` for each new question.
2. Create a `new directory` in the source folder under your topic or subtopic.
3. Crate your `markdown file` in the folder and add any `assets` such as images being used for your question.
4. Copy the markdown `template` according to your question and start editing.
5. `Add`, `commit` and then `push` to the Github repository.
6. Create a pull request and add 1 or 2 reviewers to approve your work.
7. Add a `syntax check` label on Github and make sure it passes to go and take a look at the question on [PrairieLearn](https://ca.prairielearn.org/pl/course_instance/2320/instructor/course_admin/questions). Fix errors if you notice any.
8. Keep fixing the questions using feedback from reviewiers and once ready, add the `ready_to_merge` label for a final review before the branch merges into `main`.

## General guidelines for the workflow of authoring questions

1. We will be using a [Branch and Pull Request (PR)](https://guides.github.com/introduction/flow/) method to review contributions to the OPB.

![The GitHub Flow: Branch off main, add commits, create a pull request, discuss, and then merge it in.](images/flow.png)
Image credit for the above flow is from [GitHub Guides](https://guides.github.com/pdfs/githubflow-online.pdf).

2. Feel free to start a draft pull request while you're working on the question. When you're ready, you can click "ready for review". 

3. You should request reviews from at least one or two different students on the team.

*Avoid committing anything to this repository in the `output` directory; the files in there are automatically generated with scripts in the `scripts` directory, using the `source` files.*

## Detailed steps for authoring questions

This is a detailed guide to author the questions. Including a first few steps for setting up the environment and the Github repository on your local machine.

1. Using the Terminal on your computer, clone this repository locally (i.e. on your computer)

> `git clone https://github.com/open-resources/instructor_physics_bank.git`

2. Change directory into the `instructor_physics_bank`

> `cd instructor_physics_bank`

3. Make a new branch for your question with an appropriate name (replace `newbranchname` with your question number or description)

> `git checkout -b newbranchname`

4. Create a new directory with your question's name in the `source/YourTopic/QuestionTitle` or `source/YourTopic/YourSubtopic/QuestionTitle` directory to store your markdown file and any assets (usually images) associated with it. Use the [Topics, Subtopics, and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv) file to get the "Topic" and "Subtopic" - you will need to put the question in the correct directory.

*Note that the directory structure follows the Topic/Subtopic scheme.*

*If your question title is "Distance Travelled", the equivalent directory name is "distance_travelled" and the file containing the questions should be called "distance_travelled.md".*

*So the final location of the `distance_travelled.md` should be:*

> `source/003.Kinematics(1D)/Position/distance_travelled/distance_travelled.md`

5. Create your markdown file in your created folder and copy the format from one of the [templates](https://github.com/open-resources/instructor_physics_bank/tree/main/templates).It seems the best way to do this is to copy and paste the file, and then rename it. For our example, that would be the `distance_travelled.md` file.

6. Edit the `distance_travelled.md` file to author your question. Feel free to "commit" to the repository as many times as you like. Here are the commands to first add it to the repository, then commit the file, then push it to GitHub:

> `git add source/003.Kinematics(1D)/Position/`
> `git commit -m "A message about a change you made`
> `git push`.

7. Create a `Pull Request` and ask for two reviewers by logging into GitHub.com; you will see a green button called "Compare and Pull Request".

8. Add the `syntax check` label on GitHub to trigger an automatic action to check the syntax of your question and make sure it passes; fix any errors if it does not.

9. If the syntax check passes, go to [PrairieLearn](https://ca.prairielearn.org/pl/course_instance/2320/instructor/course_admin/questions) and to [Public version of the OPB](https://firas.moosvi.com/oer/physicsbank) to check if it looks as desired. Make any changes necessary to fix if not.

10. Add the `ready_to_merge` label to mark for final review.

11. Swtich back to the `main` branch locally using:
> `git checkout main`

12.  Perform `git pull` for any changes made.

Go back to step 3 to author a new question!

