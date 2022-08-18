---
title: Wheel of Fortune
topic: Rotational Motion
author: Jake Bobowski
source: 2016 Final Q2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.1.1.1
difficulty:
- medium
randomization:
- undefined
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- AK
assets:
- wheel_of_fortune.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\omega_i = $
    suffix: $rad/s$
substitutions:
  params:
    vars:
      units: rad/s
      name: Maya
      title: Wheel of Fortune
    t: 2.4
    w_i: ${\pi \over 2} {rad\over s}$
---
# {{ params.vars.title }}
{{ params.vars.name }} wants to win a game of Wheel-of-Fortune.
The grand prize is initially located at a position at the top of the wheel and contestants win the prize located at the position to the right when the wheel stops (shown below).
{{ params.vars.name }} notes that when another contestant set the wheel spinning at $\omega_i = $ {{ params.w_i }} in the counter-clockwise direction, it takes {{ params.t }} $s$ to stop.

## Part 1

With which initial velocity in the counter-clockwise direction should {{ params.vars.name }} spin the wheel to win the grand prize? Note that it is not possible to spin the wheel such that it undergoes more than 16 full rotations. Your answer should include at three significant figures.

<img src="wheel_of_fortune.png" alt="Image of a wheel showing the prize to be at the top (0 degrees) and the winning section to be on the right (90 degrees clockwise)." width=300>

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)