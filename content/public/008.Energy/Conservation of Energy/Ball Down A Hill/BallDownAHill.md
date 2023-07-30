---
title: Ball Down A Hill
topic: Energy
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 8.5.1.1
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
- APSC181
- PJ
assets:
- BallDownAHill.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $h= $
    suffix: $\rm{m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: Ball Down A Hill
    params_d: 2.22
    params_theta: 22
---
# {{ params_vars_title }}
A ball, initially at rest, rolls down a hill slanted $\theta = {{params_theta}}^{\circ}$.
After traveling a horizontal distance $d = {{params_d}} \ \rm{m}$, it moves up a curve whose height follows the equation $h(x) = \frac{x^2}{2}$.

<img src="BallDownAHill.png" width=500 alt="A ball rolls down a hill slanted theta degrees up. At the end of that hill the path curves upwards." >

## Part 1

To what height $h$ does the ball make it up the curve?
Neglect friction, and assume a smooth transition from one section to the other.

### Answer Section

Please enter in a numeric value in m.

## Part 2

To what horizontal distance $x$ does the ball travel from the start of the curve?

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)