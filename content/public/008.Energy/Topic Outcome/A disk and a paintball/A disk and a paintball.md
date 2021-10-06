---
title: A Disk and a Paintball
topic: Physics in General
author: Jake Bobowski
source: 2017 Midterm 2 Section 002 Q6
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.5.1.3
- 7.5.1.4
- 7.5.1.9
- 8.2.1.1
- 7.5.1.7
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
- PW
assets:
- 2017Mid2S002Q6.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta K= $
    suffix: $J$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta K= $
    suffix: $J$
substitutions:
  params:
    vars:
      title: Distance travelled
      unit1: $J$
      unit2: $m/s$
    m_d: 0.06
    m_b: 0.047
    v: 17.0
---
# {{ params.vars.title }}
A {{ params.m_d }} $kg$ disk initially at rest in the Earth reference frame is free to move parallel to a horizontal bar through a hole in the disk's centre. The disk is struck face-on by a {{ params.m_b }} $kg$ paintball traveling at {{ params.v }} $m/s$.

<img src="2017Mid2S002Q6.png" alt="Figure of a paintball travelling to the right hitting a disk which has a horizontal bar going through its centre." width=300>

## Part 1

According to an observer in the Earth reference frame, what is the change in the system's kinetic energy after the ball hits the disk? Take the system to be the paintball and the disk and assume that after the collision all of the paint from the paintball sticks to the disk.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

Before the paintball hits the disk, what is the velocity of the system's zero-momentum reference frame relative to the Earth reference frame?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 3

What would an observer in the zero-momentum reference frame measure for the system's change in kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)