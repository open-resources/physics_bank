---
title: Free Fall Drag
topic: Kinematics(1D)
author: Ernest Goh
source: Original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- TA
- APSC181
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Free Fall Drag
      k: 4
      g: 9.81
      t: 0.18
---
# {{ params.vars.title }}
A tennis ball is released from rest. The acceleration that the ball experiences is given by: $a = g - kv^2$, where
$g = {{params.g}} \ \rm{m/s^2}$ and $k = {{params.k}} \ \rm{m^{-1}}$.

## Part 1

What is the speed of the ball at $t= {{params.t}} \ \rm{s}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

What is the ball's terminal velocity?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)