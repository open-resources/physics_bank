---
title: Drawing Water from a Well
topic: Physics in General
author: Jake Bobowski
source: 2013 Practice Final Q11
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.2.1.2
- 6.1.1.4
- 10.3.2.2
difficulty:
- Medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- PW
- final_exam
assets:
- q11_2013practiceFinal.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T= $
    suffix: $N$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta y= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Drawing Water from a Well
      unit1: $N$
      unit2: $m$
    M: 3.21
    m: 5.08
    R: 0.2
    t: 6.26
---
# {{ params.vars.title }}
As shown in the figure, a solid, uniform, frictionless cylindrical reel of mass $M = $ {{ params.M }} $kg$ and radius $R = $ {{ params.R }} $m$ is used to draw water from a well. A bucket of mass $m = $ {{ params.m }} $kg$ is  attached to a massless cord that is wrapped around the cylinder.

<img src="q11_2013practiceFinal.png" alt="Figure of a bucket attached to a cylindrical reel and a well." width=300>

## Part 1

If the bucket is released from rest at the top of the well, find the tension $T$ in the cord and the acceleration $a$ of the bucket (the cord does not slip on the reel).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

If the bucket falls for {{ params.t }} $s$ before hitting the water, how far does it fall?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)