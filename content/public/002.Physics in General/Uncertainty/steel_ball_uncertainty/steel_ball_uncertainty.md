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
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
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
myst:
  substitutions:
    params_vars_title: Uncertainty
    params_vars_units: s
    params_m: 32.6
    params_m_u: 0.03
    params_d: 0.30000000000000004
    params_d_u: 0.001
    params_t1: 0.0758
    params_t2: 0.0758
    params_t3: 0.0758
    params_t4: 0.0752
    params_t5: 0.0752
    params_t6: 0.0753
    params_t7: 0.0758
---
# {{ params_vars_title }}
A steel ball (mball = ({{params_m}} $\pm$ {{ params_m_u }}) g) is shot from a mini-launcher on its medium setting, through horizontal photogates spaced ({{ params_d }} $\pm$ {{ params_d_u }}) m apart.
The time interval that the ball spends between these gates is measured in six independent trials to be:

| Trial Number | Time between gates (s) |
|--------------|------------------------|
| Trial 1      | {{params_t1}}          |
| Trial 2      | {{params_t2}}          |
| Trial 3      | {{params_t3}}          |
| Trial 4      | {{params_t4}}          |
| Trial 5      | {{params_t5}}          |
| Trial 6      | {{params_t6}}          |
| Trial 7      | {{params_t7}}          |

For this problem, keep one significant figure in the calculated uncertainty and the appropriate number of significant figures in the calculated average time interval.

## Part 1

Calculate the average time interval.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Calculate the uncertainty in the average time interval

### Answer Section

Please enter a numeric value in {{ params_vars_units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)