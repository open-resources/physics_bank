---
title: Electron Beam
topic: Circuits
author: Vanshika Sharma
source: 2.9.29
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.2.2.0
- 21.2.2.1
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
    label: $ \textrm {J=} $
    suffix: $ \rm {A/m^2} $
myst:
  substitutions:
    params_vars_title: 'Electron Beam '
    params_vars_units: ' $ A / m^2 $ '
    params_I: 56
    params_r: 0.61
---
# {{ params_vars_title }}

## Question Text

An electron beam with a radius of {{params_r}} $\textrm{mm}$ has a measured current of {{params_I}}$\rm\ \mu A$.
What is the magnitude of the current density in the beam?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

### pl-submission-panel

<p></p>
{{ submitted_answers.part1_ans_str }}
<p></p>
{{ feedback.part1_ans }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)