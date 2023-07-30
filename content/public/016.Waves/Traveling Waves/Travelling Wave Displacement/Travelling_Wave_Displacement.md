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
    params_vars_title: Travelling Wave Displacement
    params_A: 5
    params_k: 10
    params_omega: 5
    params_part2_ans1_value: The positive x direction.
    params_part2_ans1_feedback: Try setting the phase equal to a constant and differentiating
      the phase implicitly with respect to time. What is the sign of $v = v_{x} =
      \frac{dx}{dt}$ ?
    params_part2_ans2_value: The negative x direction.
    params_part2_ans2_feedback: Yes, you can see this by setting the phase equal to
      a constant and differentiating the phase implicitly with respect to time to
      find that $v = v_{x} = \frac{dx}{dt}$ is negative.
---
# {{ params_vars_title }}
$D(x,t) = {{ params_A }}\cos({{ params_k }}x+ {{ params_omega }}t)$ describes the displacement $D$ in $\rm{cm}$ of a travelling sinusoidal wave as a function of displacement $x$ in $\rm{cm}$ and time $t$ in $\rm{s}$.

## Part 1

What is the amplitude $A$ of the travelling wave?

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

### pl-submission-panel

{{ feedback.part1_ans }}

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