---
title: Speed of a Clock Hand
topic: Kinematics(2D and 3D)
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.3.1.1
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
- unknown
assets:
- Clock.png
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
    label: $v_x= $
    suffix: $\rm{m/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: $\rm{m/s}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_z= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Speed of a Clock Hand
        units: m/s
      R: 0.39
      theta: 189
      alpha: 39
---
# {{ params.vars.title }}
<img src="Clock.png" width=100%>

It is well known that the second hand on a clock rotates at $1 \ \rm{RPM}$.
In the picture above, an analog clock sits slanted, making it easier for a person at a desk to read.
Take the radius of the second hand to be $R = {{ params.R }} \ \rm{m}$, $\alpha = {{ params.alpha }} ^{\circ}$, $\theta = {{ params.theta }} ^{\circ}$

## Part 1

What would the magnitude of velocity be for the end of the seconds hand?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What would the x-component of velocity be?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

What would the y-component of velocity be?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

What would the z-component of velocity be?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)