---
title: Clutch Plate Dampening System
topic: Rotational Motion
author: Peyman Yousefi
source: APSC 181, Lecture 16, Q1
template_version: 1.2
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.8
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC 181 - LA
- JR
assets:
- Springs On a Disk.gif
- simplified clutch plate top view .jpg
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $N= $
    suffix: $N$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $N= $
    suffix: $N$
substitutions:
  params:
    vars:
      title: Clutch Plate Dampening System
    w: 167
    d: 76
    k: 321
    m: 0.2
    x: 28
    d2: 1.05
---
# {{ params.vars.title }}
<img src="Springs On a Disk.gif" width=800>

In order to reduce the damaging effects of rapid speed changes, a manual transmission contains a set of coiled springs on the outer edge of the plate.
A simplistic version of a clutch plate is shown in the diagram above.
When shifting gears, the springs are compressed. This helps reduce vibrations and make shifting smooth.
At the end of each of these springs exists a block, $m = {{ params.m }}kg$ on which the force acts.

<img src="simplified clutch plate top view .jpg" width=600>

The springs are $d = {{ params.d }}mm$ from the centre, and have a stiffness of ${{ params.k }}N/m$.
The end of the spring starts with a distance of $x_0 = {{ params.x }}mm$ from the center, perpendicular to $d$.
Answer the following questions with the given information. Neglect friction and the mass of the springs.

## Part 1

If the clutch spins at $\omega= {{ params.w }}rev/min$, determine the value of $x$, the final distance of the blocks on the end of the spring.

### Answer Section

Please enter in a numeric value in metres.

## Part 2

Find the normal force $N$ exerted by the side of the slot on the block.

### Answer Section

Please enter in a numeric value in Newtons.

## Part 3

What force would be needed to compress the springs below the resting point by $\Delta x = {{ params.d2 }}$?

### Answer Section

Please enter in a numeric value in Newtons.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)