---
title: Kinetic Energy of Test Mass
topic: Energy
author: Jake Bobowski
source: 2012 Final Q5
template_version: 1.0
attribution: standard
outcomes:
- 7.2.1.0
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
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    \ndata2[\"params\"][\"vars\"][\"title\"] = 'Kinetic Energy of Test Mass'\ndata2[\"\
    params\"][\"vars\"][\"units\"] = 'J'\n\n# Randomize Variables. Errors are defined\
    \ as d_variablename\n\nm = random.randint(50,500)\nv = pbh.roundp(random.uniform(1.00,9.00),\
    \ sigfigs = 3)  #generate random float\n\nd_m = random.randint(2,4)\nd_v = pbh.roundp(random.uniform(0.01,0.09),\
    \ sigfigs = 1)\n\n# store the variables in the dictionary \"params\"\ndata2[\"\
    params\"][\"m\"] = m\ndata2[\"params\"][\"v\"] = v\n\ndata2[\"params\"][\"d_m\"\
    ] = d_m\ndata2[\"params\"][\"d_v\"] = d_v\n\n# calculate and store KE.  Since\
    \ the focus is error analysis, this will not be randomised. Round to 3 dp.\n\n\
    ke = 0.5*(m/1000)*v*v\nke_ans = str(pbh.roundp(ke,decimals=3))\n\n# define possible\
    \ answers for error\n\nans1 = ((d_m/m) + (d_v/v))*ke\ndata2[\"params\"][\"part1\"\
    ][\"ans1\"][\"value\"] = ke_ans + \" $\\pm$ \" + str(pbh.roundp(ans1,decimals=3))\n\
    data2[\"params\"][\"part1\"][\"ans1\"][\"correct\"] = False\n\nans2 = ((d_m/m)\
    \ + 2*(d_v/v))*ke\ndata2[\"params\"][\"part1\"][\"ans2\"][\"value\"] = ke_ans\
    \ + \" $\\pm$ \" + str(pbh.roundp(ans2,decimals=3))\ndata2[\"params\"][\"part1\"\
    ][\"ans2\"][\"correct\"] = True\n\nans3 = ((d_m/m) + (d_v/v)*(d_v/v))*ke \ndata2[\"\
    params\"][\"part1\"][\"ans3\"][\"value\"] = ke_ans + \" $\\pm$ \" + str(pbh.roundp(ans3,decimals=3))\n\
    data2[\"params\"][\"part1\"][\"ans3\"][\"correct\"] = False\n\nans4 = (d_m/m)\
    \ + (d_v/v)*(d_v/v)\ndata2[\"params\"][\"part1\"][\"ans4\"][\"value\"] = ke_ans\
    \ + \" $\\pm$ \" + str(pbh.roundp(ans4,decimals=3))\ndata2[\"params\"][\"part1\"\
    ][\"ans4\"][\"correct\"] = False\n\nans5 = (d_m/m) + 2*(d_v/v)\ndata2[\"params\"\
    ][\"part1\"][\"ans5\"][\"value\"] = ke_ans + \" $\\pm$ \" + str(pbh.roundp(ans5,decimals=3))\n\
    data2[\"params\"][\"part1\"][\"ans5\"][\"correct\"] = False\n\nans6 = (d_m/m)*ke\n\
    data2[\"params\"][\"part1\"][\"ans6\"][\"value\"] = ke_ans + \" $\\pm$ \" + str(pbh.roundp(ans6,decimals=3))\n\
    data2[\"params\"][\"part1\"][\"ans6\"][\"correct\"] = False\n\n# Update the data\
    \ object with a new dict\ndata.update(data2)\n"
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
      title: Kinetic Energy of Test Mass
      units: J
    m: 66
    v: 8.98
    d_m: 2
    d_v: 0.08
    part1:
      ans1:
        value: 2.661 $\pm$ 0.104
        correct: false
      ans2:
        value: 2.661 $\pm$ 0.128
        correct: true
      ans3:
        value: 2.661 $\pm$ 0.081
        correct: false
      ans4:
        value: 2.661 $\pm$ 0.03
        correct: false
      ans5:
        value: 2.661 $\pm$ 0.048
        correct: false
      ans6:
        value: 2.661 $\pm$ 0.081
        correct: false
---
# {{ params.vars.title }}
In a lab, a test mass with $m = $ {{ params.m}} $\pm$ {{ params.d_m}} g is measured to have a speed of {{ params.v}} $\pm$ {{ params.d_v}} $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)