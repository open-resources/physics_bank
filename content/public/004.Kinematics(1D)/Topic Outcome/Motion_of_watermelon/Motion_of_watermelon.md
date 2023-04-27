---
title: Motion of watermelon
topic: Kinematics(1D)
author: Jake Bobowski
source: 2017 Midterm Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
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
    label: $v = $
    variables: t
    weight: 1
    allow-blank: true
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_0 = $
    suffix: $s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: ' '
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      name: Abbas
      title: Motion of watermelon
      units1: ${m/s}^2$
      units2: $s$
    signa: +
    signb: '-'
    signc: '-'
    a: 5
    b: 7
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
The position $x$ of a watermelon as a function of time $t$ is given by $x(t) = {{ params.signa }}{{ params.a }}t^2 {{ params.signb }}{{ params.b}}t {{params.signc }}{{ params.c }}$ where $x$ is in $m$ and $t$ is in $s$.

## Part 1

What is the velocity $v$ of the watermelon as a function of time?

_Hint: Assume that the units are $m \over s$. There is no need to include them in your equation._

Use the following table as a reference.

| For | Use |
|-----|-----|
| $t$ | t   |

### Answer Section

## Part 2

At what time $t_0$ is the watermelon at rest? (Negative valuse of $t$ are not considered physically meaningful and will not be accepted as an answer. Enter -1 if the watermelon is never at rest.)

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 3

What is the acceleration $a$ of the watermelon as a function of time?

_Hint: Assume that the units are $m \over s^2$. There is no need to include them in your equation._

Use the following table as a reference.

| For | Use |
|-----|-----|
| $t$ | t   |

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 4

Is the speed of the watermelon increasing or decreasing at $t = 0$ $s$?

### Answer Section

- {{ params.part4.ans1.value}}
- {{ params.part4.ans2.value}}
- {{ params.part4.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)