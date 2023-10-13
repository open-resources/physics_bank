---
title: Pulley System
topic: Force
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.9.1.0
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
- APSC181
- JR
assets:
- Pulley.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T= $
    suffix: $\rm{lb}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_B= $
    suffix: $\rm{slug}$
myst:
  substitutions:
    params_vars_title: Distance travelled
    params_vars_units: m/s
    params_m: 344
---
# {{ params_vars_title }}
<img src="Pulley.png" width=60%>

Shown above is a system of pulleys in equilibrium. The container labeled A has a weight of $W = {{ params_m }} \ \rm{lb}$.

## Part 1

Find the tension in the cables.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Find the mass of the container labeled B.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)