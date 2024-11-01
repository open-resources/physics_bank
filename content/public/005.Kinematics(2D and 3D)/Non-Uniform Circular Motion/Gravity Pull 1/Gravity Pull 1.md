---
title: Gravity Pull
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: Original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.2
- 12.2.1.0
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
- TA
assets:
- Gravity Pull.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $|v| = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Gravity Pull
      M: 8.708
      R: 6314.0
      d: 33.0
      d1: 29.0
      v0: 1600.0
---
# {{ params.vars.title }}
<img src="Gravity Pull.png" width = 800> 

There is an asteroid flying in space. At $t = 0 \ \rm{s}$ , it travels at a speed of $v_0 = {{ params.v0 }} \ \rm{m/s}$ and a distance $d = {{ params.d }} \ \rm{km}$ away from the planet's surface as shown. The planet has a radius of $R = {{ params.R }}\ \rm{km}$ and mass $M = {{ params.M }} \times 10^{25}\ \rm{kg}$. <br>
$G = 6.67 \times 10^{-11} \ \rm{m^3. kg^{-1}. s^{-2}}$

## Part 1

Find the asteroid's speed when it is ${{ params.d1 }}\ \rm{km}$  away from the surface.

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)