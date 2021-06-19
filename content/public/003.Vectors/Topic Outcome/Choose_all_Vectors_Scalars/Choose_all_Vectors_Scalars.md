---
title: Choose all Vectors and Scalars
topic: Vectors
author: Jake Bobowski
source: 2015 practice midterm 1 Q5
template_version: 1.0
attribution: standard
outcomes:
- 2.1.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
server:
  imports: |
    import random
    import pandas as pd
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Choose all Vectors and Scalars\"\n\n\
    # define useful variables/lists\nvectors = [\"The position in 3 dimensions\",\
    \ \"The position in a 1 dimensional system\", \"Displacement\", \"velocity\",\
    \ \"Acceleration\", \"The average velocity\", \"The average acceleration\", \"\
    Momentum\", \"Force\", \"Lift\", \"Drag\", \"Weight\"]\nscalars = [\"Speed\",\
    \ \"Distance travelled\", \"Length\", \"Area\", \"Volume\", \"Mass\", \"Density\"\
    , \"Pressure\", \"Temperature\", \"Energy\", \"Entropy\", \"Work\", \"Power\"\
    ]\n\n# Randomly select 2,3,4 scalars and shuffle the lists\ntotal_choices = 6\n\
    num_scalars = random.choice([2,3,4])\nnum_vectors = total_choices - num_scalars\n\
    select = random.choice([\"vectors\",\"scalars\"])\n\ndata2[\"params\"][\"choice\"\
    ] = select\n\n# Create ans_choices\nans_choices = [\"ans{0}\".format(i+1) for\
    \ i in range(total_choices)]\n\nrandom.shuffle(scalars)\nrandom.shuffle(vectors)\n\
    \n# define possible answers\nif select == \"vectors\":\n    for i in range(num_vectors):\n\
    \        choice = ans_choices.pop(0)\n        data2[\"params\"][\"part1\"][choice][\"\
    value\"] = vectors.pop()\n        data2[\"params\"][\"part1\"][choice][\"correct\"\
    ] = True\n\n    for i in range(num_scalars):\n        choice = ans_choices.pop(0)\n\
    \        data2[\"params\"][\"part1\"][choice][\"value\"] = scalars.pop()\n   \
    \     data2[\"params\"][\"part1\"][choice][\"correct\"] = False\n\nelif select\
    \ == \"scalars\":\n    for i in range(num_scalars):\n        choice = ans_choices.pop(0)\n\
    \        data2[\"params\"][\"part1\"][choice][\"value\"] = scalars.pop()\n   \
    \     data2[\"params\"][\"part1\"][choice][\"correct\"] = True\n        \n   \
    \ for i in range(num_vectors):\n        choice = ans_choices.pop(0)\n        data2[\"\
    params\"][\"part1\"][choice][\"value\"] = vectors.pop()\n        data2[\"params\"\
    ][\"part1\"][choice][\"correct\"] = False\n\n# Update the data object with a new\
    \ dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
substitutions:
  params:
    vars:
      title: Choose all Vectors and Scalars
    choice: scalars
    part1:
      ans1:
        value: Mass
        correct: true
      ans2:
        value: Volume
        correct: true
      ans3:
        value: Density
        correct: true
      ans4:
        value: Work
        correct: true
      ans5:
        value: The position in 3 dimensions
        correct: false
      ans6:
        value: Acceleration
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)