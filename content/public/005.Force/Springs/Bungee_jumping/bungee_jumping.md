---
title: Bungee Jumping
topic: Force
author: Jake Bobowski
source: 2016 Final q8
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
- AK
server:
  imports: |
    import random
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# define or load names/items/objects\
    \ from server files\nnames = pd.read_csv(\"data/names.csv\")[\"Names\"].tolist()\n\
    \nname = random.choice(names)\n\n# store phrases etc\ndata2[\"params\"][\"vars\"\
    ][\"title\"] = 'Bungee Jumping'\ndata2[\"params\"][\"vars\"][\"name\"] = name\n\
    \n# create list of answers and shuffle\nanswers = [\nf\"The tension points up,\
    \ and { name } moves down, so negative work is done.\",\nf\"The tension points\
    \ down, and { name } moves down, so negative work is done.\",\nf\"The tension\
    \ points up, and { name } moves down, so positive work is done.\",\nf\"The tension\
    \ point up, and { name } moves up, so positive work is done.\"  \n]\n\nrandom.shuffle(answers)\n\
    \n# Create ans_choices\nans_choices = [f\"ans{i+1}\" for i in range(len(answers))]\n\
    \n# define possible answers\nfor choice in ans_choices:\n    this_answer = answers.pop()\n\
    \    data2[\"params\"][\"part1\"][choice][\"value\"] = this_answer\n\n    if(this_answer\
    \ == f\"The tension points up, and { name } moves down, so negative work is done.\"\
    ):\n        data2[\"params\"][\"part1\"][choice][\"correct\"] = True\n    else:\n\
    \        data2[\"params\"][\"part1\"][choice][\"correct\"] = False\n\n# Update\
    \ the data object with a new dict\ndata.update(data2)\n"
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
      title: Bungee Jumping
      name: Ahmed
    part1:
      ans1:
        value: The tension points up, and Ahmed moves down, so positive work is done.
        correct: false
      ans2:
        value: The tension points down, and Ahmed moves down, so negative work is
          done.
        correct: false
      ans3:
        value: The tension points up, and Ahmed moves down, so negative work is done.
        correct: true
      ans4:
        value: The tension point up, and Ahmed moves up, so positive work is done.
        correct: false
---
# {{ params.vars.title }}
{{ params.vars.name }} decides to go bungee jumping. Starting atop a very high bridge, elastic cords are tied to their feet and {{ params.vars.name }} jumps off the bridge. Once it has fallen a certain distance, the force of the bungee cords slows their descent until {{ params.vars.name }} is at a lowest point.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)