---
title: Kinetic Energy of a Simple Pendulum System
topic: Energy
author: Jake Bobowski
source: 2017 Midterm 2 Section 002 Q5
template_version: 1.2
attribution: standard
showCorrectAnswer: false
outcomes:
- 8.5.1.1
- 8.2.1.4
- 8.3.2.4
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets:
- 2017Mid2S002Q5.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = \pm $
    suffix: $^{\circ}$
substitutions:
  params:
    vars:
      title: Kinetic Energy of a Simple Pendulum System
      units: degrees
    theta: 18.0
---
# {{ params.vars.title }}
The figure below shows a simple pendulum. The length of the string is $l$ and the bob has mass $m_1$.

<img src="2017Mid2S002Q5.png" alt="Figure of a pendulum. The angle between the displaced string of the pendulum and the vertical axis is theta." >

## Question Text

If the mass is released from rest when $\theta = {{ params.theta }}^{\circ}$, at which values of $\theta$ does the mass have half of its maximum kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)