---
title: Cut The Rope
topic: Energy
author: Jake Bobowski
source: 2012 Final Q11
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.5.1.1
- 8.5.1.3
- 5.1.1.0
- 5.5.1.0
- 5.5.1.1
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
- q11_2012Final.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{cut}= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t$
    suffix: $s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Cut The Rope
      units: m
    l: 0.9
    theta_0: 36
    theta_c: 27
---
# {{ params.vars.title }}
In the mobile app "Cut the Rope", a mass (of candy) swings on a rope and the game player selects a point to cut the rope so it lands in a cute little monster's mouth.
Imagine that the mass is suspended from a fixed pivot point by a massless string of length $L = $  {{ params.l }} m.
It is released from an angle $\theta_0 = $ {{ params.theta_0 }} $^{\circ}$, swings through its lowest point, and is then cut on the other side at $\theta\_{cut} = $ {{ params.theta_c }} $^{\circ}$.
Once cut, the mass flies free (no drag) and lands on a surface a distance $d$ away from the point where it was when the rope was cut.
The surface is at the same height as the mass when the rope is cut.

The figure below shows the situation described above.

<img src="q11_2012Final.png" alt="A mass is suspended from a fixed pivot point by a massless string of length L. It is displaced to the left at an angle theta naught from equilibrium.  After swinging through its lowest point, the rope is then cut on the right at an angle theta cut. The mass lands on a surface at the same height as the mass when the rope is cut at a distance d from where the mass was when rope was cut." width=400>

## Part 1

Calculate the speed of the candy right before the string is cut.

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 2

After the string is cut, how long does the candy travel for?

### Answer Section

Please enter in a numeric value in $s$.

## Part 3

After the string is cut, how far does the candy travel in the horizontal direction?

### Answer Section

Please enter in a numeric value in $m$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)