---
title: Electrons In a Wire
topic: Circuits
author: Vanshika Sharma
source: 2.9.23
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.2.1.0
- 21.2.1.1
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
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: 'Number of electrons = '
myst:
  substitutions:
    params_vars_title: Electrons In a Wire
    params_vars_units: m/s
    params_I: 160
    params_t: 25
---
# {{ params_vars_title }}

## Question Text

How many electrons flow through a point in a wire in {{params_t}} s if there is a constant current of {{params_I}} $\textrm{A}$.

### Answer Section

Please enter a numeric value.

### pl-submission-panel

<p></p>
{{ submitted_answers.part1_ans_str }}
<p></p>
{{ feedback.part1_ans }}

### pl-answer-panel

Number of electrons =  {{correct_answers.part1_ans_str}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)