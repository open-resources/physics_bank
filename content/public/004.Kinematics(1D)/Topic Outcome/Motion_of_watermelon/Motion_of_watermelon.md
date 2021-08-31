---
title: Motion of watermelon
topic: Kinematics(1D)
author: Jake Bobowski
source: 2017 Midterm Q4
template_version: 1.1
attribution: standard
outcomes:
- 1.7.2.4
- 4.5.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
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
    weight: 1
    allow-blank: true
    label: $t_o= $
    suffix: $s$
    comparison: sigfig
    digits: 1
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 1
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      name: Lorenzo
      title: Motion of watermelon
      units1: ${m/s}^2$
      units2: $s$
    a: 3
    b: 7
    c: 8
    part4:
      ans1:
        value: The speed is increasing
      ans2:
        value: The speed is decreasing
      ans3:
        value: There is not enough information to tell
---
# {{ params.vars.title }}
The position of a watermelon is given by:
$x(t) = {{ params.a }}t^2 - {{ params.b}}t - {{ params.c }}$
where $x$ is in meters and $t$ is in seconds.

## Part 1

What is the velocity of the watermelon as a function of time?

_Hint: Assume that the units are $m \over s$. There is no need to include them in your equation._

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| $Variable$ | Use   |
|----------|-------|
| $t$  | t  |
| $g$      | g     |
| $\theta$ | theta |

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

At $t=0$ is the speed of the watermelon increasing or decreasing?

### Answer Section

- {{ params.part4.ans1.value}}
- {{ params.part4.ans2.value}}
- {{ params.part4.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)