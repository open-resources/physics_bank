---
title: Supply Crate Drop
topic: Force
author: James Ropotar
source: original
template_version: 1.4
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.9.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC181
- JR
assets:
- SupplyCrate.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T = $
    suffix: $\rm{N}$
myst:
  substitutions:
    params_vars_title: Supply Crate Drop
    params_mu: 0.49
    params_mb: 24
    params_Ma: 48
    params_x: 4
    params_y: 1
---
# {{ params_vars_title }}
<img src="SupplyCrate.png" width=90%>

When workforce is limited, solutions are needed to reduce the number of people needed.
An engineer comes up with the system in the diagram above, which seeks to autonomously limit the acceleration of a supply crate into a pit, without it needing to be manually controlled.
Find the acceleration of the supply crate, and the tension in the rope.
Assume the system starts from rest, the top block has a mass $M = {{ params_Ma }} \ \rm{kg}$, the supply crate has a mass $m = {{ params_mb }} \ \rm{kg}$, and the coefficient of static friction is equal to the kinetic friction, with a value of ${{ params_mu }}$.
Assume $x = {{ params_x }}$ and $y = {{ params_y }}$

## Part 1

What is the acceleration?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Part 2

What is the tension?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)