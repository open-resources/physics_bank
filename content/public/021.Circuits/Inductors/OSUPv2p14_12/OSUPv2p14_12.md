---
title: RL Series Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.12
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.3.0
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
- OSUP
- volume 2
- chapter 14
- problem 12
- circuits
- RL circuits
- multi-part
- JW
assets:
- fig_OSUPv2p14_12.png
part1:
  type: number-input
  pl-customizations:
    label: $V_L = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    weight: 1
    custom-format: .3g
part2:
  type: symbolic-input
  pl-customizations:
    label: $V_R = $
    variables: I, L, E
    allow-blank: false
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: RL Series Circuit
---
# {{ params.vars.title }}
Consider the $RL$ circuit shown below.

<img src="fig_OSUPv2p14_12.png" width=250>

For this question, consider the case that the current has reached its final value of ${\boldsymbol \varepsilon}/R$.

## Part 1

What is the voltage across the inductor?

### Answer Section

Please enter in a numeric value in $\rm\ V$.

## Part 2

Write the voltage across the resistor in terms of the current $I$, inductance $L$, and voltage $\boldsymbol \varepsilon$.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For                       | Use |
|---------------------------|-----|
| $I$                       | I   |
| $L$                       | L   |
| $\boldsymbol \varepsilon$ | E   |

### Answer Section

### pl-answer-panel

$V_L = 0 \rm\ V$<br>
$V_R = {\boldsymbol \varepsilon} \rm\ V$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)