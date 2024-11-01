---
title: Moving Crates
topic: Force
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.5.1.3
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
- RG
- JR
- APSC181
assets:
- MovingCrates.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F = $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      vars:
        title: Moving Crates
        units: N
      m1: 14
      m2: 11
      theta: 23
      vo: 1
---
# {{ params.vars.title }}
A mover is pushing crates $\rm{A}$ and $\rm{B}$ up a hill, in order for them to slide down the hill for loading. Crate $A$ has a mass of $m_1 = {{ params.m1 }} \ \rm{kg}$ and crate $B$ has a mass of $m_2 = {{ params.m2 }} \ \rm{kg}$. The hill has an inclination of $\theta = {{ params.theta }}^\circ$, and is frictionless.

<img src="MovingCrates.png" width=800>

## Part 1

What is the force needed to push both crates up the hill with no acceleration?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

The mover gets tired, and decides to leave the crates alone for a moment to take a break. What is the magnitude of acceleration the crates now face?

### Answer Section

Please enter in a numeric value in m/s$^2$.

## Part 3

If the crates were left with an velocity of $v_o = {{ params.vo }} \ \rm{m/s}$, how far up the hill will they still go?

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)