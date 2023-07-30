---
title: Mean resting respiratory rate
topic: Math
author: Reza Khanbabaie
source: PHYS 112 Proportional Reasoning Q2
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
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: symbolic-input
  pl-customizations:
    label: $\frac{M_{rhino}}{M_{Es}} = $
    variables: RR_r, RR_Es
    weight: 1
    allow-blank: true
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $M_{rhino}$
    suffix: $kg$
part4:
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
    params_vars_title: Mean resting respiratory rate
    params_Resp_Es: 660
    params_Resp_r: 16
    params_m_Es: 2.47
    params_power: 4
    params_part1_ans1_value: $RR \propto M$
    params_part1_ans1_feedback: Reread the question. What does $RR$ scale as?
    params_part1_ans2_value: $RR \propto M^{-1/4}$
    params_part1_ans2_feedback: Great! You got it.
    params_part1_ans3_value: $RR \propto \frac{1}{M^{-1/4}}$
    params_part1_ans3_feedback: Review the definitions of "proportional to" and "inversely
      proportional to".
    params_part1_ans4_value: $RR \propto \frac{1}{M}$
    params_part1_ans4_feedback: Hmm, try rereading the question.
---
# {{ params_vars_title }}
The mean resting respiratory rate of an Etruscan shrew is {{ params.Resp_Es }} breaths per minute, while the mean respiratory rate of healthy standing unrestrained white rhinoceroses is {{ params.Resp_r }} breaths per minute. If the mean mass of an Etruscan shrew is {{ params.m_Es }} $g$, what would one expect the mass of the white rhinoceroses to be assuming respiratory rates ($RR$) scale as $M^{-1/ {{ params_power }} }$?

## Part 1

Prepare: Write a mathematical statement (e.g. $A \propto BB$) showing the proportionality relationship between *RR* and *M*.

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}

## Part 2

Prepare: Use proportional reasoning to express $\frac{M\_{rhino}}{M\_{Es}}$ in terms of $RR\_{rhino}$ and $RR\_{Es}$.

Use the following table as a reference for using each variable:

| For  | Use   |
|----------|-------|
| $RR\_{rhino}$  | RR_r  |
| $RR\_{Es}$  |RR_Es  |

### Answer Section

## Part 3

Solve for $M\_{rhino}$.

### Answer Section

Please enter in a numeric value in $kg$.

## Part 4

Does your answer have the correct units and seem reasonable?

### Answer Section

Answer in 1-2 sentences, try to use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)