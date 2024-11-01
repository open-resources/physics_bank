---
title: Sniper Target Practice
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.0
- 5.5.1.2
- 5.5.1.3
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
- SniperQuestion.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.1
    weight: 1
    allow-blank: true
    label: $e= $
    suffix: $ \rm{m} $
myst:
  substitutions:
    params:
      vars:
        title: Sniper Target Practice
      v: 1137
      d: 1.78
      h: 42
---
# {{ params.vars.title }}
A sniper is practicing their shots on a target $h = {{ params.h }} \ \rm{m}$ high at $d = {{ params.d }} \ \rm{km}$ away.

<img src="SniperQuestion.png" height=300 alt="A gun points above a target at distance d and height h away. A straight dotted line goes from the muzzle of the gun to directly above the target. The dotted line is elevated at height e from the target." >

## Question Text

If the bullet leaves the gun at $v = {{params.v}} \ \rm{m/s}$, at what elevation $e$ above the target should the sniper aim? <br>(Use the smaller angle)

### Answer Section

Please enter in a numeric value in $m$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)