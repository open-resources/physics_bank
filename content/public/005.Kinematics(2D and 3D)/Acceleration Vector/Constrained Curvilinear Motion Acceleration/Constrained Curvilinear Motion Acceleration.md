---
title: Constrained Curvilinear Motion Acceleration
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
    label: $a = $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Constrained Curvilinear Motion Acceleration
      t: 3.4
      N: 0.21
      M1: 2.2
      M2: 8.8
---
# {{ params.vars.title }}
<img src="Constrained Curvilinear Motion.png" width=600>

There is a drone that is surveying the park. The drone turns on and flies vertically upward to a height $h$. Afterwards, the drone flies around in a pre-programmed path, while remaining at a constant height.
<br>
The path of the drone is governed by the following equations:
<br>
$\theta(t) = 2\pi sin^3({{params.M1}}t + \frac{\pi}{2})$
<br>
$r(t) = {{params.N}} cos^4({{params.M2}}t + \frac{\pi}{2})$
<br>
The origin point of this coordinate system is at the location where the drone starts the path as indicated on the figure.
<br>
Treat the drone as a particle which is constrained in the plane parallel to the ground at the height $h$.

## Part 1

What is the magnitude of the acceleration of the drone at time $t = {{params.t}} \ \rm{s}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)