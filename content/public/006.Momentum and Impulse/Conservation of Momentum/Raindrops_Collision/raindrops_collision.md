---
title: Perfectly Inelastic Collision of Raindrops
topic: Momentum
author: Jake Bobowski
source: 2012 Final Q2
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 7.5.1.3
- 7.5.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Perfectly Inelastic Collision of Raindrops
      units: m/s
    m1: 0.37
    m2: 0.37
    v1_i: 11.5
    v2_i: -16.9
    v1_j_abs: !!python/object/apply:numpy.core.multiarray.scalar
    - &id001 !!python/object/apply:numpy.dtype
      args:
      - f8
      - false
      - true
      state: !!python/tuple
      - 3
      - <
      - null
      - null
      - null
      - -1
      - -1
      - 0
    - !!binary |
      AAAAAAAAH0A=
    v2_j_abs: !!python/object/apply:numpy.core.multiarray.scalar
    - *id001
    - !!binary |
      zczMzMxMM0A=
    v1_j_sign: ' - '
    v2_j_sign: ' - '
    part1:
      ans1:
        value: -5.4$\hat{\imath}$ - 27.0$\hat{\jmath}$
      ans2:
        value: -2.7$\hat{\imath}$ - 14.0$\hat{\jmath}$
      ans3:
        value: -5.4$\hat{\imath}$ - 27.0$\hat{\jmath}$
      ans4:
        value: -0.74$\hat{\imath}$ - 3.7$\hat{\jmath}$
      ans5:
        value: 16.0$\hat{\imath}$ + 6.3$\hat{\jmath}$
      ans6:
        value: 14.0$\hat{\imath}$ + 5.8$\hat{\jmath}$
---
# {{ params.vars.title }}
## Part 1

Two raindrops in a cloud collide perfectly inelastically. The first raindrop has a mass of {{ params.m1}} g and is travelling with $\vec{v_1} =$ ({{ params.v1_i}} $\hat{\imath}$ {{params.v1_j_sign}} {{ params.v1_j_abs}} $\hat{\jmath}$) m/s. The second raindrop has a mass of {{ params.m2}} g and is travelling with $\vec{v_2} =$ ({{ params.v2_i}} $\hat{\imath}$ {{params.v2_j_sign}} {{ params.v2_j_abs}} $\hat{\jmath}$) m/s. What is the resulting velocity of the combined raindrop?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)