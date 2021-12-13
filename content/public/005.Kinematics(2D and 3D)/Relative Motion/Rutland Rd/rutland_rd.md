---
title: Rutland Rd
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 111 2013W1 MT2 Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.8.1.3
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- MP
assets:
- q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $km/h$
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Rutland Rd
      vehicle: truck
      units: km/h
    v: 56
    part2:
      ans1:
        value: North
      ans2:
        value: North-East
      ans3:
        value: East
      ans4:
        value: South-East
      ans5:
        value: South
      ans6:
        value: South-West
      ans7:
        value: West
      ans8:
        value: North-West
      ans9:
        value: Impossible to know without knowing how far each car is from the intersection.
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }} drives northward on Rutland Road North at {{ params.v }} {{ params.vars.units }} towards the intersection with 33rd Street.
A second {{ params.vars.vehicle }} drives eastward at {{params.v}} {{ params.vars.units }} on 33rd Street having just left the same intersection as shown in the figure below.

As a passenger in the second {{ params.vars.vehicle }}, the first {{ params.vars.vehicle }} appears to travel at a velocity $v$.

<img src="q1.png" width = 400px>

## Part 1

What is the magnitude of $v$, in {{ params.vars.units }}?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the (cardinal) direction of $v$ ?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}
- {{ params.part2.ans6.value }}
- {{ params.part2.ans7.value }}
- {{ params.part2.ans8.value }}
- {{ params.part2.ans9.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)