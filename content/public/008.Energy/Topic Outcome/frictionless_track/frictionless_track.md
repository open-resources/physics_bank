---
title: Horizontal frictionless track
topic: Energy
author: Jake Bobowski
source: 2013 Final Q12
template_version: 1.0
attribution: standard
outcomes:
- 8.2.1.0
- 8.3.1.0
- 8.5.1.1
- 9.1.1.1
- 9.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets:
- q12image.png
server:
  imports: |
    import random
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Horizontal frictionless track\"\ndata2[\"\
    params\"][\"vars\"][\"units\"] = \"N\"\n\n# define bounds of the variables\nm\
    \ = random.randint(1,20)*0.25\nv = random.randint(2,9)\nR = random.randint(1,(8/4))*0.5\
    \ \nL = random.randint(10,17)\ng = 9.8\n\n# store the variables in the dictionary\
    \ \"params\"\ndata2[\"params\"][\"m\"] = m\ndata2[\"params\"][\"v\"] = v\ndata2[\"\
    params\"][\"R\"] = R\ndata2[\"params\"][\"L\"] = L\n\n# define correct answers\n\
    \ndata2[\"correct_answers\"][\"part1_ans\"] = pbh.roundp((v**2)+(2*g*R)*(m/R),\
    \ sigfigs = 3)\ndata2[\"correct_answers\"][\"part2_ans\"] = pbh.roundp(((v/2)+(2*g*R))/(g*L),\
    \ sigfigs = 2)\n\n# Update the data object with a new dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: N
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\mu = $
    suffix: null
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Horizontal frictionless track
      units: N
    m: 1.25
    v: 6
    R: 0.5
    L: 15
  correct_answers:
    part1_ans: 60.5
    part2_ans: 0.087
---
# {{ params.vars.title }}
A small block of mass m = {{params.m}} kg is fired with an initial speed v0 = {{params.v}} m/s along a horizontal section of frictionless track, as shown in the top portion of the figure.
The block then moves along the frictionless semicircular vertical track of radius R = {{params.R}} m.

<img src="q12image.png" alt="Mass on frictionless track">

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)