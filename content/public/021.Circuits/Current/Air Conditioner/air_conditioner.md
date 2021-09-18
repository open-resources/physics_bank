---
title: Air Conditioner
topic: Circuits
author: Vanshika Sharma
source: 2.9.33
template_version: 1.1
attribution: standard
outcomes:
- 21.2.1.3
- 21.2.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $J=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ {A/m^2}$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $v_{d} =$
    allow-blank: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ {m/s}$
    weight: 1
substitutions:
  params:
    vars:
      title: Air Conditioner
    I: 48
    n: 6
---
# {{ params.vars.title }}
The current supplied to an air conditioner unit is {{params.I}} $\textrm{A}$. The air conditioner is wired using a 10-gauge (diameter 2.588 mm) wire. The charge density is $ {{{params.n}} \times 10^{28}} {electrons \over m^3} $.

## Part 1

What is the magnitude of the current density?

### Answer Section

Please enter a numeric value.

## Part 2

What is the magnitude of the drift velocity.

### Answer Section

Please enter a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)