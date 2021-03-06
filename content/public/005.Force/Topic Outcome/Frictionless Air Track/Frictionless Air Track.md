---
title: A Frictionless Air Track?
topic: Force
author: Jake Bobowski
source: 2012 Final Q14
template_version: 1.0
attribution: standard
outcomes:
- 6.1.1.4
- 2.4.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q14_2012Final.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{expected}= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{measured}= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $ \delta a_{measured}= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 3
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: A Frictionless Air Track?
      units: $m/s^2$
    m1: 125.9
    m2: 41.57
    d_a: 0.01
    mean: 1.48
    sd: 0.137
    a1: 1.46
    a2: 1.34
    a3: 1.37
    a4: 1.64
    a5: 1.35
    a6: 1.3
    a7: 1.44
    a8: 1.58
    a9: 1.64
    a10: 1.69
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
Because of your excellent work in lab, your professor asks you to test out a new "frictionless" air track, which can be used to measure the acceleration due to gravity. In your setup, you place a cart with mass $m_1$ = {{ params.m1 }} $g$ on the track and suspend a second mass $m_2$ = {{ params.m2 }} $g$ over a (supposedly) massless, frictionless pulley. Using a photogate that reads the acceleration of the system at the pulley, you measure the acceleration in 10 trials as given in the table below. The uncertainty in each acceleration measurement is $\pm$ {{ params.d_a }} $m/s^2$; the uncertainties in $m_1$ and $m_2$ are negligible. The mean and standard deviation (SD) of the acceleration data are also given in the table. Given these data, would you conclude that the air track system is frictionless as claimed? Justify your answer!

![Mass m one sits on a horizontal surface while mass m two is suspended over a pulley. The masses are connected by a string.](q14_2012Final.png)

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

Calculate the standard deviation error of $a\_{measured}$.

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