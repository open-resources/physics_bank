---
title: Travelling Wave Displacement
topic: Waves
author: John Hopkinson
source: Phys122 2022S Tutorial 11 Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 16.1.1.1
- 16.1.1.3
difficulty:
- medium
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- medium
tags:
- JR
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $A = $
    suffix: $\rm{cm}$
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Travelling Wave Displacement
      A: 2
      k: 7
      omega: 8
      part2:
        ans1:
          value: The positive x direction.
          feedback: Try setting the phase equal to a constant and differentiating
            the phase implicitly with respect to time. What is the sign of $v = v_{x}
            = \frac{dx}{dt}$ ?
        ans2:
          value: The negative x direction.
          feedback: Yes, you can see this by setting the phase equal to a constant
            and differentiating the phase implicitly with respect to time to find
            that $v = v_{x} = \frac{dx}{dt}$ is negative.
---
# {{ params.vars.title }}
$D(x,t) = {{ params.A }}\cos({{ params.k }}x+ {{ params.omega }}t)$ describes the displacement $D$ in $\rm{cm}$ of a travelling sinusoidal wave as a function of displacement $x$ in $\rm{cm}$ and time $t$ in $\rm{s}$.

## Part 1

What is the amplitude $A$ of the travelling wave?

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 2

In what direction is the travelling wave moving?

### Answer Section

- {{ params.part2.ans1}}
- {{ params.part2.ans2}}

## Part 3

At what speed $v$ is the travelling wave moving?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)