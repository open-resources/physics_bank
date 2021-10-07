---
title: Pendulum on a Downhill Cart
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 14, Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
- APSC 181 - LA
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
      title: Pendulum on a Downhill Cart
      units: ^{\circ}
    a: 7
    theta: 10
---
# {{ params.vars.title }}

## Question Text

<img src="L14Q3.png" width=80%>

A pendulum is attached to a cart moving up hill, and is free to swing in the vertical plane of the cart.
If the cart has a constant acceleration $a = {{params.a}}m/s^2$ up the hill, which is inclined at ${{params.theta}}^{\circ}$,
then what is the angle $\beta$ created by the pendulum after all startup movement has ceased?

### Answer Section

Please enter an numerical value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)