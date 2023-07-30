---
title: Total Force in Deep Space
topic: Force
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 12.2.1.1
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
- APSC181-2023MD
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\lvert F \rvert= $
    suffix: N
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $\circ $
myst:
  substitutions:
    params_vars_title: Total Force in Deep Space
    params_vars_units: N
    params_vars_string_1: Object A is a cube with sides 1.09 m. It has a density of
      18000.0 $\frac{kg}{m^{3}}$ and it is at position $(4,1)$.
    params_vars_string_2: The other one, Object B, is a sphere with radius 1.06 m.
      It has a density of 21500.0 $\frac{kg}{m^{3}}$ and it is at position $(1,-2)$.
    params_m: 3600
---
# {{ params_vars_title }}
There are two objects surrounding our spaceship in deep space. {{ params.vars.string_1}} {{ params.vars.string_2}} Our space shuttle has a mass of {{ params_m}} tons. Find the total gravitational force on the spaceship.

Note:
Volume of a Sphere: $V = \frac{4}{3}.\pi.r^3$
Volume of a Cube: $V = a^3$
Volume of a Cylinder: $V = \pi . r^{2} . h$
Volume of a Cone: $V = \frac{1}{3} . \pi . r^{2} . h$

## Part 1

What is the magnitude of the total gravitational force on our spaceship?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What is the direction of the total gravitational force, in degrees? (positive values only)

### Answer Section

Please enter in a numeric value in degrees.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)