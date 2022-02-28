---
title: Cars on a track
topic: Rotational Motion
author: Peyman Yousefi
source: APSC 181, Lecture 6 Q1
template_version: 1.1
attribution: standard
outcomes:
- 5.6.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- AP
- APSC 181 - LA
assets:
- L6Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{A}= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{B}= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Cars on a track
      units: $m/s$
    r1: 26
    r2: 34
---
# {{ params.vars.title }}
Two cars travel side by side on an even, unbanked turn on a roadway.
Car A has a turn radius $R\_{1} = {{params.r1}}m$ and Car B has a turn radius $R\_{2} = {{params.r2}}m$.
What is the maximum speed of each car if the centripetal acceleration is restricted to $g$ (Earth's gravitational constant)?

<img src="L6Q1.png" width=85%>

## Part 1

Determine the maximum speed for car A.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Determine the maximum speed for car B.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)