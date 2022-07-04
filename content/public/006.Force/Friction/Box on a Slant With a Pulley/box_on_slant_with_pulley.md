---
title: Box on a Slant with a Pulley
topic: Force
author: Jake Bobowski
source: 2013 Midterm 2 002 Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.4
- 6.3.1.2
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
assets:
- Q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $kg$
substitutions:
  params:
    vars:
      title: Box on a Slant with a Pulley
      units: $kg$
    theta: 25
    mu: 0.6
    m: 10
---
# {{ params.vars.title }}
The figure shows a block of mass $m$ resting on a {{params.theta}}$^\circ$ slope.
The coefficient of static friction between the block and the sloped surface is {{params.mu}}.
It is connected via a massless string over a massless, frictionless pulley to a hanging block of mass {{params.m}} $kg$.

<img src="Q4.png" width=300 alt = "A box sits on a ramp that is at an angle theta from the horizontal. The box is connected by a rope to another mass that hangs freely from a pulley.">

## Question Text

What is the _minimum_ value of $m$ such that the system remains at rest?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)