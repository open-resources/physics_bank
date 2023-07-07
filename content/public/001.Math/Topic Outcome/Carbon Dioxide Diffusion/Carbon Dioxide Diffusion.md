---
title: Carbon Dioxide Diffusion
topic: Math
author: Reza Khanbabaie
source: PHYS 112 Proportional Reasoning Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.1.1.0
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
- sample.html
part1:
  type: symbolic-input
  pl-customizations:
    label: $t =$
    variables: d1, D
    weight: 1
    allow-blank: true
part2:
  type: symbolic-input
  pl-customizations:
    label: $\frac{t_{water}}{t_{air}} =$
    variables: D_w, D_a
    weight: 1
    allow-blank: true
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{water} = $
    suffix: $s$
part5:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
myst:
  substitutions:
    params_vars_title: Carbon Dioxide Diffusion
    params_vars_unit1: $m^2/s$
    params_vars_unit2: $s$
    params_water: 2.1
    params_air: 1.9
    params_time: 6
    params_const: 5
    params_part3_ans1_value: directly
    params_part3_ans2_value: inversely
---
# {{ params_vars_title }}
According to our textbook, at 25$^\circ$ $C$, the diffusion constant of $CO_2$ in water is $D\_{water} = {{ params_water }} \times 10^{-9}$ $m^2/s$ and the diffusion constant of $CO_2$ in air at one atmosphere is $D\_{air} = {{ params_air }} \times 10^{-5}$ $m^2/s$. If it takes $t\_{air} = $ {{ params_time }} $s$ for $CO_2$ to diffuse a distance $r\_{rms}=d_1$ through the air, how long does it take for $CO_2$ to diffuse $r\_{rms}=d_1$ through the water?

## Part 1

Prepare: Write a formula for the diffusion time $t$ in terms of the distance $d_1$ and diffusion constant $D$ given that $r\_{rms}=\sqrt{ {{ params_const }} Dt}$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| For  | Use   |
|----------|-------|
| $d_1$  | d1  |
| $D$  | D  |

### Answer Section

## Part 2

Prepare: Use proportional reasoning to express $\frac{t\_{water}}{t\_{air}}$  in terms of $D\_{water}$ and $D\_{air}$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| For  | Use   |
|----------|-------|
| $D\_{water}$  | D_w  |
| $D\_{air}$  | D_a  |

### Answer Section

## Part 3

Prepare: In this problem, are $t$ and $D$ directly or inversely proportional?

### Answer Section

- {{ params_part3_ans1_value}}
- {{ params_part3_ans2_value}}

## Part 4

Solve for $t\_{water}$ numerically.

### Answer Section

Please enter in a numeric value in $ {{ params_vars_unit2 }} $.

## Part 5

Assess: Does your answer make sense in the context of carbonated water being something people drink? Explain your answer.

### Answer Section

Answer in 2-3 sentences, try and use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)