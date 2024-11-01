---
title: Arrow Shot Rotational Motion
topic: Kinematics(2D and 3D)
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.2
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
- JR
- APSC181
assets:
- Arrow Shot Rotational Motion.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot r = $
    suffix: $\rm{ft/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot \theta = $
    suffix: $\rm{rad/s}$
myst:
  substitutions:
    params:
      vars:
        title: Arrow Shot Rotational Motion
        units: ft/s
      v: 134
      t: 7.57
      d: 61
---
# {{ params.vars.title }}
<img src="Arrow Shot Rotational Motion.png" width=800>

An archer shoots an arrow straight up into the air to hit a bird, with an initial speed $v = {{ params.v }}$ $\rm{ft/s}$.
Their friend stands $d = {{ params.d }}$ $\rm{ft}$ away.
Find the following information. Assume the arrow launches from the horizontal line of site of the friend.

## Part 1

At $t = {{ params.t }}$ $\rm{s}$, what is $\dot r$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

At $t = {{ params.t }}$ $\rm{s}$, what is $\dot \theta$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)