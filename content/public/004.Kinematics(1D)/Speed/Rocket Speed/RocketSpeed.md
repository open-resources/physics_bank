---
title: Rocket Speed
topic: Kinematics(1D)
author: Patrick Jilek-Rodriguez
source: WebWork
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.6.2.0
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
- PJ
assets:
- RocketSpeed.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Rocket Speed
      d: 3.1
      theta1: 44
      theta2: 47.0
      dt: 0.46
---
# {{ params.vars.title }}
A rocket is fired vertically from a launch pad $d={{params.d}} \ \rm{km}$ away from a tracking radar.
At some time, the angle of elevation is $\theta={{params.theta1}}^\circ$.
After ${{params.dt}} \ \rm{s}$, the angle becomes $\theta={{params.theta2}}^\circ$.

<img src="RocketSpeed.png" width=700 alt="A rocket moving upwards at a distance d from a radar." >

## Part 1

What is the approximate speed of the rocket?

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)