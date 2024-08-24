---
title: Man Vs Box
topic: Momentum and Impulse
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.3.1.3
- 5.9.1.0
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
assets:
- Man vs box.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Man Vs Box
        units: "$\rm{m/s^2}$"
      m: 139
      M: 89
      theta: 60
      h: 1.52
---
# {{ params.vars.title }}
<img src="Man vs box.png" width=700>

In the figure shown is a pulley system with a box attached with mass ${{params.m}}\ \rm{kg}$. On the other side of the pulley is a person with mass ${{params.M}}\ \rm{kg}$ and height ${{params.h}}\ \rm{m}$.
The person leans back at an angle ${{params.theta}}^\circ$  and uses only their weight as leverage on the rope.
Up is negative, down is positive.

## Part 1

What is the acceleration of the box at that moment?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)