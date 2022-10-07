---
title: Steel Ball Uncertainty
topic: Math
author: Jake Bobowski
source: 2013 Final Q13
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.3.1.2
- 1.3.1.3
- 2.1.1.2
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
- MP
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $mean= $
    suffix: s
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\sigma= $
    suffix: s
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Uncertainty
      units: s
    m: 26.12
    m_u: 0.04
    d: 0.1
    d_u: 0.002
    t1: 0.0506
    t2: 0.0502
    t3: 0.0508
    t4: 0.0508
    t5: 0.0503
    t6: 0.0506
    t7: 0.0505
---
# {{ params.vars.title }}
A steel ball (mball = ({{params.m}} $\pm$ {{ params.m_u }}) g) is shot from a mini-launcher on its medium setting, through horizontal photogates spaced ({{ params.d }} $\pm$ {{ params.d_u }}) m apart.
The time interval that the ball spends between these gates is measured in six independent trials to be:

| Trial Number | Time between gates (s) |
|--------------|------------------------|
| Trial 1      | {{params.t1}}          |
| Trial 2      | {{params.t2}}          |
| Trial 3      | {{params.t3}}          |
| Trial 4      | {{params.t4}}          |
| Trial 5      | {{params.t5}}          |
| Trial 6      | {{params.t6}}          |
| Trial 7      | {{params.t7}}          |

For this problem, keep one significant figure in the calculated uncertainty and the appropriate number of significant figures in the calculated average time interval.

## Part 1

Calculate the average time interval.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Calculate the uncertainty in the average time interval

### Answer Section

Please enter a numeric value in {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)