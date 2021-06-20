---
title: Rock Powered Rocket
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q7
template_version: 1.0
attribution: standard
outcomes:
- 6.2.1.1
- 7.2.2.0
- 7.2.2.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = "Rock Powered Rocket"
    data2["params"]["vars"]["units1"] = "m/s"
    data2["params"]["vars"]["units2"] = "kg"

    # define bounds of the variables
    i = random.randint(300,400)
    m = random.randint(20,40)
    v_1 = random.randint(5,30)
    v_2 = random.randint(5,30)

    # store the variables in the dictionary "params"
    data2["params"]["i"] = i
    data2["params"]["m"] = m
    data2["params"]["v_1"] = v_1
    data2["params"]["v_2"] = v_2

    ## Part 1

    # define correct answers
    data2["correct_answers"]["part1_ans"] = 0

    ## Part 2

    # define correct answers
    data2["correct_answers"]["part2_ans"] = (-((m+i)*v_1))/m

    ## Part 3

    # define correct answers
    data2["correct_answers"]["part3_ans"] = (((m+i)*v_1)-(i*v_2))/m


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
  label: $P_{total}=$
  pl-customizations:
    allow-blank: true
    weight: 1
part2:
  type: number-input
  label: $v_{f}=$
  pl-customizations:
    allow-blank: true
    weight: 1
part3:
  type: number-input
  label: $v_{rock f}=$
  pl-customizations:
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Rock Powered Rocket
      units1: m/s
      units2: kg
    i: 400
    m: 20
    v_1: 21
    v_2: 17
  correct_answers:
    part1_ans: 0
    part2_ans: -441.0
    part3_ans: 101.0
---
# {{ params.vars.title }}
I am an astronaut caveman, floating in space.
My rocket is powered by throwing rocks out of a hole in the back of the spaceship.
The total inertia of me and my rocket is {{ params.i }} kg.
I also have two {{ params.m }} kg rocks on board.
We are initially at rest.
I throw the first rock, and then we are moving with velocity {{ params.v_1 }} {{ params.vars.units1 }}.
Then I throw the second rock out of the back and we are moving with velocity {{ params.v_2 }} {{ params.vars.units1 }} .

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)