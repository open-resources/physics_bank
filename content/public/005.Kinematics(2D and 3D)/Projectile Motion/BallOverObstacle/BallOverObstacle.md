---
title: Ball Over Obstacle
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.0
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
- RG
- PJ
assets:
- BallOverObstacle.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Ball Over Obstacle
      phrases:
        ball: baseball
        action: throws
        obstacle: wall
      d: 56
      h: 3
      v: 28
      theta: 61
      part1:
        ans1:
          value: It clears the wall
          feedback: Correct!
        ans2:
          value: It hits the wall
          feedback: Try again...
        ans3:
          value: It doesn't even reach the wall
          feedback: Try again...
---
# {{ params.vars.title }}
A person {{params.phrases.action}} a {{params.phrases.ball}} towards their friend who is behind a ${{params.h}} \ \rm{m}$ {{params.phrases.obstacle}}. The {{params.phrases.ball}} has an initial velocity of ${{params.v}} \ \rm{m/s}$ at an angle ${{params.theta}}^\circ$ relative to ground.

<img src="BallOverObstacle.png" width="800px">

## Part 1

If the {{params.phrases.obstacle}} is ${{params.d}} \ \rm{m}$ away, how far does the {{params.phrases.ball}} go?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)