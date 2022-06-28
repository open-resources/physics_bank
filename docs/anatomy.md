# Anatomy of a Markdown file

TODO: add an image and overview here!

## Header

The header section of the markdown format is in a YAML format.
There are several keys, and below is the key name, and a brief description

- **title** : This is the title for the question that you are authoring.

- **topic** : The topic related to your question. Make sure to choose from the list of available topics for this to be valid.

- **author** : The name of the person who should be credited with creation of the question.

- **source** : The place where the question has been found or taken from. Possible 

- **template_version** : The version of the template that you are using to author the question.

- **attribution** : There are several attribution possibilities:
    - "standard": "Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/)."
    - "openstax-physics-vol1": Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/)
    - "openstax-physics-vol2": Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/)

- **outcomes** : The learning outcomes for the question. Make sure to choose from the list of available learning outcomes for this to be valid. Create an issue on GitHub or notify a supervisor to add a new learning outcome if you are unsure of it's existence in the existing list.

- **difficulty** : This field can have three possible values: `easy`, `medium` or `hard`, and is a subjective assessment of question difficulty.

- **tags** : A list of tags you'd like to add to your question, you should add your initials when coding a problem so you can easily find questions created by you. Eg: If your name is John Doe, add a tag for `JD`. 

- **assets** : Any images or any other files related to the question that you are including in the folder of the question with the markdown file.

- **server** : The python code that is used to generate the randomness, symbolic, or plots in the question. This has all the import statements, the variables that are being used, the function calls to the different libraries being used and the answers as well. See the next section for more details about this.

- **part1** : Every question has a `part1` entry, and the `type` key is required here (`number-input`, `multiple-choice`, etc.). `pl-customizations` is another key where customizations can be entered in based on the [PrairieLearn documentation](https://prairielearn.readthedocs.io/en/latest/elements/).

- **part2** : Multi-part problems have a `part2`, `part3`, etc... in the same format as described in `part1`.

### More details about the `server` section of the header

This can be found in the **server** section of the markdown file.

The first key in this section is the `imports` key which defines all the libraries that will be used in the Python code later and imports them with or without aliases. Make sure to remove any unused imports from here even if they might be present in the template.

The next key in this section is the `generate` key which contains the Python code.
This code defines the variables that will be used in the authoring process of the question such as:

- loading in the list of names and vehicles from files to a python list and picking a random element from the lists.
- Defining the title of the question again and units (if the question requires any).
- Defining numerical variables to be used in the question itself such as speed, velocity, distance or others and then choosing a sensible random range for these according to the question.
- Storing the defined variables in the params dictionary to be later processed by the conversion code to be accessed in the Question Section of the markdown file.
- Defining the formula to find the correct answer for the question with the defined variables. Or storing different answers for questions with multiple answers.

## Question Body

After the YAML header is complete, the next section contains the question text, and this is what the students will be able to see.

### `Part X` Section in the markdown file

This section will include your question in sentences for the question that you are authoring.
You should keep the following in mind while filling this section in:

- Keep each sentence on a separate line.
- Use markdown syntax for any variables you use from the Python code section. Eg: `{{ params.vars.varName }}`
- Use latex syntax for any units or symbols that you might use.

**All the data used in this section should be stored in the data2 dictionary as seen in the `server` section of the header.**

### `Answer Section` in the markdown file

This section will include the answer(s) for your question.
There may be different number of answers depending upon the type of the question you will be authoring.
It will always be a three level ### header in the markdown file.
Each part of the question should have an answer section.

### `Rubric` Section in the markdown file

This is not a required section, but would be used to give the grader a rubric to use for grading a tricky question.

### `Solution` Section in the markdown file

This section is primarily for the questions that do not have a simple answer.
Multi-sentence answers or questions that have elaborate explanations that cannot be coded in should use this section to explain how these questions should be graded.

This is not a required section, and is hidden from the students.

## `Comments` Section in the markdown file

This is for any comments related to the question that you might want to include.
This is not a required section, and is hidden from the students.


## Link to all resources for authoring questions

- [Masterlist of Topics, Subtopics and Learning Outcomes](https://github.com/open-resources/learning_outcomes/blob/main/Masterlist.csv)

- [Templates for different type of questions](https://github.com/open-resources/instructor_physics_bank/tree/main/templates)

- [Guide to using Latex in questions](https://firas.moosvi.com/oer/physicsbank/docs/latex.html)

- [Rounding and Significant Figures in problems](https://firas.moosvi.com/oer/physics_bank/docs/rounding.html)

- [More tips for authoring questions](https://firas.moosvi.com/oer/physics_bank/docs/tips.html)
