---
title: Distance Between Two People
topic: Kinematics(1D)
author: Jake Bobowski
source: 2014 Final Q10
template_version: 1.1
attribution: standard
outcomes:
- 1.2.1.0
- 4.4.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
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
      title: Distance Between Two People
      units: $m$
      name1: Savannah
      name2: Mateo
    s: 2
    ai_1: 2
    ai_2: 4
    ai_3: 3
    aj_1: 1
    aj_2: 4
    aj_3: 1
    bi_1: 3
    bi_2: 2
    bi_3: 3
    bj_1: 6
    bj_2: 3
    bj_3: 3
    part1:
      ans1:
        value: 19.0
      ans2:
        value: 9.6
      ans3:
        value: 370.0
      ans4:
        value: 30.0
      ans5:
        value: 890.0
---
# {{ params.vars.title }}
The position of {{ params.vars.name1 }} as a function of time is given by:

$\vec{r}\_A = ({{ params.ai_1 }}+{{ params.ai_2 }}t-{{ params.ai_3 }}t^2)\hat{\imath} + ({{ params.aj_2 }}+{{ params.aj_3 }}t-{{ params.aj_1 }}t^2)\hat{\jmath}$

{{ params.vars.name2 }}'s position is given by:

$\vec{r}\_B = ({{ params.bi_1 }}+{{ params.bi_2 }}t-{{ params.bi_3 }}t^2)\hat{\imath} + ({{ params.bj_1 }}+{{ params.bj_2 }}t+{{ params.bj_3 }}t^2)\hat{\jmath}$

The positions $\vec{r}\_A$ and $\vec{r}\_B$ are in meters and $t$ is in seconds.

## Part 1

What is the distance between {{ params.vars.name1 }} and {{ params.vars.name2 }} when $t$ = {{ params.s }}?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)