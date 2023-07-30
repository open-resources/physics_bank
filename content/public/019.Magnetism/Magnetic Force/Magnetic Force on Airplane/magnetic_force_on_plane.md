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
myst:
  substitutions:
    params_vars_title: Magnetic Force on Airplane
    params_q: 0.045
    params_v: 520
    params_part2_ans1_value: North
    params_part2_ans2_value: South
    params_part2_ans3_value: East
    params_part2_ans4_value: West
---
# {{ params_vars_title }}
Aircrafts sometimes acquire small static charges. Suppose a supersonic jet has a {{params_q}} $\rm\ {\mu C}$ charge and flies due west at a speed of {{params_v}} $\textrm{ m/s}$ over Earths south magnetic pole, where the $\mathrm{8 \times 10^{-5}} \textrm{ T}$ magnetic field points straight down into the ground.

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

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params_part2_ans4_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)