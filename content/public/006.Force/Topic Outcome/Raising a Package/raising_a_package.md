---
title: Raising a Package
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 13, Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
- APSC 181 - LA
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
substitutions:
  params:
    vars:
      title: Raising a Package
      units: mm
    v_a: 320
    t: 8
---
# {{ params.vars.title }}

## Question Text

<img src="L13Q1.png" width=60%>

How far does the weight $W$ rise in {{params.t}} seconds if the motor wraps the cable at a constant rate of ${{params.v_a}} mm/s$?

### Answer Section

Please enter an integer value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)