---
title: Algebra Test Q1
topic: Template
author: Firas Moosvi
source: 1.1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.5.1.5
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
- FM
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: number-input
  pl-customizations:
    weight: 2
substitutions:
  params:
    vars:
      title: Kinematics
      name: Aliyah
      vehicle: a skateboard
      units: m/s
    v: 5
    t: 9
    part1:
      ans1:
        value: 42
        feedback: This is a random number, you probably selected this choice by mistake!
          Try again please!
      ans2:
        value: 45
        feedback: Great! You got it.
      ans3:
        value: 14
        feedback: Hmm, does it make sense to add a velocity and a time? Check the
          units!
      ans4:
        value: 0.5555555555555556
        feedback: 'Hmm, check the units of the resulting answer: v/t.'
      ans5:
        value: -4
        feedback: Hmm, does it make sense to subtract a velocity and a time? Check
          the units!
      ans6:
        value: -5.2
        feedback: Hmm, does it make sense to subtract a velocity and a time? Check
          the units!
---
# {{ params.vars.title }}
{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.

## Part 1

How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

### pl-submission-panel

Everything here will get inserted directly into the pl-submission-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 2

What is the acceleration of {{ params.vars.name }} while they are stopping on the {{ params.vars.vehicle }} ?

### Answer Section

Please enter in a numeric value.

### pl-submission-panel

Everything here will get inserted directly into the pl-submission-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)