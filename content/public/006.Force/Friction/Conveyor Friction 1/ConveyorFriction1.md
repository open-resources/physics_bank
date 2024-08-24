---
title: Conveyor Friction 1
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
- ConvFric1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\mu = $
    suffix: $ \ $
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Conveyor Friction 1
      theta: 33
      v: 1
      part2:
        ans1:
          value: Greater than before
        ans2:
          value: The same
        ans3:
          value: Less than before
---
# {{ params.vars.title }}
<img src="ConvFric1.png" width=90%>

A conveyor belt, angled at $\theta = {{ params.theta }}^{\circ}$, carries packages up an incline.
What must the coefficient of friction be to prevent the packages from slipping as they move?
Assume the conveyor belt runs at $v = {{ params.v }} \ \rm{ft/s}$  and the package has a smooth transition onto the belt.

## Part 1

What is the coefficient of friction?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

If the direction of the conveyor belt was downwards, would the coefficient need to be greater, less than, or the same?

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)