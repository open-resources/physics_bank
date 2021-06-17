---
title: Distance travelled
topic: Kinematics
author: Firas Moosvi
source: original
template_version: 1.0
attribution: standard
outcomes:
- undefined
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
server:
  imports: |
    import random
    import pandas as pd
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects from server files
    names = pd.read_csv("data/names.csv")["Names"].tolist()
    manual_vehicles = pd.read_csv("data/manual_vehicles.csv")["Manual Vehicles"].tolist()

    # store phrases etc
    data2["params"]["vars"]["name"] = random.choice(names)
    data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    data2["params"]["vars"]["units"] = "m/s"
    data2["params"]["vars"]["title"] = "Distance travelled"

    # Randomize Variables
    v = random.randint(2,7)
    t = random.randint(5,10)

    # store the variables in the dictionary "params"
    data2["params"]["v"] = v
    data2["params"]["t"] = t

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = 42
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = v*t
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = v+t
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = v/t
    data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = v-t
    data2["params"]["part1"]["ans5"]["correct"] = False

    data2["params"]["part1"]["ans6"]["value"] = 1.3*(v-t)
    data2["params"]["part1"]["ans6"]["correct"] = False

    # Update the data object with a new dict
    data.update(data2)
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
      name: Emilia
      vehicle: ice skates
      units: m/s
      title: Distance travelled
    v: 5
    t: 8
    part1:
      ans1:
        value: 42
        correct: false
      ans2:
        value: 40
        correct: true
      ans3:
        value: 13
        correct: false
      ans4:
        value: 0.625
        correct: false
      ans5:
        value: -3
        correct: false
      ans6:
        value: -3.9000000000000004
        correct: false
---
# {{ params.vars.title }}
{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)