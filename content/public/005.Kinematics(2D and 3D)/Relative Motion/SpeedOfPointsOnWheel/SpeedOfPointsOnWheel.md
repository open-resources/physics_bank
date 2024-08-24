---
title: Speed of Points on Wheel
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.9.1.0
- 5.6.2.1
- 5.8.1.2
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
- unknown
assets:
- SpeedOfPointsOnWheel.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Speed of Points on Wheel
      part1:
        ans1:
          value: $v$
          feedback: Think of how fast the cart is moving, and how fast the point is
            moving relative to the cart.
        ans2:
          value: $2v$
          feedback: Great! You got it.
        ans3:
          value: $0$
          feedback: Nope
        ans4:
          value: $-v$
          feedback: Why would it go the other way?
        ans5:
          value: $4v$
          feedback: That's a bit fast don't you think?
      part2:
        ans1:
          value: $v$
          feedback: Nope
        ans2:
          value: $2v$
          feedback: Nope
        ans3:
          value: $0$
          feedback: Correct!
        ans4:
          value: $-v$
          feedback: Nope
        ans5:
          value: $4v$
          feedback: Nope
---
# {{ params.vars.title }}
A cart on wheels is moving to the right with a velocity of $\vec{v}$ without slipping or skidding.
Point $A$ is situated at the top of a wheel, and point $B$ is at the bottom of a wheel.

<img src="SpeedOfPointsOnWheel.png">

## Part 1

What is the velocity of point $A$ relative to the ground?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Part 2

What is the velocity of point $B$ relative to the ground?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)