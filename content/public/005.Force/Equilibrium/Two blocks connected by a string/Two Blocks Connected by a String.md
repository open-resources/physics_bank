---
title: Two Blocks Connected by a String
topic: Force
author: Jake Bobowski
source: 2012 Final Q7
template_version: 1.0
attribution: standard
outcomes:
- 6.7.1.0
- 6.3.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q7_2012Final.png
server:
  imports: |
    import random as rd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = 'Two Blocks Connected by a String'\n\
    data2[\"params\"][\"vars\"][\"units\"] = \"N\"\n\n# Define variables in case the\
    \ image is randomized in the future.\nm1 = 1\nm2 = 1.2\ng = 9.81\n\n# store the\
    \ variables in the dictionary \"params\".  \ndata2[\"params\"][\"m1\"] = m1\n\n\
    # define possible answers\n# round in traditional way using pbh.roundp() and then\
    \ convert to int\ndata2[\"params\"][\"part1\"][\"ans1\"][\"value\"] = int(pbh.roundp(m1*g,\
    \ decimals = 0))     \ndata2[\"params\"][\"part1\"][\"ans1\"][\"correct\"] = False\n\
    \ndata2[\"params\"][\"part1\"][\"ans2\"][\"value\"] = int(pbh.roundp(m2*g, decimals\
    \ = 0))\ndata2[\"params\"][\"part1\"][\"ans2\"][\"correct\"] = True\n\ndata2[\"\
    params\"][\"part1\"][\"ans3\"][\"value\"] = int(pbh.roundp(2*m2*g, decimals =\
    \ 0))\ndata2[\"params\"][\"part1\"][\"ans3\"][\"correct\"] = False\n\ndata2[\"\
    params\"][\"part1\"][\"ans4\"][\"value\"] = int(pbh.roundp(2*m1*g, decimals =\
    \ 0))\ndata2[\"params\"][\"part1\"][\"ans4\"][\"correct\"] = False\n\ndata2[\"\
    params\"][\"part1\"][\"ans5\"][\"value\"] = int(pbh.roundp(m2*g, decimals = 0))\
    \ + 1\ndata2[\"params\"][\"part1\"][\"ans5\"][\"correct\"] = False\n\ndata2[\"\
    params\"][\"part1\"][\"ans6\"][\"value\"] = int(pbh.roundp(m2*g, decimals = 0))\
    \ - 1\ndata2[\"params\"][\"part1\"][\"ans6\"][\"correct\"] = False\n\n# Update\
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
      title: Two Blocks Connected by a String
      units: N
    m1: 1
    part1:
      ans1:
        value: 10
        correct: false
      ans2:
        value: 12
        correct: true
      ans3:
        value: 24
        correct: false
      ans4:
        value: 20
        correct: false
      ans5:
        value: 13
        correct: false
      ans6:
        value: 11
        correct: false
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).