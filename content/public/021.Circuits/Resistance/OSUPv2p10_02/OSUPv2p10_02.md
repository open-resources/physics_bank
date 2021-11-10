---
title: Battery Internal Resistance
topic: Circuits
author: Joseph Wandinger
source: 2.10.2
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.8.2.0
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
- JW
- OSUP
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I_\mathrm{f}/I_0= $
    show-placeholder: false
substitutions:
  params:
    vars:
      title: Battery Internal Resistance
    x: 3
    N: 4
    V_string: '6.50'
---
# {{ params.vars.title }}
A battery with an internal resistance of $r$ and an emf of {{ params.V_string }}$\textrm{ V}$ is connected to a load resistor $R =$ {{ params.N }}$r$ and current $I_0$ flows.
As the battery ages, the internal resistance increases by a factor of {{ params.x }}.

## Part 1

Find the ratio $I\_\mathrm{f}/I_0$, where $I\_\mathrm{f}$ is the final current after the battery has aged.

### Answer Section

Please enter a rational number.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)