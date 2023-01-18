---
title: Three Blocks
topic: Force
author: Reza Khanbabaie
source: PHYS 112 Newton's Third Law - Torque Q1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 6.2.1.1
- 6.2.1.2
- 6.3.1.2
- 6.5.1.1
- 6.6.1.0
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
assets:
- threeblocks.png
- systems.png
- fbd.png
part1:
  type: file-upload
  pl-customizations:
    file-names: systems.pdf
part2:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part3:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part4:
  type: file-upload
  pl-customizations:
    file-names: fbd.pdf
part5:
  type: symbolic-input
  pl-customizations:
    label: $m_A \times a = $
    variables: F_a, F_ba, F_ab, F_cb, F_bc
    weight: 1
    allow-blank: false
part6:
  type: symbolic-input
  pl-customizations:
    label: $m_B \times a = $
    variables: F_a, F_ba, F_ab, F_cb, F_bc
    weight: 1
    allow-blank: false
part7:
  type: symbolic-input
  pl-customizations:
    label: $m_C \times a = $
    variables: F_a, F_ba, F_ab, F_cb, F_bc
    weight: 1
    allow-blank: false
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\rm{a} = $
    suffix: $\rm{m/s^2}$
part9:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{\text{B on A}} = $
    suffix: $\rm{N}$
part10:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{\text{B on C}} = $
    suffix: $\rm{N}$
substitutions:
  params:
    vars:
      title: Three Blocks
      unit1: $\rm{m/s^2}$
      unit2: $\rm{N}$
    m_A: 1.3
    m_B: 2.6
    m_C: 5.2
    F: 30
    part2:
      ans1:
        value: $m_B$
        feedback: Correct! Nice work
      ans2:
        value: $m_C$
        feedback: Correct! Nice work
      ans3:
        value: $m_A$
        feedback: Correct! Nice work
      ans4:
        value: $F_{\text{on A}}$
        feedback: Correct! Nice work
      ans5:
        value: $F_{\text{B on A}}$
        feedback: Not quite - Try again!
      ans6:
        value: $F_{\text{B on C}}$
        feedback: Not quite - Try again!
    part3:
      ans1:
        value: $F_{\text{B on A}}$
        feedback: Correct! Nice work
      ans2:
        value: $F_{\text{B on C}}$
        feedback: Correct! Nice work
      ans3:
        value: $m_B$
        feedback: Not quite - Try again!
      ans4:
        value: $m_C$
        feedback: Not quite - Try again!
      ans5:
        value: $m_A$
        feedback: Not quite - Try again!
      ans6:
        value: $F_{\text{on A}}$
        feedback: Not quite - Try again!
---
# {{ params.vars.title }}
Three blocks with masses $m_A = $ {{ params.m_A }} $\rm{kg}$, $m_B = $ {{ params.m_B }} $\rm{kg}$, and $m_C = $ {{ params.m_C }} $\rm{kg}$ are lined up in a row on a frictionless table. All three blocks are pushed forward by a force applied to block $A$ as shown in the figure ($F\_\text{on A} = F =$ {{ params.F }} $\rm{N}$). We would like to determine the force block $B$ exerts on blocks $A$ and $C$.

<img src="threeblocks.png" width=400 alt="Three blocks of increasing height labelled A, B, and C are lined up in a row. A force F is applied to block A, the smallest block. The blocks are placed in the first quadrant of a cartesian plane.">

## Part 1

Draw a closed line around each of the three systems of interest (on the following figure) and show the environment, i.e., objects outside of the system that affect or exert forces on the system. Upload your file as a PDF named "systems.pdf".

<img src="systems.png" width=600 alt="Figure showing three identical copies of the image shown in the main question text.">

### Answer Section

File upload box will be shown here.

## Part 2

What information is known?

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}
- {{ params.part2.ans4.value}}
- {{ params.part2.ans5.value}}
- {{ params.part2.ans6.value}}

## Part 3

What are the unknowns?

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}
- {{ params.part3.ans3.value}}
- {{ params.part3.ans4.value}}
- {{ params.part3.ans5.value}}
- {{ params.part3.ans6.value}}

## Part 4

Draw a free body diagram for each individual masse and connect the action/reaction force pairs with dashed lines. Also remember to show the net forces. Upload your file as a PDF named "fbd.pdf".

<img src="fbd.png" width=600 alt="Figure showing three cartesian planes - one for each mass.">

### Answer Section

File upload box will be shown here.

## Part 5

Apply Newton's 2nd law to block $A$ along the x-axis.

Let $a$ be the acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For $\quad \quad$       | Use   |
|-------------------------|-------|
| $F\_{\text{on A}}$       | F_a     |
| $F\_{\text{B on A}}$     | F_ba    |
| $F\_{\text{A on B}}$     | F_ab    |
| $F\_{\text{C on B}}$     | F_cb    |
| $F\_{\text{B on C}}$     | F_bc    |

### Answer Section

## Part 6

Apply Newton's 2nd law to block $B$ along the x-axis.

Let $a$ be the acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For $\quad \quad$       | Use   |
|-------------------------|-------|
| $F\_{\text{on A}}$       | F_a     |
| $F\_{\text{B on A}}$     | F_ba    |
| $F\_{\text{A on B}}$     | F_ab    |
| $F\_{\text{C on B}}$     | F_cb    |
| $F\_{\text{B on C}}$     | F_bc    |

### Answer Section

## Part 7

Apply Newton's 2nd law to block $C$ along the x-axis.

Let $a$ be the acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For $\quad \quad$       | Use   |
|-------------------------|-------|
| $F\_{\text{on A}}$       | F_a     |
| $F\_{\text{B on A}}$     | F_ba    |
| $F\_{\text{A on B}}$     | F_ab    |
| $F\_{\text{C on B}}$     | F_cb    |
| $F\_{\text{B on C}}$     | F_bc    |

### Answer Section

## Part 8

Apply Newton's 2nd law and calculate the acceleration.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 9

Using the acceleration obtained in Part 8, determine the force exerted by block $B$ on block $A$, $F\_{\text{B on A}}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 10

Using the acceleration obtained in Part 8, determine the force exerted by block $B$ on block $C$, $F\_{\text{B on C}}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)