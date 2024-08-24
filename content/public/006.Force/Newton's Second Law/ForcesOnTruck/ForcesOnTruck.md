---
title: Forces On Truck
topic: Force
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.6.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC181
- JR
assets:
- ForcesOnTruck.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F = $
    suffix: $\rm{N}$
myst:
  substitutions:
    params:
      vars:
        title: Forces on Truck
      MT: 4650
      mc: 1
      theta: 16
---
# {{ params.vars.title }}
<img src="ForcesOnTruck.png" width=90%>

A truck has a golf cart with no brakes on its back bed.
To prevent it from rolling out, a ramp is installed.
What is the maximum acceleration force that the engine can apply before the cart goes over the ramp and falls out?
The mass of the truck is $M = {{ params.MT }} \ \rm{kg}$, the ramp has an angle $\theta = {{ params.theta }}^{\circ}$, and the cart has a mass $m = {{ params.mc }} \ \rm{kg}$.

## Part 1

### Answer Section

Please enter in a numeric value in $\rm{N}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)