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
myst:
  substitutions:
    params_vars_name: Abbas
    params_vars_title: Motion of watermelon
    params_vars_units1: ${m/s}^2$
    params_vars_units2: $s$
    params_signa: +
    params_signb: +
    params_signc: '-'
    params_a: 1
    params_b: 5
    params_c: 8
    params_part4_ans1_value: The speed is increasing
    params_part4_ans2_value: The speed is decreasing
    params_part4_ans3_value: There is not enough information to tell
---
# {{ params_vars_title }}
The position $x$ of a watermelon as a function of time $t$ is given by $x(t) = {{ params_signa }}{{ params_a }}t^2 {{ params_signb }}{{ params_b}}t {{params_signc }}{{ params_c }}$ where $x$ is in $m$ and $t$ is in $s$.

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

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 3

What is the acceleration $a$ of the watermelon as a function of time?

_Hint: Assume that the units are $m \over s^2$. There is no need to include them in your equation._

Use the following table as a reference.

| For | Use |
|-----|-----|
| $t$ | t   |

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 4

Is the speed of the watermelon increasing or decreasing at $t = 0$ $s$?

### Answer Section

- {{ params_part4_ans1_value}}
- {{ params_part4_ans2_value}}
- {{ params_part4_ans3_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)