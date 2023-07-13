---
title: Charge Model
topic: Circuits
author: Vanshika Sharma
source: 2.9.25
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.2.1.0
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
- chapter 9
- problem 25
- derivative
- model
- charge
- current
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $I= $
    suffix: $\rm\ A$
myst:
  substitutions:
    params_vars_title: Charge Model
    params_vars_units: A
    params_c1: 22
    params_c2: 26
    params_c3: 1
    params_t: 10
---
# {{ params_vars_title }}
The quantity of charge through a conductor is modeled as $ \textrm{Q}=$ {{params_c1}}$\rm{t^4}$ $\rm{mC \over s^4}$ - {{params_c2}}$\rm{t}$ $\rm{mC \over s}$ + {{params_c1}} $\rm{mC}$.
What is the current at time $\textrm{t} =$ {{params_t}} $\textrm{s}$?

## Question Text

### Answer Section

### pl-submission-panel

<p></p>
{{ submitted_answers.part1_ans_str }}
<p></p>
{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)