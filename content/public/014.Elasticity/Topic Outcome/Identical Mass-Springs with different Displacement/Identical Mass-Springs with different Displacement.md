---
title: Identical Mass-Springs with Different Displacement
topic: Springs
author: Jake Bobowski
source: 2012 Final Q8
template_version: 1.0
attribution: standard
outcomes:
- null
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q8_2012Final.png
server:
  imports: |
    import random
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\ndata2 = nested_dict()\n\n# store title\ndata2[\"\
    params\"][\"vars\"][\"title\"] = 'Identical Mass-Springs with Different Displacement'\n\
    \n# Define Variables in case the image is changed in the future\nd1 = \"$d$\"\n\
    d2 = \"$2d$\"\n\n# store the variables in the dictionary \"params\"\ndata2[\"\
    params\"][\"d1\"] = d1\ndata2[\"params\"][\"d2\"] = d2\n\n# create list of answers\
    \ and shuffle\nanswers = [\"Spring A\", \"Spring B\", \"It is a tie.\", \"Not\
    \ enough information is given.\"]\nrandom.shuffle(answers)\n\n# Create ans_choices.\
    \  \ntotal_choices = len(answers)\nans_choices = [\"ans{0}\".format(i+1) for i\
    \ in range(total_choices)]\n\n# define possible answers.  \nfor i in range(total_choices):\n\
    \    choice = ans_choices.pop(0)\n    this_answer = answers.pop()\n    data2[\"\
    params\"][\"part1\"][choice][\"value\"] = this_answer\n\n    if (this_answer ==\
    \ \"It is a tie.\"):\n        data2[\"params\"][\"part1\"][choice][\"correct\"\
    ] = True\n    else:\n        data2[\"params\"][\"part1\"][choice][\"correct\"\
    ] = False\n\n# Update the data object with a new dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Identical Mass-Springs with Different Displacement
    d1: $d$
    d2: $2d$
    part1:
      ans1:
        value: Spring B
        correct: false
      ans2:
        value: Spring A
        correct: false
      ans3:
        value: Not enough information is given.
        correct: false
      ans4:
        value: It is a tie.
        correct: true
---
# {{ params.vars.title }}
Two identical springs are attached to two identical masses.
Both masses are free to slide along a frictionless horizontal surface.
One of the springs is displaced a distance {{ params.d1 }} from its equilibrium position, while the other is displaced a distance {{ params.d2 }}.

![Using the same point of reference, Spring A is displaced a distance d from its equilibrium position while Spring B is displaced a distance 2d.](q8_2012Final.png)

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)