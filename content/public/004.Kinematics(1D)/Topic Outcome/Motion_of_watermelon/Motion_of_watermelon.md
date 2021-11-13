---
title: Motion of watermelon
topic: Kinematics(1D)
author: Jake Bobowski
source: 2017 Midterm Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.7.2.4
- 4.5.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- AK
assets: null
part1:
  type: symbolic-input
  pl-customizations:
    label: $v= $
    variables: t
    weight: 1
    allow-blank: true
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_o= $
    suffix: $s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      name: Emilia
      title: Motion of watermelon
      units1: ${m/s}^2$
      units2: $s$
    a: 3
    b: 5
    c: 3
    part4:
      ans1:
        value: The speed is increasing
      ans2:
        value: The speed is decreasing
      ans3:
        value: There is not enough information to tell
---
# {{ params.vars.title }}
The position of a watermelon is given by $x(t) =$ {{ params.a }}$t^2 - ${{ params.b}}$t - ${{ params.c }} where $x$ is in meters and $t$ is in seconds.

## Part 1

What is the velocity of the watermelon as a function of time?

_Hint: Assume that the units are $m \over s$. There is no need to include them in your equation._

Use the following table as a reference.

| For  | Use   |
|----------|-------|
| $t$  | t  |

### Answer Section

## Part 2

At what time, if ever, is the watermelon at rest? (Enter -1 if the watermelon is never at rest)

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 3

What is the acceleration of the watermelon as a function of time?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 4

Is the speed of the watermelon increasing or decreasing at $t=0$ $s$?

### Answer Section

- {{ params.part4.ans1.value}}
- {{ params.part4.ans2.value}}
- {{ params.part4.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)