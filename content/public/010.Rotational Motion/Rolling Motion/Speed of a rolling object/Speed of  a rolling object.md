---
title: Speed of a Rolling Object
topic: Rotational Motion
author: Jake Bobowski
source: 2013 Practice Final Q9
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 10.3.1.0
- 8.5.1.2
- 10.5.2.2
- 10.5.2.1
- 8.2.1.3
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- PW
- final_exam
assets:
- q9_2013practiceFinal.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Speed of a Rolling Object
    params_vars_units: "$\rm{m/s}$"
    params_h: 23.6
---
# {{ params_vars_title }}
Consider the setup shown in the figure below.
One end of a string of negligible mass is connected to a round object of mass $m$ and circular cross-section of radius $r$.
The string is connected to the round object via a frictionless axel of negligible mass that passes through the centre of mass of the round object.
The round object is on an incline that makes an angle $\theta = 30^{\circ}$ with the horizontal.
The string runs over a frictionless pulley of negligible mass and the other end of the string is connected to a rectangular object of mass $m$.
The pulley is positioned at the end of the incline such that the rectangular object is suspended in the air.

The system is initally at rest, but once the rectangular object is released, it accelerates downward, causing the round object to roll up the incline without slipping. Find the speed of the round object when the rectangular object has fallen $h =$ {{ params_h }} $\rm{m}$ for the case where the round object is a solid sphere, hollow sphere, or a solid cylinder.

<img longdesc="Speed of a rolling object.md#desc" alt="Figure of the system described in the question text." src="q9_2013practiceFinal.png">

<div id="desc">
<h5>Long Description of Image: Figure of the system described in the question text.</h5>
A round object rolls up an incline.  The round object is attached to a string which passes over a frictionless pulley of negligible mass positioned at the end of the incline. A rectangular object is suspended from the opposite end of the string.
<p>Long description ends.</p>
<div>

## Part 1

Find the speed of the round object assuming that it is a solid sphere.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Find the speed of the round object assuming that it is a hollow sphere.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

Find the speed of the round object assuming that it is a solid cylinder.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)