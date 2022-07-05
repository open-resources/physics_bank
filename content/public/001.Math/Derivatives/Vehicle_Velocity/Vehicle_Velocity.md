---
title: Vehicle Velocity
topic: Math
author: Jake Bobowski
source: 2014 Final Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.7.2.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- EW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Vehicle Velocity
      vehicle: van
      units: $m/s$
    i_1: 1
    i_2: 3
    j_1: 7
    j_2: 1
    s: 2
    part1:
      ans1:
        value: (1$\hat{\imath}$ + 41/4$\hat{\jmath}$)
      ans2:
        value: (1$\hat{\imath}$ + 12$\hat{\jmath}$)
      ans3:
        value: (-2$\hat{\imath}$ + 23/2$\hat{\jmath}$)
      ans4:
        value: (-2$\hat{\imath}$ + 41/4$\hat{\jmath}$)
      ans5:
        value: (1$\hat{\imath}$ + 23/2$\hat{\jmath}$)
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }}'s position as a function of time is given by $\vec{r} =$ ({{ params.i_1 }}$t^2 -$ {{ params.i_2 }}$t)\hat{\imath} + ($ {{ params.j_1 }}$t^{-1}+$ {{ params.j_2 }} $t^3)\hat{\jmath}$ where $\vec{r}$ is in meters and $t$ is in seconds.

## Part 1

What is the {{ params.vars.vehicle }}'s velocity at $t=$ {{ params.s }} $s$?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)