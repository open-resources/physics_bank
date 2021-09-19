---
title: Rotating Bar
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 11, Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.7.1.2
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
- AP
- APSC 181 - LA
assets:
- L11Q1.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\ddot{r}= $
    suffix: $mm/s^2$
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\ddot{\theta}= $
    suffix: $rad/s^2$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Rotating Bar
    v: 15
    h: 163
    x: 67
    a: 3
---
# {{ params.vars.title }}
<img src="L11Q1.png" width=85%>

The bar $OA$ is rotated by a collar $C$ which moves a pin $P$ with velocity of $v = {{params.v}} mm/s$.
The velocity of the collar $C$ is decreasing at a rate of ${{params.a}} mm/s^2$ in the moment shown.
Determine the following values where $r = \bar{OP}$, $h = {{params.h}} mm$ and $x = {{params.x}} mm$.

## Part 1

Determine the value of $\ddot{r}$

### Answer Section

## Part 2

Determine the value of $\ddot{\theta}$

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)