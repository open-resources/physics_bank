---
title: Projectile Motion on an Incline
topic: Projectile Motion Kinematics
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.1
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
- APSC181
- A.Z
assets:
- part1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: m
substitutions:
  params:
    a: 1
    theta: 22
    u: 45
---
# Projectile Motion on an Incline
A tennis ball is projected with a speed of u at angle of Î¸ measured counter-clockwise from the normal to the inclined plane.

<img src="part1.png" width=600>

## Part 1

Determine the range R of the tennis ball if it hits the incline at the end of its motion.<br>
Treat the ball as a particle and neglect any resistive forces.<br><br>
$u = {{ params.u }}ms^{-1}$, $\theta = {{ params.theta }}\circ$, $\alpha = {{ params.a }}\circ$

### Answer Section

Please enter the range in $m$.

### pl-submission-panel

{{ feedback.part1_ans }}

Everything here will get inserted directly into the pl-submission-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

### pl-submission-panel

{{ feedback.part1_ans }}

Everything here will get inserted directly into the pl-submission-panel element at the end of the `question.html`.

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)