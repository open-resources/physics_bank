---
title: Energy Lost due to Air Friction
topic: Energy
author: Jake Bobowski
source: 2012 Final Q4
template_version: 1.0
attribution: standard
outcomes:
- 7.5.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
server:
  imports: |
    import random
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store units etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Energy Lost due to Air Friction\"\n\
    data2[\"params\"][\"vars\"][\"units\"] = \"J\"\n\n# Randomize Variables\nm = random.uniform(0.50,3.00)\
    \  #generate random float\nv = random.uniform(10.0,60.0)\nh = random.uniform(5.0,100.0)\n\
    \n#round variables for display and before calculations are performed to avoid\
    \ floating point errors\nm = pbh.roundp(m, sigfigs = 3)\nv = pbh.roundp(v, sigfigs\
    \ = 3)\nh = pbh.roundp(h, sigfigs = 3)\n\n# store the variables in the dictionary\
    \ \"params\"\ndata2[\"params\"][\"m\"] = m\ndata2[\"params\"][\"v\"] = v\ndata2[\"\
    params\"][\"h\"] = h\n\n# store value of g\ng = 9.81\n\n# define possible answers.\
    \ \n\nans1 = (m*g*h)-(0.5*m*v*v)\ndata2[\"params\"][\"part1\"][\"ans1\"][\"value\"\
    ] = pbh.roundp(ans1,sigfigs = 3)\ndata2[\"params\"][\"part1\"][\"ans1\"][\"correct\"\
    ] = False\n\nans2 = (-1)*((m*g*h)-(0.5*m*v*v))   #Taking the negative since we\
    \ are considering the energy lost.\ndata2[\"params\"][\"part1\"][\"ans2\"][\"\
    value\"] = pbh.roundp(ans2,sigfigs = 3)\ndata2[\"params\"][\"part1\"][\"ans2\"\
    ][\"correct\"] = True\n\nans3 = (-1)*((m*g*h)+(0.5*m*v*v))\ndata2[\"params\"][\"\
    part1\"][\"ans3\"][\"value\"] = pbh.roundp(ans3,sigfigs = 3)\ndata2[\"params\"\
    ][\"part1\"][\"ans3\"][\"correct\"] = False\n\nans4 = (m*g*h)+(0.5*m*v*v)\ndata2[\"\
    params\"][\"part1\"][\"ans4\"][\"value\"] = pbh.roundp(ans4,sigfigs = 3)\ndata2[\"\
    params\"][\"part1\"][\"ans4\"][\"correct\"] = False\n\nans5 = (m*g*h)-(0.5*m*v)\n\
    data2[\"params\"][\"part1\"][\"ans5\"][\"value\"] = pbh.roundp(ans5,sigfigs =\
    \ 3)\ndata2[\"params\"][\"part1\"][\"ans5\"][\"correct\"] = False\n\nans6 = (m*g*h)+(0.5*m*v)\n\
    data2[\"params\"][\"part1\"][\"ans6\"][\"value\"] = pbh.roundp(ans6,sigfigs =\
    \ 3)\ndata2[\"params\"][\"part1\"][\"ans6\"][\"correct\"] = False\n\n# Update\
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
      title: Energy Lost due to Air Friction
      units: J
    m: 1.07
    v: 24.2
    h: 68.6
    part1:
      ans1:
        value: 407.0
        correct: false
      ans2:
        value: -407.0
        correct: true
      ans3:
        value: -1030.0
        correct: false
      ans4:
        value: 1030.0
        correct: false
      ans5:
        value: 707.0
        correct: false
      ans6:
        value: 733.0
        correct: false
---
# {{ params.vars.title }}
A body of mass {{ params.m }} kg is thrown upwards with a velocity of {{ params.v }} m/s.
It momentarily comes to rest after attaining a height of {{ params.h }} m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)