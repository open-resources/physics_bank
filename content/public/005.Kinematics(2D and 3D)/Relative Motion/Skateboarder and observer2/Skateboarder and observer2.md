---
title: A Skateboarder and an Observer2
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2015 Final Q14
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.1
- 5.8.1.3
- 5.5.1.0
- 5.5.1.1
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
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$ ($\hat{\imath}$)
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$ ($\hat{\imath}$)
myst:
  substitutions:
    params:
      vars:
        name1: Maya
        name2: Santiago
        title: A Skateboarder and an Observer
        unit_v: $m/s$
        unit_t: $s$
        unit_x: $m$
      v: -1.82
      v_b: 4.82
      h: 2.27
      m_s: 109.0
      m_b: 2.92
---
# {{ params.vars.title }}
{{ params.vars.name1 }}  is  on  a  skateboard  and  has  an  initial  velocity  of  ({{ params.v }} $m/s$) $\hat{\imath}$ relative  to  {{ params.vars.name2 }}  who  is at rest with respect to the earth.  Just as they are gliding past {{ params.vars.name2 }},  {{ params.vars.name1 }} throws a ball in the positive $x$-direction from a height of {{ params.h }} m.  According to {{ params.vars.name1 }}, the ball has an initial velocity of ({{ params.v_b }} $m/s$) $\hat{\imath}$.

## Part 1

What is the initial velocity of the ball according to {{ params.vars.name2 }}?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit_v }}.

## Part 2

How long is the ball in the air?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit_t }}.

## Part 3

Relative to {{ params.vars.name2 }}, where does the ball land?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit_x }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)