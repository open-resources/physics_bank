---
title: Archer Shooting Arrow
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
- RG
- JR
- APSC181
assets:
- Archer Shooting Arrow.png
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
    label: $v= $
    suffix: $\rm{ft/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: s$\rm{s}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{ft/s}$
myst:
  substitutions:
    params:
      vars:
        title: Archer Shooting Arrow
      v: 169
      thetad: 18
      d: 66
---
# {{ params.vars.title }}
<img src="Archer Shooting Arrow.png" width=800>

An archer shoots an arrow up into the air to hit a bird with an initial speed of $v = {{ params.v }} \ \rm{ft/s}$.
Their friend, who is standing $d = {{ params.d }}\ \rm{ft}$ away, sees the arrow at an angle of $\theta = {{ params.thetad }}^{\circ}$ with respect to the horizontal.

## Part 1

At what time will the friend see the arrow pass by their line of site?

### Answer Section

Please enter in a numeric value in s.

## Part 2

What is the vertical velocity of the arrow at this time?

### Answer Section

Please enter in a numeric value in $\rm{ft/s}$.

## Part 3

The archer misses the bird, causing the arrow to come straight back down.
At what time since fire will the arrow pass the line of site of the friend again?

### Answer Section

Please enter in a numeric value in s.

## Part 4

What will its vertical velocity be at this time?

### Answer Section

Please enter in a numeric value in $\rm{ft/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)