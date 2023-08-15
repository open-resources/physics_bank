---
title: Car Suspension System
topic: Work
author: Ammar Zavahir
source: original
template_version: 1.0
attribution: standard
outcomes:
- 6.12.2.0
- 9.2.1.1
- 8.5.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
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
    label: $ v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $\rm{N/m}$
myst:
  substitutions:
    params_vars_title: Car Suspension System
    params_m: 1314
    params_r: 77
    params_x: 165
    params_u: 99.9
    params_v: 97.9
---
# {{ params_vars_title }}
A car is moving over a hump in the road with a constant speed $v \  \rm{ms^{-1}}$.

<img src="part1.png" width=800>

## Part 1

What is the maximum speed, $v$ with which the car can move without it losing contact with the road at the top of the hump.
<br>Treat the car as a particle. Neglect friction and air resistance.
<br>
$m = {{ params_m }} \ \rm{kg}$, $R = {{ params_r }} \ \rm{m}$

### Answer Section

Please enter value of $v$ in $m/s$.

## Part 2

In order to reduce the likelihood of loss of contact when navigating the curvature of the hump, a suspension system consisting of a series of springs is connected to the wheels to absorb some of the excess kinetic energy of the vehicle before it encounters the circular arc.
<br>If the maximum compression ($\delta x$) of the springs are ${{ params_x }}\ \rm{mm}$ at the top of the hump, what must the equivalent spring stiffness constant, $k$, be if the speed of the car goes at the top of the hump is ${{ params_v }} \ \rm{km/h}$.
<br>
The speed of the car just before the hump is ${{ params_u }} \ \rm{km/h}$. The height of the hump above the ground plane is $0.5 \ \rm{m}$.

<img src="part2.png" width=800>

### Answer Section

Please enter the value of $k$ in $Nm^{-1}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)