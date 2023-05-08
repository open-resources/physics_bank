---
title: Archery Competition
topic: Template
author: Firas Moosvi
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.1
- 5.5.1.2
difficulty:
- medium
randomization:
- 4
taxonomy:
- undefined
span:
- undefined
length:
- medium
tags:
- JR
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
    label: $x = $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_name: Emilia
    params_vars_title: Archery Competition
    params_d: 150
    params_v: 121
    params_h: 202
    params_theta: 41
---
# {{ params_vars_title }}
{{ params_vars_name }} is reading a novel that describes an athelete participating in an archery competition.
The athlete fires an arrow horizontally at a height of ${{ params_h }}$ $\rm{cm}$ above the ground and it lands ${{ params_d }}$ $\rm{m}$ away from them.

## Part 1

Neglecting air resistance, lift, and drag, what is the initial speed the arrow must have been fired at to land ${{ params_d }}$ $\rm{m}$ away?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

If the arrow was instead fired at an angle ${{ params_theta }}^\circ$ to the horizontal (instead of horizontally), how far would it have gone if it was launched at a speed of ${{ params_v }}$ $\rm{m/s}$.

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)