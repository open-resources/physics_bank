---
title: Displacement and Distance of a particle
topic: Kinematics(1D)
author: Peyman Yousefi
source: APSC 181, Lecture 3, Q1
template_version: 1.1
attribution: standard
outcomes:
- 4.4.1.0
- 4.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
- APSC 181 - LA
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $s= $
    suffix: cm
    comparison: sigfig
    digits: 2
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: cm
    comparison: sigfig
    digits: 2
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Displacement and Distance of a particle
      units: cm
    seconds: 44
---
# {{ params.vars.title }}
The position of a particle in centimeters is given by $s(t) = 20 - 9t + t^2$, where $t$ is in seconds.

## Part 1

Determine the net displacement in the first {{params.seconds}} seconds.

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Part 2

Determine the total distance travelled in the first {{params.seconds}} seconds.

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)