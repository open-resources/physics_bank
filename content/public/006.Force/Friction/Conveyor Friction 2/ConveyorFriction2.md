---
title: Conveyor Friction 2
topic: Kinematics(2D and 3D)
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.9.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC181
- JR
assets:
- ConvFric2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_c = $
    suffix: $\rm{ft/s}$
myst:
  substitutions:
    params_vars_title: Conveyor Friction 2
    params_theta: 27
    params_W: 27
    params_v: 4
    params_C: 1.5
---
# {{ params_vars_title }}
<img src="ConvFric2.png" width=90%>

A conveyor belt, angled at $\theta = {{ params_theta }}^{\circ}$, carries packages up an incline.
The package aboard it slips and begins moving downwards at a constant speed $v_p = {{ params_v }} \ \rm{ft/s}$ relative to the ground.
Given that friction can be found as $F = Cv\_{PC}$, where $C$ is a constant ${{ params_C }}$.
$v\_{PC}$  is the relative velocity of the package to the conveyor.\
The package has a weight of $W = {{ params_W }} \ \rm{lb}$.

## Part 1

What is the speed of the conveyor?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)