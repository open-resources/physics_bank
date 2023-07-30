---
title: Railcar Softball Pitch
topic: Kinematics(2D and 3D)
author: Ammar Zavahir
source: Webwork
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.3
- 5.3.1.0
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
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{ball}= $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\alpha= $
    suffix: $\rm{^{\circ}}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_v_r: 25
    params_v_b_r: 22
    params_theta: 154
---
# Railcar Softball Pitch
A softball pitcher stands atop a moving railcar which is moving in a straight line with a speed of $v\_{railcar} = {{ params.v_r }}\ \rm{m/s}$ as illustrated in the figure below.

<img src="part1.png" width=600>

## Part 1

If the pitcher throws a ball horizontally at a speed of $v\_{ball/railcar} = {{ params.v_b_r }}\ \rm{m/s}$ relative to the railcar at an angle $\theta = {{ params_theta }}\ \rm{^{\circ}}$ measured counterclockwise from the direction of motion of the car, what is the speed($v\_{ball}$) of the ball relative to the ground at the instant of projection?
<br>

### Answer Section

Please enter the value of $v\_{ball}$ in $\rm{m/s}$.

## Part 2

What is the angle $\alpha$, measured counter-clockwise, that the velocity of the ball relative to the ground makes with the direction of motion of the railcar?

<img src="part2.png" width=600>

### Answer Section

Please enter the value of $\alpha$ in $\rm{^{\circ}}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)