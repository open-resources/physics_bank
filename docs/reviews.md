# Reviewing a markdown question

This process specifically applies to .md files which will be converted to the PrairieLearn (PL) format and uploaded to PL, however many of the review processes are similar and applicable for other purposes.

## Review Process

1. If you have been requested to review a PR, make sure to click "Add your review". 
    - Comment or edit each line of the .md file as you see fit as part of your review
1. Check that the python syntax is correct.
    - This can be verified by adding the check_syntax label (hopefully the original author has already done this).
1. Check that the metadata is correctly filled out. 
    - This includes title, topic, author, source, template_version, attribution, outcomes, difficulty, randomization, taxonomy, tags, and assets. 
1. Check that the type for each part is correct. 
    - For example, if there are multiple parts, each part may have a different "type" assignment. 
1. Check that any randomization is sensible, and that the corner cases will not seem to cause issues. 
1. For each question part, check that the format is correct and follows the most up to date syntax and organizational structure on the relevant template file. 
1. Check that the problem works in PrairieLearn.
    - Be sure to pull from the git repo within PL to make sure you are viewing the latest problem version.
    For problems with randomization, you may need to do the problem multiple times to check all of the potential outcome branches. 
1. Once your review is complete, submit your review with a comment which outlines what you have found and what needs to be done, if anything. 
    If there are no issues, approve it. If there are issues, request changes before approval

## Common Issues

1. Check that the variable values are being stored correctly. For example, see the following example (don't feel bad if this is your question!):

<img src="https://user-images.githubusercontent.com/25753746/121758868-104a8d00-cad8-11eb-9765-bb54ea28ac9f.png" width=300>

In this case, because the question maker copied and pasted the code, the '[ans1][correct]' value is used for each variable, instead of incrementing. 
It should be '[ans2]' in the second answer, and so on.
     
2. Check that all the numbers/floats are rounded using `pbh.roundp()`.
     
3. Make sure that the mustache templating syntax in the markdown section of the question correctly references the variables stored in the `data` dictionary.

4. In most cases, you should be using $\LaTeX$ syntax to refer to variables and units. For units, our convention is to use `\textrm{ kg}`
