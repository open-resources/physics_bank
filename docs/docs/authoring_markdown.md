# Detailed descriptions of the markdown files used for authoring questions

This guide describes each key present in the markdown file which is used to author questions.

Each question type has it's own template for this markdown file which can be found at [Templates for different type of questions](https://github.com/open-resources/instructor_physics_bank/tree/main/templates)

This markdown file has several sections but is internally read in as a `yaml file` with several keys and values and nested key-value pairs as well. We fill in different sections of this markdown file according to our question.

![YAML markdown file](https://user-images.githubusercontent.com/2507459/128770969-a0a408e6-c50e-4e0d-9da9-369cba8992aa.png)

## Keys in the markdown file

- **title** : This is the title for the question that you are authoring.

- **topic** : The topic related to your question. Make sure to choose from the list of available topics for this to be valid.

- **author** :  The name of the person who has come up with the question.

- **source** : The place where the question has been found or taken from.

- **template_version** : The version of the template that you are using to author the question.

- **attributon** : This is for the licensing, it should always be "standard".

- **outcomes** : The learning outcomes for the question. Make sure to choose from the list of available learning outcomes for this to be valid. Create an issue on GitHub or notify a supervisor to add a new learning outcome if you are unsure of it's existence in the existing list.

- **difficulty** : This can be easy, medium or hard depending upon the question.

- **tags** : Mention your name's initials here. Eg: If your name is John Doe, write J.D. here. 

- **assets** : Any images or any other files related to the question that you are including in the folder of the question with the markdown file.

- **server** : The python code that is used to generate the randomness in the question. This has all the import statements, the variables that are being used, the function calls to the different libraries being used and the answers as well.

## Question Section in the markdown file

This section will include your question in sentences for the question that you are authoring.
You should keep the following in mind while filling this section in:

- Keep each sentence on a separate line.
- Use markdown syntax for any variables you use from the Python code section. Eg: {{params.vars.varName}}
- Use latex syntax for any units or symbols that you might use.

## Answer Section in the markdown file

This section will include the answer(s) for your question.
There may be different number of answers depending upon the type of the question you will be authoring.
It will always be a three level ### header in the markdown file.
Each part of the question should have an answer section.

## Rubric Section in the markdown file

This is not required to be filled always.

## Solution Section in the markdown file

This section is primarily for the questions that do not have a simple answer.
Multi-sentence answers or questions that have elaborate explanations that cannot be coded in should use this section to explain how these questions should be graded.
This section is hidden from the students.
This is not required to be filled always.

## Comments Section in the markdown file

This is for any comments related to the question that you might want to include.
This is not required to be filled always.

## Python Code section in the markdown file

This can be found in the **server** section of the markdown file.

The first key in this section is the `imports` key which defines all the libraries that will be used in the Python code later and imports them with or without aliases. Make sure to remove any unused imports from here even if they might be present in the template.

The next key in this section is the `generate` key which contains the Python code.
This code defines the variables that will be used in the authoring process of the question such as:

- loading in the list of names and vehicles from files to a python list and picking a random element from the lists.
- Defining the title of the question again and units (if the question requires any).
- Defining numerical variables to be used in the question itself such as speed, velocity, distance or others and then choosing a sensible random range for these according to the question.
- Storing the defined variables in the params dictionary to be later processed by the conversion code to be accessed in the Question Section of the markdown file.
- Defining the formula to find the correct answer for the question with the defined variables. Or storing different answers for questions with multiple answers.

**All this data should be stored in the data2 dictionary as seen in the template code.**

