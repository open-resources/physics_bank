---
title: Magnetic Force on Airplane
topic: Magnetism
author: Vanshika Sharma
source: 2.11.21
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.3.2.0
- 19.3.1.1
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
- chapter 11
- problem 21
- VS
- magnetic force
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $F=$
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    suffix: $\rm\ N$
    weight: 1
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Magnetic Force on Airplane
    q: 0.828
    v: 514
    part2:
      ans1:
        value: North
      ans2:
        value: South
      ans3:
        value: East
      ans4:
        value: West
---
# {{ params.vars.title }}
Aircrafts sometimes acquire small static charges. Suppose a supersonic jet has a {{params.q}} $\rm\ {\mu C}$ charge and flies due west at a speed of {{params.v}} $\textrm{ m/s}$ over Earths south magnetic pole, where the $\mathrm{8 \times 10^{-5}} \textrm{ T}$ magnetic field points straight down into the ground.

## Part 1

What is the magnitude of the electric force on the plane?

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

$F=$ {{ correct_answers.part1_ans_str }} $\mathrm{N}$

## Part 2

What is the direction of the magnetic force on the plane?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)