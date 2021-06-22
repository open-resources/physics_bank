---
title: Running Dog
topic: Kinematics (1D)
author: Jake Bobowski
source: 2015 Practice Midterm Q1
template_version: 1.0
attribution: standard
outcomes:
- 4.2.1.0
- 4.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q1.png
server:
  imports: |
    import random
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = 'Running Dog'\n\n# define useful variables/lists\n\
    TrueAns = [\"The dog is moving at a constant velocity between t=2s and t=6s\"\
    , \n           \"The dog is speeding up at time t=7s\", \n           \"The dog\
    \ is moving at the same speed at time t=10s and t=4s\", \n           \"The dog\
    \ has an average velocity of 0 m/s between time t=0s and t=8s\", \n          \
    \ \"The dog is not moving between t=2s and t=6s\"]\n\nUntrueAns = [\"The dog has\
    \ a negative acceleration at t=9s\", \n             \"The dog is slowing down\
    \ at t=7s\", \n             \"The dog is moving at the same speed at time t=8s\
    \ and t=10s\", \n             \"The dog is not moving between t=6s and t=10s\"\
    , \n             \"The dog has a velocity of 1 m/s between time t=6s and t=10s\"\
    \ ]\n\n# Randomly select 2,3 TrueAns and shuffle the lists\ntotal_choices = 4\n\
    num_Untrue = random.choice([2,3])\nnum_True = total_choices - num_Untrue\nselect\
    \ = random.choice([\"True\",\"Untrue\"])\n\ndata2[\"params\"][\"choice\"] = select\n\
    \n# Create ans_choices\nans_choices = [\"ans{0}\".format(i+1) for i in range(total_choices)]\n\
    \nrandom.shuffle(TrueAns)\nrandom.shuffle(UntrueAns)\n\n# define possible answers\n\
    if select == \"True\":\n    for i in range(num_True):\n        choice = ans_choices.pop(0)\n\
    \        data2[\"params\"][\"part1\"][choice][\"value\"] = TrueAns.pop()\n   \
    \     data2[\"params\"][\"part1\"][choice][\"correct\"] = True\n\n    for i in\
    \ range(num_Untrue):\n        choice = ans_choices.pop(0)\n        data2[\"params\"\
    ][\"part1\"][choice][\"value\"] = UntrueAns.pop()\n        data2[\"params\"][\"\
    part1\"][choice][\"correct\"] = False\n\nelif select == \"Untrue\":\n    for i\
    \ in range(num_Untrue):\n        choice = ans_choices.pop(0)\n        data2[\"\
    params\"][\"part1\"][choice][\"value\"] = UntrueAns.pop()\n        data2[\"params\"\
    ][\"part1\"][choice][\"correct\"] = True\n\n    for i in range(num_True):\n  \
    \      choice = ans_choices.pop(0)\n        data2[\"params\"][\"part1\"][choice][\"\
    value\"] = TrueAns.pop()\n        data2[\"params\"][\"part1\"][choice][\"correct\"\
    ] = False\n# Update the data object with a new dict\ndata.update(data2)\n"
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
      title: Running Dog
    choice: Untrue
    part1:
      ans1:
        value: The dog is not moving between t=6s and t=10s
        correct: true
      ans2:
        value: The dog is slowing down at t=7s
        correct: true
      ans3:
        value: The dog is speeding up at time t=7s
        correct: false
      ans4:
        value: The dog is moving at the same speed at time t=10s and t=4s
        correct: false
---
# {{ params.vars.title }}
Consider the following motion diagram for a dog running down a straight path.

<img src="Q1.png" alt= "A displacement time graph showing the dog increasing by 2 meters from t equals 0 seconds to t equals 2 seconds. The dog is not moving from t equals 2 seconds to t equals 6 seconds. The dog decreases 2 meters from t equals 6 seconds to t equals 8 seconds. The dog decreases to negative 2 meters from t equals 8 second to t equals 10 seconds. The dog increases 2 meters from t equals 10 seconds to t equals 12 seconds.">

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)