---
title: Person running in rain
topic: Kinematics(2D and 3D)
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.3
- 5.8.1.2
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
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{man}= $
    suffix: $\rm{mph}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{r/m}= $
    suffix: $\rm{mph}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_v_r1: 21
    params_a: 39
    params_v_r2: 6
    params_theta: 51
---
# Person Running in Rain
A man without an umbrella is running along a straight road with constant speed whilst it is raining.

<img src="part1.png" width=600>

## Part 1

If the rain droplets are falling with a terminal velocity of $v\_{rain} = {{ params.v_r1 }}\ \rm{mph}$ at an angle of $\alpha = {{ params_a }}^{\circ}$ from the vertical, what must the speed of the person be such that the rain does not hit his face or clothes?
<br>
Treat the man and rain droplets as particles. Assume the man's face is always oriented parallel to the horizontal.

### Answer Section

Please enter the speed in $\rm{mph}$.

## Part 2

What is the speed of the rain droplets relative to the man?

### Answer Section

Please enter the speed in $mph$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)