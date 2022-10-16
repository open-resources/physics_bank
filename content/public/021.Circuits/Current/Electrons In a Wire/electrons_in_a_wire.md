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
substitutions:
  params:
    vars:
      title: Electrons In a Wire
      units: m/s
    I: 42
    t: 45
---
# {{ params.vars.title }}

## Question Text

How many electrons flow through a point in a wire in {{params.t}} s if there is a constant current of {{params.I}} $\textrm{A}$.

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