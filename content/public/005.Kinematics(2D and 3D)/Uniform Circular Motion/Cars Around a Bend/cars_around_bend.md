---
title: Cars around a bend
topic: Kinematics 2D and 3D
author: Peyman Yousefi
source: APSC 181, Lecture 8, Q1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- AP
- APSC181
- Lecture Activities
assets:
- L8Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $S = $
    suffix: $\rm{m}$
substitutions:
  params:
    vars:
      title: Cars around a bend
      units: "$\rm{m}$"
    max_acc_A: 0.5
    max_acc_B: 0.3
    ra: 304
    rb: 360
    angle: 34
---
# {{ params.vars.title }}
Two cars travel at constant speeds around a curve as shown below.
The front end of both cars crosses line $C$ at the same time and each driver minimizes their time in the curve.
The maximum centripetal acceleration for car A is ${{params.max_acc_A}}g$ with $R\_{A} = {{params.ra}}$ $\rm{m}$ and for car B is ${{params.max_acc_B}}g$ with $R\_{B} = {{params.rb}}$ $\rm{m}$, where $g$ is the gravitational constant.
The angle $\theta = {{params.angle}}^{\circ}$.

<img src="L8Q1.png" width=400 alt="Two cars are on a curved road. The radius or curvature of the road for car A (R_A) is less than that of car B (R_B). Both cars start at radial line C. Radial line D, which is some distance in front of the cars, makes an angle (theta) with radial line C.">

## Question Text

Determine the distance $S$ that the second car has yet to travel to reach line $D$ when the first car reaches line $D$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)