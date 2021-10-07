---
title: Force on a Highway Exit
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 15, Q1
template_version: 1.2
attribution: standard
outcomes:
- 6.5.1.3
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- APSC 181 - LA
- JR
assets:
- Force on a Highway Exit.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_b= $
    suffix: $ft/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: $lb$
substitutions:
  params:
    vars:
      title: Force on a Highway Exit
    vami: 59
    vcmi: 20
    W: 4835
    d: 156
    r: 164
---
# {{ params.vars.title }}
<img src="Force on a Highway Exit.png" width=400>

A {{ params.W }}$lb$ truck travels with a speed of ${{ params.vami }}mi/hr$ as it approaches point A. At A, it decelerates uniformly to a speed of ${{ params.vcmi }}mi/hr$ as it passes point C on the horizontal unbanked ramp highway ramp.
$R = {{ params.r }}ft$, $d = {{ params.d }}ft$.

## Part 1

What is the velocity as the truck passes point B?

### Answer Section

Please enter in a numeric value in $ft/s$.

## Part 2

What is the force at point B?

### Answer Section

Please enter in a numeric value in $lb$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)