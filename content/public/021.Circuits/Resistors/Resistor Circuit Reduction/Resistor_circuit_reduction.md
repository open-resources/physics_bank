---
title: Resistor Circuit Reduction
topic: Circuits
author: John Hopkinson
source: PHYS122 2017W2 Final Exam Q11
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
outcomes:
- 21.8.2.0
- 21.8.3.0
- 21.12.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- JR
- AK
assets:
- rcircred.png
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: PC
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R_6 = $
    suffix: $\rm{\Omega}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R_7 = $
    suffix: $\rm{\Omega}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R_8 = $
    suffix: $\rm{\Omega}$
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Resistor Circuit Reduction
      r1: 13
      r2: 6
      r3: 15
      r4: 15
      r5: 8
      part1:
        ans1:
          value: $(a)$ to $(b)$
          feedback: ''
        ans2:
          value: $(b)$ to $(c)$
          feedback: ''
        ans3:
          value: $(c)$ to $(d)$
          feedback: ''
      part5:
        ans1:
          value: Subtract the two electromotive forces and divide by the sum of the
            resistors.
          feedback: ''
        ans2:
          value: Use Kirchhoff's laws (junction and loop rules) to write three equations
            in three unknown currents, and solve them by eliminating one variable
            at a time.
          feedback: ''
---
# {{ params.vars.title }}
A car battery charger circuit contains resistors with resistances $R_1 = {{ params.r1 }} \rm{\Omega}$, $R_2 = {{ params.r2 }} \rm{\Omega}$, $R_3 = {{ params.r3 }} \rm{\Omega}$, $R_4 = {{ params.r4 }} \rm{\Omega}$, $R_5 = {{ params.r5 }} \rm{\Omega}$. The circuit is reduced in the steps shown in the figure below.

<img src="rcircred.png" width=400 alt="Circuit diagrams showing the car battery circuit in a and the steps taken to reduce the circuit from a to b , b to c, and c to d (if that step is allowed).">

## Part 1

Select the steps in reducing the circuit that are allowed.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Part 2

If step **(a)** to **(b)** is allowed, calculate the value of $R_6$. Otherwise enter "-1".

### Answer Section

Please enter an answer in $\rm{\Omega}$.

## Part 3

If step **(b)** to **(c)** is allowed, calculate the value of $R_7$. Otherwise enter "-1".

### Answer Section

Please enter an answer in $\rm{\Omega}$.

## Part 4

If step **(c)** to **(d)** is allowed, calculate the value of $R_8$. Otherwise enter "-1".

### Answer Section

Please enter an answer in $\rm{\Omega}$.

## Part 5

Once the circuit is as simplified as possible, what would you do to find the current through $R_5$?

### Answer Section

- {{ params.part3.ans1.value }}
- {{ params.part3.ans2.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)