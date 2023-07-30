---
title: Cricket On Moving Ship
topic: Kinematics(2D and 3D)
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.3
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
- AZ
- JR
- APSC181
assets:
- Cricket.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^{\circ}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Cricket on a Moving Ship
    params_vars_units: m/s
    params_v: 13
    params_h: 10
    params_u: 42
    params_x: 140.58207419828975
---
# {{ params_vars_title }}
<img src="Cricket.png" width=85%>

A group of students are playing a game of cricket atop a ship moving at $v = {{ params_v }} \ \rm{m/s}$.
The cricket ball is thrown with velocity $u = {{ params_u }} \ \rm{m/s}$, from an elevated point on the ship, $h = {{ params_h }} \ \rm{m}$ up.

## Part 1

What is the initial projection angle($\theta$) relative to the horizontal of the ball if it travels the entire length of the moving ship, which is $x = {{ params_x }} \rm{m}$ long?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What is the absolute projection speed of the ball?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)