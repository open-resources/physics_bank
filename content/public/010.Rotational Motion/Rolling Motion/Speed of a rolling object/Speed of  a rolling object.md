---
title: Speed of a Rolling Object
topic: Rotational Motion
author: Jake Bobowski
source: 2013 Practice Final Q9
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
    label: $v= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Speed of a Rolling Object
      units: $m/s$
    h: 17.2
---
# {{ params.vars.title }}
One end of a massless string is attached to a massless axle that passes through the centre of mass of an object (mass $m$) that has a circular cross-section (radius $R$)  and  rolls  without  slipping  up  the  incline.
The  string  passes  over a massless, frictionless pulley and a block (also of mass $m$) is suspended from the opposite end of the string as shown in the figure.

In this problem you are to find the speed of the rolling object after the hanging mass has fallen by {{ params.h }} $m$ (the system is released from rest).

<img longdesc="Speed of a rolling object.md#desc" alt="Figure of the system described in the question text." src="q9_2013practiceFinal.png">

<div id="desc">
<h5>Long Description of image: Figure of the system described in the question text.</h5>
An object with a circular cross-section rolls up a thirty-degree incline (to the horizontal).  This object is attached to a string which passes  over a massless, frictionless pulley and a block of mass m is suspended from the opposite end of the string. The whole setup forms a right-angle triangle with the opposite side on the right.
<p>Long description ends.</p>
<div>

## Part 1

Find the rolling object's speed assuming that it is a solid sphere.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Find the rolling object's speed assuming that it is a hollow sphere.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

Find the rolling object's speed assuming that it is a solid cylinder.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)