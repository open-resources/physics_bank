---
title: Perfectly Inelastic Collision of Raindrops
topic: Momentum and Impulse
author: Jake Bobowski
source: 2012 Final Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.1.3
- 7.5.1.4
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Perfectly Inelastic Collision of Raindrops
        units: m/s
      m1: 0.81
      m2: 0.43
      v1_i: -13.7
      v2_i: 19.0
      v1_j_abs: 16.8
      v2_j_abs: 1.52
      v1_j_sign: ' + '
      v2_j_sign: ' - '
      part1:
        ans1:
          value: -3.6$\hat{\imath}$ + 16.0$\hat{\jmath}$
        ans2:
          value: -2.4$\hat{\imath}$ + 10.0$\hat{\jmath}$
        ans3:
          value: -6.8$\hat{\imath}$ + 30.0$\hat{\jmath}$
        ans4:
          value: -1.8$\hat{\imath}$ + 8.0$\hat{\jmath}$
        ans5:
          value: -48.0$\hat{\imath}$ + 35.0$\hat{\jmath}$
        ans6:
          value: -16.0$\hat{\imath}$ + 12.0$\hat{\jmath}$
---
# {{ params.vars.title }}
Two raindrops in a cloud collide perfectly inelastically. The first raindrop has a mass of {{ params.m1}} g and is travelling with $\vec{v_1} =$ ({{ params.v1_i}} $\hat{\imath}$ {{params.v1_j_sign}} {{ params.v1_j_abs}} $\hat{\jmath}$) m/s.
The second raindrop has a mass of {{ params.m2}} g and is travelling with $\vec{v_2} =$ ({{ params.v2_i}} $\hat{\imath}$ {{params.v2_j_sign}} {{ params.v2_j_abs}} $\hat{\jmath}$) m/s.

## Part 1

What is the resulting velocity of the combined raindrop?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)