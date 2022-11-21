---
title: Conductor Surface Charge
topic: Electrostatics
author: Jake Bobowski
source: 2.6.19
template_version: 1.0
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 18.10.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 6
- problem 19
- electric field
- conductor
- surface charge
- cavity
- numeric
- JB
assets:
- OSUPv2p6_19.png
part1:
  type: number-input
  pl-customizations:
    label: $Q_\mathrm{cavity}=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \mu C$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $Q_\mathrm{outer}=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \mu C$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Conductor Surface Charge
    Q: '7.8'
    q: '7.2'
---
# {{ params.vars.title }}
The conductor in the figure has an excess charge of ${{params.Q}}\rm\ \mu C$.
A point charge $q = {{params.q}}\rm\ \mu C$ is placed in the cavity.

<img src="OSUPv2p6_19.png" width=300 alt="Conductor with a cavity enclosing a point charge.">

## Part 1

What is the net charge on the surface of the cavity?
Give your answer in units of micro-Coulombs.

### Answer Section

## Part 2

What is the net charge on the outer surface of the conductor?
Give your answer in units of micro-Coulombs.

### Answer Section

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}

### pl-answer-panel

$Q\_\mathrm{cavity}=$ {{ correct_answers.part1_ans_str }} $\rm\ \mu C$<br>
$Q\_\mathrm{outer}=$ {{ correct_answers.part2_ans_str }} $\rm\ \mu C$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)