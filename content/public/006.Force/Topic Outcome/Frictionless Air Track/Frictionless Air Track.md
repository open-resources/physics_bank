---
title: A Frictionless Air Track?
topic: Force
author: Jake Bobowski
source: 2012 Final Q14
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
substitutions:
  params:
    vars:
      title: A Frictionless Air Track?
      name: Abbas
      units: $m/s^2$
    m1: 484.2
    m2: 48.64
    d_a: 0.02
    mean: 1.61
    sd: 0.15
    a1: 1.33
    a2: 1.68
    a3: 1.8
    a4: 1.72
    a5: 1.74
    a6: 1.6
    a7: 1.71
    a8: 1.62
    a9: 1.36
    a10: 1.56
    part4:
      ans1:
        value: The track is frictionless because $a_{expected}$ does not agree with
          $a_{measured}$.
      ans2:
        value: The track is not frictionless because $a_{expected}$ agrees with $a_{measured}$.
      ans3:
        value: The track is not frictionless because $a_{expected}$ does not agree
          with $a_{measured}$.
      ans4:
        value: The track is frictionless because $a_{expected}$ agrees with $a_{measured}$.
---
# {{ params.vars.title }}
Because of {{ params.vars.name }}'s excellent work in lab, their professor asks them to test out a new "frictionless" air track, which can be used to measure the acceleration due to gravity.
In {{ params.vars.name }}'s setup, they place a cart with mass $m_1$ = {{ params.m1 }} $g$ on the track and suspend a second mass $m_2$ = {{ params.m2 }} $g$ over a (supposedly) massless, frictionless pulley.
Using a photogate that reads the acceleration of the system at the pulley, {{ params.vars.name }} measures the acceleration in 10 trials as given in the table below.
The uncertainty in each acceleration measurement is $\pm$ {{ params.d_a }} $m/s^2$; the uncertainties in $m_1$ and $m_2$ are negligible.
The mean and standard deviation (SD) of the acceleration data are also given in the table.
Given these data, would you conclude that the air track system is frictionless as claimed?
Justify your answer!

<img src="q14_2012Final.png" alt="Mass m one sits on a horizontal surface while mass m two is suspended over a pulley. The masses are connected by a string." width=300>

| Trial     | Accel. ($m/s^2$) |
| ----------- | ----------- |
| 1     |  {{ params.a1 }}     |
| 2   |   {{ params.a2 }}      |
| 3     |  {{ params.a3 }}     |
| 4   |   {{ params.a4 }}      |
| 5     |  {{ params.a5 }}     |
| 6   |   {{ params.a6 }}      |
| 7     |  {{ params.a7 }}     |
| 8   |   {{ params.a8 }}      |
| 9     |  {{ params.a9 }}     |
| 10   |   {{ params.a10 }}      |
| **Mean** | {{ params.mean }}      |
| **SD** | {{ params.sd }}      |

## Part 1

Calculate $a\_{expected}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Calculate $a\_{measured}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

Calculate the standard error of $a\_{measured}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

Would you conclude that the air track system is frictionless as claimed? Justify your answer!

### Answer Section

- {{ params.part4.ans1.value}}
- {{ params.part4.ans2.value}}
- {{ params.part4.ans3.value}}
- {{ params.part4.ans4.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)