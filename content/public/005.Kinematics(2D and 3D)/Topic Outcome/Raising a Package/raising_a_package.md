---
title: Raising a Package
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 13, Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.9.1.0
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- AP
- APSC181
- Lecture Activities
assets:
- L13Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $h=$
    suffix: $mm$
    weight: 1
    allow-blank: true
myst:
  substitutions:
    params_vars_title: Raising a Package
    params_vars_units: mm
    params_v_a: 318
    params_t: 3
---
# {{ params_vars_title }}

## Question Text

<img src="L13Q1.png" width=60%>

How far does the weight $W$ rise in {{params_t}} seconds if the motor wraps the cable at a constant rate of ${{params.v_a}} mm/s$?

### Answer Section

Please enter an integer value in ${{ params_vars_units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)