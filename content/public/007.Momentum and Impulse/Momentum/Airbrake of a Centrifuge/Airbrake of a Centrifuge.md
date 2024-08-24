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
    params:
      vars:
        title: Airbrake of a Centrifuge
        units: "$\rm{m/s}$"
      v: 88
      N: 2
      M: 912
      C: 1.48
      r: 3.93
      t: 2.95
      mass: 355
---
# {{ params.vars.title }}
An important part of astronaut training is force resistance training. It is done in a large centrifuge, with radius $r = {{params.r}} \ \rm{m}$ and total mass $m = {{params.mass}} \ \rm{kg}$.
The centrifuge cabin is accelerated to a speed $\lvert v \rvert = {{params.v}} \ \rm{m/s}$.
When it is time to slow down the centrifuge, it is slowed down due to a constant resistive moment $M = {{params.M}} \ \rm{N.m}$ at the axle and the deployment of an airbrake that creates more air resistance such that the force is described by this equation $F = {{params.C}}t^{{{params.N}}} \ \rm{N}$.

What is the speed of the cabin ${{params.t}}$ seconds later?

## Part 1

What is $\lvert v \rvert$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)