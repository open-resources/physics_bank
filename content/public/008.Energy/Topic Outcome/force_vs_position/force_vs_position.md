---
title: Force vs Position Graph
topic: Energy
author: Jake Bobowski
source: 2017 Final Q15
template_version: 1.1
attribution: standard
outcomes:
- 8.2.1.0
- 9.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets:
- q15image.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: J
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Force vs Position Graph
      units1: m/s
      units2: m
      units3: J
    m: 5.0
    v: -3.5
---
# {{ params.vars.title }}
The graph below shows the net force on a particle as a function of its position. The mass of
the particle is m = {{params.m}} $kg$.

<img src="q15image.png" width=400 alt="Force vs position graph">
## Part 1

If the particle has a velocity of $v_x =$ {{params.v}} m/s when $x =$ 0 $m$, what is the particle's speed
when $x =$ 3.0 $m$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.
## Part 2

At what value of x (in meters) is does the particle have the maximum kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.
## Part 3

What is the particle's maximum kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.units3 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)