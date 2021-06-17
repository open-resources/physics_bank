---
title: Spring on an Incline
topic: Energy
author: Jake Bobowski
source: 2013 Final Q10
template_version: 1.0
attribution: standard
outcomes:
- 5.9.1.0
- 5.11
- 7.2.1.0
- 8.1.1.0
- 8.3.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets:
- q10image.png
server:
  imports: |
    import random
    import pandas as pd
    import math
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Spring on an Incline\"\ndata2[\"params\"\
    ][\"vars\"][\"units1\"] = \"m\"\ndata2[\"params\"][\"vars\"][\"units2\"] = \"\
    J\"\n\n# define bounds of the variables\nm = random.randint(2,5)\nk = random.randint(630,670)\n\
    theta = random.randint(25,30)\nmu = 0.250\nd = random.randint(5,9)\ng = 9.8\n\n\
    # store the variables in the dictionary \"params\"\ndata2[\"params\"][\"m\"] =\
    \ m\ndata2[\"params\"][\"k\"] = k\ndata2[\"params\"][\"theta\"] = theta\ndata2[\"\
    params\"][\"mu\"] = mu\ndata2[\"params\"][\"d\"] = d\ndata2[\"params\"][\"g\"\
    ] = g\n\n## Part 1\n\n# define correct answers\ndata2[\"correct_answers\"][\"\
    part1_ans\"] = math.sqrt((2*m*g*d/k)*(mu+math.tan(math.radians(theta)))) \n\n\
    ## Part 2\n\n# define correct answers\ndata2[\"correct_answers\"][\"part2_ans\"\
    ]= 0.5*k*(math.sqrt((2*m*g*d/k)*(mu+math.tan(math.radians(theta)))))**2\n\n# Update\
    \ the data object with a new dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: "pass  \n"
part1:
  type: number-input
  pl-customizations:
    label: $x=$
    allow-blank: true
    weight: 1
    suffix: m
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    label: $K_{max}=$
    allow-blank: true
    weight: 1
    suffix: J
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Spring on an Incline
      units1: m
      units2: J
    m: 2
    k: 661
    theta: 28
    mu: 0.25
    d: 5
    g: 9.8
  correct_answers:
    part1_ans: 0.4814486595773738
    part2_ans: 76.60752430282491
---
# {{ params.vars.title }}
A small {{params.m}} kg block is accelerated from rest on a flat surface by a compressed spring (k = {{params.k}} N/m) along a frictionless, horizontal surface.
The block leaves the spring at the spring's equilibrium position (x = 0) and travels on an incline ($\theta$ = {{params.theta}}$^{\circ}$) with a coefficient of kinetic friction $\mu_k$ = {{params.mu}}.
The block moves a horizontal distance $D$ = {{params.d}} m before coming to a stop.

<img src="q10image.png" width=300>

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)