---
title: Curvilinear Motion of Race Car
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
difficulty:
- undefined
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- JR
- APSC181
- RG
assets:
- CurvRaceCar.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params_vars_title: Curvilinear Motion of Jet
    params_r: 300
    params_va: 11
    params_vad: 5
    params_s: 12
---
# {{ params_vars_title }}
<img src="CurvRaceCar.png" width=90%>

A circular racetrack has a radius of $r = {{ params_r }} \ \rm{m}$.
A race car races at a speed of $v = {{ params_va }} \ \rm{m/s}$.
For a short distance starting at $s = 0 \ \rm{m}$, the race car increases its velocity at $\dot v = {{ params_vad }}.s \ \rm{m/s^2}$.\
What is the speed and magnitude of its acceleration when it has moved $s = {{ params_s }} \ \rm{m}$

## Part 1

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 2

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)