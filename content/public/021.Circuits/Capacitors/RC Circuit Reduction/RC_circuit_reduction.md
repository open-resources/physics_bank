---
title: RC Circuit Reduction
topic: Circuits
author: John Hopkinson
source: PHYS122 2018W2 Q10
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 21.7.3.0
difficulty:
- easy
randomization:
- 4
taxonomy:
- undefined
span:
- undefined
length:
- long
tags:
- JR
- AK
assets:
- rccircred.png
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $C_5 = $
    suffix: $\rm{\mu F}$
part3:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $C_6 = $
    suffix: $\rm{\mu F}$
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\tau = $
    suffix: $\rm{s}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $Q = $
    suffix: $\rm{C}$
myst:
  substitutions:
    params:
      vars:
        title: RC Circuit Reduction
      c1: 12.4
      c2: 15.8
      c3: 13.2
      c4: 18.8
      part1:
        ans1:
          value: $C_1$
        ans2:
          value: $C_2$
        ans3:
          value: $C_3$
        ans4:
          value: $C_4$
      part3:
        ans1:
          value: $C_1$
        ans2:
          value: $C_2$
          feedback: This capacitor should not be in your redrawn circuit.
        ans3:
          value: $C_3$
          feedback: This capacitor should not be in your redrawn circuit.
        ans4:
          value: $C_4$
          feedback: This capacitor should not be in your redrawn circuit.
        ans5:
          value: $C_5$
---
# {{ params.vars.title }}
Consider the RC circuit shown below. Here, $C_1 = {{ params.c1 }}$ $\rm{\mu F}$, $C_2 = {{ params.c2 }}$ $\rm{\mu F}$, $C_3 = {{ params.c3 }}$ $\rm{\mu F}$, and $C_4 = {{ params.c4 }}$ $\rm{\mu F}$.

In this problem we will find the equivalent capacitance of this capacitor system in two steps. We will then use this result to determine the carge stored in the capacitor system.

<img src="rccircred.png" width=400 alt="A circuit diagram showing a 20 volt battery with its long teminal connected to a 100 ohm resistor that is connected to a capacitor with capacitance C1. After the capacitor, the circuit splits into three paths. One is connected to a capacitor with capacitance C2, another is connected to a capacitor with capacitance C3, and another is connected to a capacitor with capacitance C4. The paths then come together and connect to a switch, which is connected back to the short terminal the battery.">

## Part 1

Select the capacitors that are in parallel with eachother.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Part 2

Redraw the circuit by replacing the capacitors that you identified in Part 1 by an equivalent capacitor with capacitance $C_5$. Determine value of $C_5$.

Round your answer to three significant figures.

### Answer Section

Please enter an answer in $\rm{\mu F}$.

## Part 3

For your redrawn circuit, select the capacitors that are in series with each other. Do not select any capacitors that you have replaced.

### Answer Section

- {{ params.part3.ans1.value }}
- {{ params.part3.ans2.value }}
- {{ params.part3.ans3.value }}
- {{ params.part3.ans4.value }}
- {{ params.part3.ans5.value }}

## Part 4

Redraw the circuit by replacing the capacitors that you identified in Part 3 by an equivalent capacitor with capacitance $C_6$. Determine the value of $C_6$.

Round your answer to three significant figures.

### Answer Section

Please enter an answer in $\rm{\mu F}$.

## Part 5

Find the time constant $\tau$ for this circuit.

Round your answer to three significant figures.

### Answer Section

Please enter an answer in $\rm{s}$.

## Part 6

Find the maximum charge $Q$ that can be stored in this capacitor system.

### Answer Section

Please enter an answer in $\rm{C}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)