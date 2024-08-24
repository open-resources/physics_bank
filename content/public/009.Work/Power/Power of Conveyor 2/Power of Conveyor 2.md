---
title: Power of Conveyor 2
topic: Work
author: James Ropotar
source: Original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- JR
- APSC181
assets:
- Power of Conveyer 2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $P = $
    suffix: $\rm{ft-lb/s}$
myst:
  substitutions:
    params:
      vars:
        title: Power of Conveyor 2
      theta: 28.0
      v: 4.3
      L: 13.0
      W: 0.3
      mu: 0.3
---
# {{ params.vars.title }}
<img src="Power of Conveyer 2.png" width=600>

The conveyor above contains a slide plate below the belt, which is used for structure.
This plate gives a coefficient of friction of $\mu = {{ params.mu }}$ between the plate and the belt.
The belt is then loaded with a load, with a weight density of $W = {{ params.W }} \ \rm{lb/ft}$.\
How much horsepower is required to run the belt at a velocity of $v = {{ params.v }} \ \rm{ft/s}$ ?
The belt is $L = {{ params.L }} \ \rm{ft}$ long and angled at $\theta = {{ params.theta }}^{\circ}$.
Assume the load is constantly fed onto the belt and transitions smoothly.
Assume the belt itself is massless.

## Part 1

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)