---
title: Moving Creature
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2018W Group Problem Solving Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 2.1.1.3
- 4.2.1.0
- 4.2.1.1
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
- PW
- tutorial
assets:
- livingcreature.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-letter-keys: true
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-letter-keys: true
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-letter-keys: true
myst:
  substitutions:
    params:
      vars:
        title: Moving Creature
      part1:
        ans1:
          value: The creature is speeding up because the distance between points equally
            spaced in time is increasing.
        ans2:
          value: The creature is slowing down because the distance between points
            equally spaced in time is increasing.
        ans3:
          value: The creature is maintaining a constant speed because the distance
            between points equally spaced in time is increasing at a constant rate.
        ans4:
          value: The creature is stationary because the points form a horizontal line.
      part2:
        ans1:
          value: The creature maintains a constant space because the distance between
            points equally spaced in time is constant.
        ans2:
          value: The creature is stationary because the distance between points equally
            spaced in time is constant.
        ans3:
          value: The creature is speeding up because the dots form a line with a positive
            slope.
        ans4:
          value: The creature is slowing down because the dots form a line with a
            positive slope.
      part3:
        ans1:
          value: This could describe a loon or a duck accelerating across the surface
            of the water before taking flight at a constant speed, about 30$^{\circ}$
            above the water.
        ans2:
          value: This could describe a loon or a duck flying at a constant speed across
            the surface of the water before taking flight with an increasing speed,
            about 30$^{\circ}$ above the water.
        ans3:
          value: This could describe a loon or a duck at rest on the surface of the
            water before taking flight at a constant speed, about 30$^{\circ}$ above
            the water.
        ans4:
          value: This could describe a loon or a duck at rest on the surface of the
            water before taking flight with an increasing speed, about 30$^{\circ}$
            above the water.
---
# {{ params.vars.title }}
A set of dots representing the position of a living creature is shown in the figure. The spots are equally spaced in time.

<img longdesc="Moving Creature.md#desc" alt="Motion diagram of the creature." src="livingcreature.png" width="500px">

<div id="desc">
<h5>Long Description of image: Motion diagram of the creature.</h5>
The motion diagram consists of seven dots numbered 0 to 6.
Dots 0 to 3 form a horizontal line with an increasing spacing between adjacent dots.
Dots 3 to 6 form a straight line with positive slope with an equal spacing between adjacent dots.
<p>Long description ends.</p>
<div>

## Part 1

From dots 0 to 3, is the creature slowing down, speeding up, stationary or maintaining a constant speed? Please explain your answer.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Part 2

From dots 3 to 6, is the creature slowing down, speeding up, stationary or maintaining a constant speed?  Please explain your answer.

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}
- {{ params.part2.ans4.value}}

## Part 3

Describe a physical situation this set of dots could represent.  (Choose a creature and explain what it is doing from time 0 to time 6).

### Answer Section

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}
- {{ params.part3.ans3.value}}
- {{ params.part3.ans4.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)