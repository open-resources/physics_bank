---
title: Constrained Curvilinear Motion Velocity
topic: Kinematics(2D and 3D)
author: Ernest Goh
source: Original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- Constrained Curvilinear Motion.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Constrained Curvilinear Motion Velocity
    params_t: 6.8
    params_C1: 7
    params_C2: 4
    params_N1: 2
    params_N2: 2
    params_A1: 11
    params_A2: 29
---
# {{ params_vars_title }}
<img src="Constrained Curvilinear Motion.png" width=600>

It can be seen that the $x$ and $y$ motions of guides $\rm{A}$ and $\rm{B}$ with right angle slots control the curvilinear motion of the connecting pin $\rm{P}$, which slides in both slots.
<br>
The motions are governed by:
<br>
$x = {{params_A1}} + \frac{1}{{{params_C1}}}t^{{{params_N1}}}$
<br>
$y = {{params_A2}} + \frac{1}{{{params_C2}}}t^{{{params_N2}}}$

## Part 1

What is the magnitude of the velocity of pin P at time $t = {{params_t}} \ \rm{s}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)