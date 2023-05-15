# Prairie Learn System workflow

The markdown files that are created to author questions are then parsed by a function in [problem_bank_scripts](https://github.com/open-resources/problem_bank_scripts). The function creates the correct format in which the question should be uploaded to PrairieLearn to be able to correctly be randomised and displayed.

Your markdown files are sent to PrairieLearn when you add the `syntax check` label to it in your pull request. This triggers a Github action which makes `problem_bank_scripts` parse your question and pushes your files to be available on PrairieLearn.

[PrairieLearn](https://ca.prairielearn.org/pl) has an impressive randomisation system where the answer choices can get shuffled and new variants of the question can be created using the different randomisation ranges and files that you provide in the Python code section while creating the markdown file.

![Image for files created by pbs for PL](https://user-images.githubusercontent.com/2507459/128770962-2a8b1cf7-500a-4968-ab8d-94b50cd019fc.png)

## Files created for PrairieLearn

There are three important files created for the PrairieLearn platform:

1. `info.json` : This JSON file contains the unique identifier (UUID), title and topic of the question along with any tags it has.

2. `question.html` : This includes all the HTML that is displayed on PrairieLearn for your question. This includes the question and answer sections and includes the {{}} markdown format that you used for your variables.

3. `server.py` : This .py file contains the Python code from the `server` section of your markdown file. It just contains all the import statements as well as the variables and correct answers defined in the code section. This tells PrairieLearn how to calculate the correct answer, what the question is, what the differnt variables are and how to randomise the questions.

*It is important that the correct format is followed for `server.py` and the values of the variables are stored in the correct keys of the params dicitonary, as shown in the templates*

![Image of the 3 files created for PL](https://user-images.githubusercontent.com/2507459/128770964-55a95262-6369-46fa-bec0-744ba86824b3.png)

These files can also be found on PrairieLearn once your question is available there. You might want to change the values in the `question.html` or the `server.py` file to try and debug your question if there is an issue, but make sure to make the same changes in the file locally and push it to the Github repository. Uniformity should be maintainted between the repository and PrairieLearn.