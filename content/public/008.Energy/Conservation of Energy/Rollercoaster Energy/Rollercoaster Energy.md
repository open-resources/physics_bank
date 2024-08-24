---
title: Rollercoaster Energy
topic: Energy
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 8.2.1.0
- 8.2.1.1
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
- RG
- PJ
assets:
- RollercoasterEnergy.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max}= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_b= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Rollercoaster Energy
        units: m/s
      m: 956
      r: 13
      h: 63
      d: 47
---
# {{ params.vars.title }}
A rollercoaster ride moves a car with a mass of ${{params.m}}\ \rm{kg}$ to point $A$ at a height $h_A = {{params.h}} \ \rm{m}$. At point $A$, the car is at rest, and then goes down the path through a loop of radius ${{params.r}} \ \rm{m}$. Point $B$ is at a height of $h_B = {{params.d}} \ \rm{m}$.

<img src="RollercoasterEnergy.png" width=700 alt="A rollercoaster track with max height h and a loop with height d." >

## Part 1

What is the maximum possible speed of the rollercoaster?

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Part 2

What is the speed at point $B$?

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)