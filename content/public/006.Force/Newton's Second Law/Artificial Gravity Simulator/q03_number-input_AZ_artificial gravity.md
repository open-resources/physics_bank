---
title: Artificial Gravity Simulator
topic: Force
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.12.1.1
- 6.12.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- spacecraft.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{ms^{-1}}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_vars_title: Artificial Gravity Simulator
    params_m: 86
    params_r: 285
---
# {{ params_vars_title }}
To simulate the effects of "weight" in deep space, the spacecraft is made to rotate with the astronaut "standing" on the outer hull of a circular chamber. The artificial gravity experienced by the astronaut is the inertial reaction to the normal force pulling them to the center of rotation.

<img src="spacecraft.png" width=600>

## Question Text

What is the rotational speed($v$) with which the rocket has to rotate to mimic earth's gravity($g$).<br>
$m = {{ params_m }}\ \rm{kg}$, $R = {{ params_r }}\ \rm{m}$

### Answer Section

Please enter in a numeric value in m/s.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)