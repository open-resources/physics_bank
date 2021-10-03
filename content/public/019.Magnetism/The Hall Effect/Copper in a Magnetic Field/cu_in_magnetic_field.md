---
title: Copper in a Magnetic Field
topic: Magnetism
author: Vanshika Sharma
source: 2.11.48
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 19.5.1.0
- 19.5.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- VS
- chapter 11
- problem 48
- drift velocity
- current
- hall effect
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $v_d =$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ m/s$
    weight: 1
    custom-format: .2e
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $I=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .2g
substitutions:
  params:
    vars:
      title: Copper in a Magnetic Field
    B: 8.6
    E: 5.8
    n: 5
    A: 7.2
---
# {{ params.vars.title }}
A strip of copper is placed in a uniform magnetic field of magnitude ${{params.B}}\textrm{ T}$.
The Hall electric field is measured to be ${{params.E}} \times 10^{-3}\textrm{ V/m}$.

## Part 1

What is the drift speed of the conduction electrons?

### Answer Section

Please enter a numeric value.

## Part 2

Assuming that $n = {{params.n}} \times 10^{28}$ electrons per cubic meter and that the cross-sectional area of the strip is ${{params.A}} \times 10^{-6} \rm\ { m^{2}}$, calculate the current in the strip.

### Answer Section

Please enter a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)