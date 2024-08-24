---
title: Combined Resistors
topic: Circuits
author: John Hopkinson
source: Physics 122 2019 W2 Final Q14
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 21.8.2.0
- 21.8.3.0
difficulty:
- medium
randomization:
- 0
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- L.K
assets:
- resistors.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.005
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: Ω
part2:
  type: number-input
  pl-customizations:
    rtol: 0.005
    weight: 1
    allow-blank: true
    label: $V_{diff}= $
    suffix: V
part3:
  type: number-input
  pl-customizations:
    rtol: 0.005
    weight: 1
    allow-blank: true
    label: $V_{diff}= $
    suffix: V
myst:
  substitutions:
    params:
      vars:
        title: Combined Resistors
---
# {{ params.vars.title }}
The figure below shows a resistor circuit.

<img src="resistors.png" width = 400>

## Part 1

Find the total resistance of this circuit (in the ideal wire approximation), identifying any resistors in parallel or in series by calculating the effective resistance, reducing the circuit by replacing these resistors with an equivalent resistor and redrawing the circuit until only one resistor remains in the final circuit.
What is the resistance in the final circuit?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Solve for the potential difference $V_B - V_C$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

Solve for the potential difference $V_A - V_B$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)