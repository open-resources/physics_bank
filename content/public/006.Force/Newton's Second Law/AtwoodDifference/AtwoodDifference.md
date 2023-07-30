---
title: Atwood Machine Difference
topic: Force
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.6.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC181
- JR
assets:
- AtwoodDifference.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_A = $
    suffix: $\rm{ft/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_B = $
    suffix: $\rm{ft/s^2}$
myst:
  substitutions:
    params_vars_title: Atwood Machine Difference
    params_Wa: 25
    params_Wb: 49
---
# {{ params_vars_title }}
<img src="AtwoodDifference.png" width=90%>

Examine the scenario in the above image of an Atwood Machine.
In the second image, the box has been replaced by a force such that the tension in the rope is equal to the weight of box B.
Calculate the acceleration of the box A in both scenarios.
Take $W_A = {{ params_Wa }} \ \rm{lb}$, and $W_B = {{ params_Wb }} \ \rm{lb}$
Take upward motion to be positive.

## Part 1

What is the acceleration in Scenario A?

### Answer Section

Please enter in a numeric value in $\rm{ft/s^2}$.

## Part 2

What is the acceleration in Scenario B?

### Answer Section

Please enter in a numeric value in $\rm{ft/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)