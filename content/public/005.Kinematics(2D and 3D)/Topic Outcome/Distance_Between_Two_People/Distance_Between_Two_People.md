---
title: Distance Between Two People
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2014 Final Q10
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.2.1.0
- 4.4.1.0
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
      title: Distance Between Two People
      units: $m$
      name1: Mateo
      name2: Savannah
    s: 3
    ai_1: 3
    ai_2: 4
    ai_3: 2
    aj_1: 1
    aj_2: 4
    aj_3: 1
    bi_1: 5
    bi_2: 3
    bi_3: 1
    bj_1: 5
    bj_2: 3
    bj_3: 2
    part1:
      ans1:
        value: 29.0
      ans2:
        value: 15.0
      ans3:
        value: 850.0
      ans4:
        value: 28.0
      ans5:
        value: 780.0
---
# {{ params.vars.title }}
The position of {{ params.vars.name1 }} as a function of time is given by:

$\vec{r_A} =$ ({{ params.ai_1 }}$+${{ params.ai_2 }}$t-${{ params.ai_3 }}$t^2)\hat{\imath} + (${{ params.aj_2 }}$+${{ params.aj_3 }}$t-${{ params.aj_1 }}$t^2)\hat{\jmath}$

{{ params.vars.name2 }}'s position is given by:

$\vec{r_B} =$ ({{ params.bi_1 }}$+${{ params.bi_2 }}$t-${{ params.bi_3 }}$t^2)\hat{\imath} + (${{ params.bj_1 }}$+${{ params.bj_2 }}$t+${{ params.bj_3 }}$t^2)\hat{\jmath}$.

The positions $\vec{r_A}$ and $\vec{r_B}$ are in meters and $t$ is in seconds.

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