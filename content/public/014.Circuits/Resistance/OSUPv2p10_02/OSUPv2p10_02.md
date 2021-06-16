---
title: Battery Internal Resistance
topic: Circuits
author: Joseph Wandinger
source: OSUP Volume 2, Chapter 10, Question 2
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 21.8.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- JW
assets: null
server:
  imports: |
    import random
    import numpy as np
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects from server files
    # Commented b/c I don't think I need them. I'll get rid of them in the final version.
    #names = pd.read_csv("data/names.csv")["Names"].tolist()
    #manual_vehicles = pd.read_csv("data/manual_vehicles.csv")["Manual Vehicles"].tolist()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Battery Internal Resistance'
    # Commented b/c I don't think I need them. I'll get rid of them in the final version.
    #data2["params"]["vars"]["name"] = random.choice(names)
    #data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    #data2["params"]["vars"]["units"] = "m/s"

    # Randomize Variables
    x = random.randint(2,5)
    N = random.randint(2,5)
    V_num = random.choice(np.linspace(5,15,41))
    V_string = '{:.2f}'.format(round(V_num,2))

    # store the variables in the dictionary "params"
    data2["params"]["x"] = x
    data2["params"]["N"] = N
    data2["params"]["V_string"] = V_string

    # define correct answers
    data2["correct_answers"]["part1_ans"] = (N+1)/(N+x)

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: |
    pass
    pass
  grade: ''
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    label: $I_\mathrm{f}/I_0= $
    comparison: decdig
    digits: 5
    show-placeholder: false
substitutions:
  params:
    vars:
      title: Battery Internal Resistance
    x: 2
    N: 3
    V_string: '8.25'
  correct_answers:
    part1_ans: 0.8
---
# {{ params.vars.title }}
A battery with an internal resistance of $r$ and an emf of {{ params.V_string }}$\textrm{ V}$ is connected to a load resistor $R = {{ params.N }}r$ and current $I_0$ flows.
As the battery ages, the internal resistance increases by a factor of {{ params.x }}.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).
![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)