---
title: Equilibrium Length of a Spring
topic: Energy
author: Jake Bobowski
source: 2012 Final Q9
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.3.3.0
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
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Equilibrium Length of a Spring
      units: J
    Ux: 10x^2 - 3x - 88
---
# {{ params.vars.title }}
The potential energy of a spring is given by $U(x) = (${{ params.Ux }}$) J$ if $x$ is given in metres.

## Question Text

What is the equilibrium length of the spring?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)