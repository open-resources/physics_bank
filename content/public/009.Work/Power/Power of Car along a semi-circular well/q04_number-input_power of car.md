---
title: Power of car along a semi-circular well
topic: Work
author: Ammar Zavahir
source: original
template_version: 1.0
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $P= $
    suffix: $\rm{kW}$
    comparison: sigfig
    digits: 2
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
    fixed-order: true
    hide-letter-keys: true
myst:
  substitutions:
    params_vars_title: Power of car along a circular arc
    params_m: 2500.0
    params_v: 91
    params_a: 56
    params_part2_ans1_value: A
    params_part2_ans2_value: B
    params_part2_ans3_value: C
---
# {{ params_vars_title }}
A car is travelling up a smooth semi-circular slope with a constant speed of ${{ params_v }}\ \rm{kmh^{-1}}$.

<img src="part1.png" width=600>

## Question Text

What is the additional power which has to be developed in the engine to keep the car moving at this speed at $\alpha = {{ params_a }}^{\circ}$ mark?
<br>
Neglect air resistance. Treat the car as a particle with mass $M= {{ params_m }}\ \rm{kg}$

### Answer Section

Please enter in a numeric value in W.

## Part 2

At what point along the circular arc is the power developed by the engine the maximum if the speed is kept constant?

<img src="part2.png" width=600>

### Answer Section

- {{ params_part2_ans1_value}}
- {{ params_part2_ans2_value}}
- {{ params_part2_ans3_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)