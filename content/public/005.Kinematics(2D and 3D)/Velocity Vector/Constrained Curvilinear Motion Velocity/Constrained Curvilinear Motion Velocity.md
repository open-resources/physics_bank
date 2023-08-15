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
    params_N: 0.16
    params_M1: 2.6
    params_M2: 10.4
---
# {{ params_vars_title }}
<img src="Constrained Curvilinear Motion.png" width=90%>

There is a drone that is surveying the park. The drone turns on and flies vertically upward to a height $h$. Afterwards, the drone flies around in a pre-programmed path, while remaining at a constant height.
<br>
The path of the drone is governed by the following equations:
<br>
$\theta(t) = 2\pi sin^3({{params_M1}}t + \frac{\pi}{2})$
<br>
$r(t) = {{params_N}} cos^4({{params_M2}}t + \frac{\pi}{2})$
<br>
The origin point of this coordinate system is at the location where the drone starts the path as indicated on the figure.
<br>
Treat the drone as a particle which is constrained in the plane parallel to the ground at the height $h$.

## Part 1

What is the magnitude of the velocity of the drone at time $t = {{params_t}} \ \rm{s}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)