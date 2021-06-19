---
title: Frictional Force between Tires and the Road
topic: Force
author: Jake Bobowski
source: 2012 Final Q6
template_version: 1.0
attribution: standard
outcomes:
- 6.9.1.3
- 6.12.1.1
- 6.3.1.3
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
  imports: "import random    \nimport pandas as pd\nimport prairielearn as pl\nimport\
    \ sympy as sp\nfrom collections import defaultdict\nnested_dict = lambda: defaultdict(nested_dict)\n"
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects from server files
    manual_vehicles = pd.read_csv("data/manual_vehicles.csv")["Manual Vehicles"].tolist()

    # store phrases etc
    data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    data2["params"]["vars"]["title"] = 'Frictional Force between Tires and the Road'

    # Declare math symbols to be used by sympy
    v, R, g = sp.symbols('v R g')

    # Describe the solution equation
    mu = v**2/(g*R)

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(mu)

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: "pass    \n"
part1:
  type: symbolic-input
  label: $\mu_s = $
  pl-customizations:
    variables: m, v, R, g
    weight: 1
    allow-blank: false
substitutions:
  params:
    vars:
      vehicle: a tricycle
      title: Frictional Force between Tires and the Road
  correct_answers:
    part1_ans:
      _type: sympy
      _value: v**2/(R*g)
      _variables:
      - g
      - R
      - v
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }} of mass $m$ is driving around a horizontal circular track of radius $R$ at constant speed $v$.
The frictional force between the tires of the {{ params.vars.vehicle }} and the road is at its maximum value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)