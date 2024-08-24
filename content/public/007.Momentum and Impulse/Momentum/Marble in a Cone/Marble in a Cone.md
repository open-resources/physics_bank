---
title: Marble in a Cone
topic: Momentum and Impulse
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.3.0
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
- Marble Around a Cone.jpg
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\lvert v \rvert= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^{\circ}$
myst:
  substitutions:
    params:
      vars:
        title: Marble in a Cone
        units: m/s
      v: 1.39
      H: 6.25
      R: 2.527
      r: 1.937
---
# {{ params.vars.title }}
<img src="Marble Around a Cone.jpg" width=800>

A marble is spun in a cone that has a radius ${{params.R}}\ \rm{m}$ and height ${{params.H}}\ \rm{m}$ with an initial velocity of ${{params.v}}\ \rm{m/s}$ tangent to the horizontal rim of the cone. As the marble spins around the bowl, its rotational radius r shrinks. As the marble descends, where r  = ${{params.r}}\ \rm{m}$, the velocity vector makes an angle $\theta$ with the horizontal. Determine the new velocity magnitude and $\theta$ in degrees.

## Part 1

What is $\lvert v \rvert$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is $\theta$?

### Answer Section

Please enter in a numeric value in $\circ$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)