---
title: Dice on the Mirror
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 14, Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.8
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- AP
- APSC181
- Lecture Activities
assets:
- L14Q3.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $\beta$
    suffix: $^{\circ}$
    weight: 1
    allow-blank: true
substitutions:
  params:
    vars:
      title: Dice on the Mirror
      units: ^{\circ}
    a: 6
    theta: 19
---
# {{ params.vars.title }}

## Question Text

<img src="L14Q3.png" width=80%>

A van drives up a hill, with fuzzy dice attached to the mirror.
If the van constantly accelerates, $a = {{params.a}}m/s^2$, up the hill, which is inclined at ${{params.theta}}^{\circ}$,
then what is the angle $\beta$ created by the dice after all startup movement has ceased?

### Answer Section

Please enter an numerical value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)