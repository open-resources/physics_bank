---
title: Parachuter
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.0
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
- Parachute.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $\rm{km}$
myst:
  substitutions:
    params:
      vars:
        title: Parachuter
        units: m/s
      v: 456
      theta: 11
      h: 609
---
# {{ params.vars.title }}
<img src="Parachute.png" width=100%>

A parachuter jumps out of a plane at height $h = {{ params.h }} \ \rm{m}$, with a goal of landing at a marked spot to meet a group of people.  The plane has a velocity $v = {{ params.v }} \ \rm{km/hr}$ with angle $\theta = {{ params.theta }}^{\circ}$

## Part 1

At what time will the parachuter land in the marked spot?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the distance the parachuter traveled?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)