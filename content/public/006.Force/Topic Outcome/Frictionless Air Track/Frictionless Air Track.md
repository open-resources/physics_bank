---
title: A Frictionless Air Track?
topic: Force
author: Jake Bobowski
source: 2012 Final Q14
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 2.4.1.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- PW
- final_exqm
assets:
- q14_2012Final.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{expected}= $
    suffix: $m/s^2$
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{measured}= $
    suffix: $m/s^2$
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\sigma_{\bar{x}} = $
    suffix: $m/s^2$
    digits: 3
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: A Frictionless Air Track?
    params_vars_name: Ahmed
    params_vars_units: $m/s^2$
    params_m1: 337.9
    params_m2: 27.79
    params_d_a: 0.02
    params_mean: 1.48
    params_sd: 0.0916
    params_a1: 1.35
    params_a2: 1.46
    params_a3: 1.46
    params_a4: 1.63
    params_a5: 1.49
    params_a6: 1.38
    params_a7: 1.61
    params_a8: 1.46
    params_a9: 1.38
    params_a10: 1.56
    params_part4_ans1_value: The track is frictionless because $a_{expected}$ does
      not agree with $a_{measured}$.
    params_part4_ans2_value: The track is not frictionless because $a_{expected}$
      agrees with $a_{measured}$.
    params_part4_ans3_value: The track is not frictionless because $a_{expected}$
      does not agree with $a_{measured}$.
    params_part4_ans4_value: The track is frictionless because $a_{expected}$ agrees
      with $a_{measured}$.
---
# {{ params_vars_title }}
Because of {{ params_vars_name }}'s excellent work in lab, their professor asks them to test out a new "frictionless" air track, which can be used to measure the acceleration due to gravity.
In {{ params_vars_name }}'s setup, they place a cart with mass $m_1$ = {{ params_m1 }} $g$ on the track and suspend a second mass $m_2$ = {{ params_m2 }} $g$ over a (supposedly) massless, frictionless pulley.
Using a photogate that reads the acceleration of the system at the pulley, {{ params_vars_name }} measures the acceleration in 10 trials as given in the table below.
The uncertainty in each acceleration measurement is $\pm$ {{ params.d_a }} $m/s^2$; the uncertainties in $m_1$ and $m_2$ are negligible.
The mean and standard deviation (SD) of the acceleration data are also given in the table.
Given these data, would you conclude that the air track system is frictionless as claimed?
Justify your answer!

<img src="q14_2012Final.png" alt="Mass m one sits on a horizontal surface while mass m two is suspended over a pulley. The masses are connected by a string." width=300>

| Trial     | Accel. ($m/s^2$) |
| ----------- | ----------- |
| 1     |  {{ params_a1 }}     |
| 2   |   {{ params_a2 }}      |
| 3     |  {{ params_a3 }}     |
| 4   |   {{ params_a4 }}      |
| 5     |  {{ params_a5 }}     |
| 6   |   {{ params_a6 }}      |
| 7     |  {{ params_a7 }}     |
| 8   |   {{ params_a8 }}      |
| 9     |  {{ params_a9 }}     |
| 10   |   {{ params_a10 }}      |
| **Mean** | {{ params_mean }}      |
| **SD** | {{ params_sd }}      |

## Part 1

Calculate $a\_{expected}$.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Calculate $a\_{measured}$.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

Calculate the standard error of $a\_{measured}$.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 4

Would you conclude that the air track system is frictionless as claimed? Justify your answer!

### Answer Section

- {{ params_part4_ans1_value}}
- {{ params_part4_ans2_value}}
- {{ params_part4_ans3_value}}
- {{ params_part4_ans4_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)