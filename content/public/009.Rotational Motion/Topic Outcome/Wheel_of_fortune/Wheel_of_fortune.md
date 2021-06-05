---
title: Wheel of Fortune
topic: Kinematics
author: Jake Bobowski
source: 2016 Final Q2
template_version: 0.3
outcomes:
- 9.1.1.1
tags:
- quiz
- homework
assets:
- q2_2016Final.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      units: rad/s
      title: Wheel of Fortune
    w_i: 0.7853981633974483
    t: 4
    part1:
      ans1:
        value: 0.02
      ans2:
        value: 0.15
      ans3:
        value: 0.31
      ans4:
        value: 0.79
---
# {{ params.vars.title }}
## Part 1

I want to win a game of Wheel-of-Fortune.
The grand prize is initially located at a position at the top of the wheel (shown) and I only win if the wheel stops when the prize is at the position to the right ($\\theta$ = 0).\
I note that when another contestant set the wheel spinning at $w_i = {{params.w_i}} {rad\\over s}$, it takes {{params.t}} seconds to stop.
With which initial velocity should I spin the wheel to win the prize?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
