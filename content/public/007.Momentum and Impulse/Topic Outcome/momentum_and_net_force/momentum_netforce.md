---
title: Momentum and Net Force
topic: Momentum and Impulse
author: Jake Bobowski
source: 2017 Final Q9
template_version: 1.4
attribution: standard
outcomes:
- 6.1.1.3
- 7.2.1.3
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
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Momentum and Net Force
        units: N
      p_i: -6t^2 - 3t
      p_j: 9t^3 - 8t^2 - 7t
      time: 10.8
      part1:
        ans1:
          value: 0
        ans2:
          value: 3000.0
        ans3:
          value: 190.0
        ans4:
          value: 53.0
        ans5:
          value: 8800000.0
---
# {{ params.vars.title }}
The momentum of an object as a function of time is given by $\vec{p} = ({{ params.p_i }})\hat{\imath} + ({{ params.p_j }})\hat{\jmath}$ where $p$ is in kg $\cdot$ m/s and $t$ is in seconds.

## Part 1

What is the magnitude of the net force on the object at $t$ = {{params.time}} s?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)