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
substitutions:
  params:
    vars:
      title: Mean resting respiratory rate
    Resp_Es: 668
    Resp_r: 22
    m_Es: 2.11
    power: 3
    part1:
      ans1:
        value: $RR \propto M$
        feedback: Reread the question. What does $RR$ scale as?
      ans2:
        value: $RR \propto M^{-1/3}$
        feedback: Great! You got it.
      ans3:
        value: $RR \propto \frac{1}{M^{-1/3}}$
        feedback: Review the definitions of "proportional to" and "inversely proportional
          to".
      ans4:
        value: $RR \propto \frac{1}{M}$
        feedback: Hmm, try rereading the question.
---
# {{ params.vars.title }}
The mean resting respiratory rate of an Etruscan shrew is {{ params.Resp_Es }} breaths per minute, while the mean respiratory rate of healthy standing unrestrained white rhinoceroses is {{ params.Resp_r }} breaths per minute. If the mean mass of an Etruscan shrew is {{ params.m_Es }} $g$, what would one expect the mass of the white rhinoceroses to be assuming respiratory rates ($RR$) scale as $M^{-1/ {{ params.power }} }$?

## Part 1

Prepare: Write a mathematical statement (e.g. $A \propto BB$) showing the proportionality relationship between *RR* and *M*.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

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