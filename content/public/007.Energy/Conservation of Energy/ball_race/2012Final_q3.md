---
title: Two Balls Launched on Different Tracks
topic: Energy
author: Jake Bobowski
source: 2012 Final Q3
template_version: 1.0
attribution: standard
outcomes:
- 7.5.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q3_2012Final.png
server:
  imports: |
    import random
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store title\ndata2[\"\
    params\"][\"vars\"][\"title\"] = 'Two Balls Launched on Different Tracks'\n\n\
    # create list of answers and shuffle\nanswers = [\"A\", \"B\", \"They reach the\
    \ end of the track at the same time.\", \"More information is needed.\"]\nrandom.shuffle(answers)\n\
    \n# Create ans_choices.  \ntotal_choices = len(answers)\nans_choices = [\"ans{0}\"\
    .format(i+1) for i in range(total_choices)]\n\n\n# define possible answers.  \n\
    for i in range(total_choices):\n    choice = ans_choices.pop(0)\n\n    this_answer\
    \ = answers.pop()\n    data2[\"params\"][\"part1\"][choice][\"value\"] = this_answer\n\
    \n    if (this_answer == 'B'):\n        data2[\"params\"][\"part1\"][choice][\"\
    correct\"] = True\n    else:\n        data2[\"params\"][\"part1\"][choice][\"\
    correct\"] = False\n\n# Update the data object with a new dict\ndata.update(data2)\n"
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
      title: Two Balls Launched on Different Tracks
    part1:
      ans1:
        value: More information is needed.
        correct: false
      ans2:
        value: They reach the end of the track at the same time.
        correct: false
      ans3:
        value: A
        correct: false
      ans4:
        value: B
        correct: true
---
# {{ params.vars.title }}
Balls A and B are launched with the same initial velocity along a pair of tracks as shown in the figure.

![Ball A is launched along a horizontal track while Ball B is launched along a u-shaped track.](q3_2012Final.png)

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)