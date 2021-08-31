---
title: Speed Before Impact
topic: Momentum and Impulse
author: Jake Bobowski
source: 2014 Final Q4
template_version: 1.1
attribution: standard
outcomes:
- 7.3.1.2
- 7.3.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q4.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Speed Before Impact
      vehicle: bus
      units: $m/s$
    m: 646
    part1:
      ans1:
        value: 84.0
      ans2:
        value: 42.0
      ans3:
        value: 21.0
      ans4:
        value: 10.0
      ans5:
        value: 0
---
# {{ params.vars.title }}
The figure below shows the force on a {{ params.vars.vehicle }} during a typical collision used during safety tests.
The mass of the {{ params.vars.vehicle }} is {{ params.m }} $kg$ and it comes to rest at the end of the collision.

<img src="Q4.png" alt= " A graph of force in the unit of 10 sub 5 newtons, and time in ms. The graph shows a grid of boxes covering the graph and a curve. There are approximately 27 boxes under the curve." width= 400>

## Part 1

What was the *approximate* speed of the car just before the impact? Choose the best answer.

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)