---
title: System Open or Closed
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm Q3
template_version: 1.0
attribution: standard
outcomes:
- 7.5.1.1
- 7.5.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q3.png
server:
  imports: |
    import random
    import pandas as pd
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    manual_vehicles = pd.read_csv("data/vehicles.csv")["Vehicles"].tolist()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'System Open or Closed'
    data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    data2["params"]["vars"]["units"] = "kg"

    # Randomize Variables
    i_a = random.randint(50,150)
    i_b = random.randint(250,350)

    # store the variables in the dictionary "params"
    data2["params"]["i_a"] = i_a
    data2["params"]["i_b"] = i_b

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = "Yes, because the two carts are on a track with no friction."
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = "Yes, because their change in velocities are the same."
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = "No, because the total momentum is nonzero."
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = "No, because the momentum is not conserved"
    data2["params"]["part1"]["ans4"]["correct"] = True

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
      title: System Open or Closed
      vehicle: sedan
      units: kg
    i_a: 65
    i_b: 335
    part1:
      ans1:
        value: Yes, because the two carts are on a track with no friction.
        correct: false
      ans2:
        value: Yes, because their change in velocities are the same.
        correct: false
      ans3:
        value: No, because the total momentum is nonzero.
        correct: false
      ans4:
        value: No, because the momentum is not conserved
        correct: true
---
# {{ params.vars.title }}
Two {{ params.vars.vehicle }}s collide on a track, {{ params.vars.vehicle }}  A comes up behind {{ params.vars.vehicle }}  B and runs into it.
{{ params.vars.vehicle }} A has inertia {{ params.i_a }} {{ params.vars.units }}, {{ params.vars.vehicle }} B has inertia {{ params.i_b }} {{ params.vars.units }}.
The following diagram shows the velocity of each {{ params.vars.vehicle }} as a function of time.

<img src="Q3.png" alt="A velocity versus time graph where {{ params.vars.vehicle }} A has an initial velocity of 8 meters per second and {{ params.vars.vehicle }} B has an initial velocity of 1 meter per second. The two {{ params.vars.vehicle }}s collide at around 4 seconds. The velocity of {{ params.vars.vehicle }} A decreases to 2 meters per second and the velocity of {{ params.vars.vehicle }} B increases to 5 meters per second." width=300>

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)