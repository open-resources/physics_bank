---
title: Dinner Plate
topic: Momentum and Impulse
author: Jake Bobowski
source: 2016 Final Q1 P2
template_version: 1.0
attribution: standard
outcomes:
- 10.1.1.1
- 10.5.2.2
- 11.4.1.1
- 7.2.3.2
- 7.2.3.2
- 7.5.3.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects


    # store phrases etc
    data2["params"]["vars"]["title"] = "Dinner Plate"
    data2["params"]["vars"]["part1"]["units"] = "rad/s"
    data2["params"]["vars"]["part2"]["units"] = "$kg m^2$"
    data2["params"]["vars"]["part3"]["units"] = "$kg m^2$/s"
    data2["params"]["vars"]["part4"]["units"] = "rad/s"
    data2["params"]["vars"]["part5"]["units"] = "J"

    # define bounds of the variables
    m_p = pbh.roundp(random.uniform(0.7, 1.7), decimals =2)
    r_p = pbh.roundp(random.uniform(0.10, 0.50), decimals =2)
    m = pbh.roundp(random.uniform(1.9, 2.9), decimals =2)
    r = pbh.roundp(random.uniform(0.05, 0.45), decimals =2)
    x = random.randint(1, 6)

    # store the variables in the dictionary "params"
    data2["params"]["m_p"] = m_p
    data2["params"]["r_p"] = r_p
    data2["params"]["m"] = m
    data2["params"]["r"] = r
    data2["params"]["x"] = x

    ## Part 1

    # define correct answers
    part1_ans = pbh.roundp(x*2*math.pi,decimals=2)
    data2["correct_answers"]["part1_ans"] = part1_ans

    ## Part 2

    # define correct answers
    part2_ans = pbh.roundp(0.5*m*math.pow(r_p, 2),decimals=2)
    data2["correct_answers"]["part2_ans"] = part2_ans

    ## Part 3

    # define correct answers
    part3_ans = pbh.roundp(part2_ans*part1_ans,decimals=2)
    data2["correct_answers"]["part3_ans"] = part3_ans

    # Part 4

    # define correct answers
    part4_ans = pbh.roundp(part3_ans/(part2_ans+(0.5*m*math.pow(r, 2))),decimals=2)
    data2["correct_answers"]["part4_ans"] = part4_ans

    ## Part 5

    # define correct answers
    part5_ans = pbh.roundp(((0.5*(part2_ans+(0.5*m*math.pow(r, 2))))*part4_ans) - (0.5*(part2_ans)*math.pow(part1_ans,2)),decimals=2)
    data2["correct_answers"]["part5_ans"] = part5_ans

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $\omega_i = $
part2:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $I_p = $
part3:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $L_i = $
part4:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $w_f = $
part5:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $\Delta E = $
substitutions:
  params:
    vars:
      title: Dinner Plate
      part1:
        units: rad/s
      part2:
        units: $kg m^2$
      part3:
        units: $kg m^2$/s
      part4:
        units: rad/s
      part5:
        units: J
    m_p: 1.43
    r_p: 0.38
    m: 2.73
    r: 0.33
    x: 5
  correct_answers:
    part1_ans: 31.42
    part2_ans: 0.2
    part3_ans: 6.28
    part4_ans: 18.01
    part5_ans: -95.58
---
# {{ params.vars.title }}
A cylindrical dinner plate is spinning out in space. It has mass $m_p = {{params.m_p}} kg$, radius $r = {{ params.r_p }} m$ and it rotates clockwise (as seen from above) {{ params.x }} times every second.
A (non-rotating) cylindrical cake is shot at it, in the manner shown, and it sticks to the surface of the plate.
The cake has a mass $m = {{ params.m }} kg$ and radius $r = {{ params.r }} m$.
In the end, both the cake and the plate rotate together.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)