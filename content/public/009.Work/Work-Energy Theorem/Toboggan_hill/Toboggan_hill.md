---
title: Sled Hill
topic: Work
author: Jake Bobowski
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.1.1.1
- 9.2.1.0
difficulty:
- medium
randomization:
- 8
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- AK
assets:
- Sled.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $W_g = $
    allow-blank: true
    weight: 1
    suffix: $\rm{kJ}$
    comparison: decdig
    digits: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $W_{fr} = $
    allow-blank: true
    weight: 1
    suffix: $\rm{kJ}$
    comparison: decdig
    digits: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $W_w = $
    allow-blank: true
    weight: 1
    suffix: $\rm{kJ}$
    comparison: decdig
    digits: 1
part4:
  type: number-input
  pl-customizations:
    label: $v_f = $
    allow-blank: true
    weight: 1
    suffix: $\rm{m/s}$
    comparison: decdig
    digits: 1
myst:
  substitutions:
    params_vars_name: Santiago
    params_vars_title: Toboggan Hill
    params_vars_units1_2_3: "$\rm{kJ}$"
    params_vars_units_4: "$\rm{m/s}$"
    params_m: 30
    params_l: 83
    params_ang_horiz: 32
    params_fr: 79
    params_fwind: 23
    params_ang_wind: 23
    params_v_i: 3
---
# {{ params_vars_title }}
{{params_vars_name}} and their sled, with a combined mass of ${{params_m}}$ $\rm{kg}$, slide ${{params_l}}$ $\rm{m}$ down a hill that makes an angle of ${{params.ang_horiz}}^\circ$ with the horizontal.
They feel a friction force from the snow $F\_{fr} = {{params_fr}}$ $\rm{N}$ and another force from the wind $F\_{wind} = {{params_fwind}}$ $\rm{N}$ blowing at ${{params.ang_wind}}^\circ$ below the horizontal from the top of the hill toward the bottom.

For reference, below is a picture of a sled.

<img src="Sled.png" alt= "Picture of a sled" width="260" height="160">

## Part 1

How much work is done by gravity $W_g$ by the time {{params_vars_name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 2

How much work $W\_{fr}$ is done by friction by the time {{params_vars_name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 3

How much work $W_w$ is done by the wind by the time {{params_vars_name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 4

If {{params_vars_name}}'s inital speed at the top of the hill is $v_i = {{params.v_i}}$ $\rm{m/s}$, what is their speed $v_f$ at the bottom of the hill?

If you are not able to get an answer for Part 3, you can still get marks for Part 4. Use $W_w = 10$ $\rm{kJ}$ to continue answering Part 4.

### Answer Section

Please enter in a numeric value in {{ params.vars.units_4 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)