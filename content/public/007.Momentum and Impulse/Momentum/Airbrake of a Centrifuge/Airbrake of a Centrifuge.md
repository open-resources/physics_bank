---
title: Airbrake of a Centrifuge
topic: Momentum and Impulse
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.3.0
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
- TA
- APSC181
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\lvert v \rvert= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Airbrake of a Centrifuge
    params_vars_units: "$\rm{m/s}$"
    params_v: 69
    params_N: 2
    params_M: 832
    params_C: 1.902
    params_r: 3.07
    params_t: 3.76
    params_mass: 316
---
# {{ params_vars_title }}
An important part of astronaut training is force resistance training. It is done in a large centrifuge, with radius $r = {{params_r}} \ \rm{m}$ and total mass $m = {{params_mass}} \ \rm{kg}$.
The centrifuge cabin is accelerated to a speed $\lvert v \rvert = {{params_v}} \ \rm{m/s}$.
When it is time to slow down the centrifuge, it is slowed down due to a constant resistive moment $M = {{params_M}} \ \rm{N.m}$ at the axle and the deployment of an airbrake that creates more air resistance such that the force is described by this equation $F = {{params_C}}t^{{{params_N}}} \ \rm{N}$.

What is the speed of the cabin ${{params_t}}$ seconds later?

## Part 1

What is $\lvert v \rvert$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)