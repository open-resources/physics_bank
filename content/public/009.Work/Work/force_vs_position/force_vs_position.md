---
title: Force vs Position Graph
topic: Work
author: Jake Bobowski
source: 2017 Final Q15
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.2.1.0
- 9.2.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- MP
- JR
assets:
- q15image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $\rm{m}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $\rm{J}$
myst:
  substitutions:
    params_vars_title: Force vs Position Graph
    params_m: 0.5
    params_v: 0.5
    params_x: 0.5
---
# {{ params_vars_title }}
The graph below shows the net force on a particle in the $x$-direction as a function of its position along the $x$-axis.
The mass of the particle is $m = {{params_m}} \rm{kg}$.

<img src="q15image.png" width=400 alt="Force vs position graph">

## Part 1

If the particle has a velocity of $v_x = {{ params_v }} \rm{m/s}$ when $x = 0 \rm{m}$, what is the particle's speed
when $x = {{ params_x }} \rm{m}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

At what value of x does the particle have its maximum kinetic energy?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Part 3

What is the particle's maximum kinetic energy?

### Answer Section

Please enter in a numeric value in $\rm{J}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)