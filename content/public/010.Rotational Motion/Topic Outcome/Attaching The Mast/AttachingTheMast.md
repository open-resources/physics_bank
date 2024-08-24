---
title: Attaching The Mast
topic: Rotational Motion
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 10.1.1.1
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
- JR
assets:
- AttachingTheMast.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_2= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Attaching The Mast
        units: m/s
      v: 5
      theta: 126
      d1: 2
      d2: 4
---
# {{ params.vars.title }}
<img src="AttachingTheMast.png" width=400>

A common problem when assembling a mining drill is attaching the mast tower.
A common method to attach the mast is to attach a chain to the feed cylinders and spin the mast up.
If the feed cylinder lowers at a rate of $v_1 = {{ params.v }} \ \rm{m/s}$, then what is the angular speed the tip of the tower is moving at in the instant shown?
The distance from the chain to the pivot tower is $d_1 = {{ params.d1 }} \ \rm{m}$, the distance from the pivot tower to the end of the mast is $d_2 = {{ params.d2 }} \ \rm{m}$, and the angle between the chain and pivot tower is $\theta = {{ params.theta }} ^{\circ}$

## Part 1

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)