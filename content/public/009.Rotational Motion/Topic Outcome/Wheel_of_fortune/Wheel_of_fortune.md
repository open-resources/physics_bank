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
    w_i: 1.0471975511965976
    t: 5
    part1:
      ans1:
        value: 0.05
      ans2:
        value: 0.22
      ans3:
        value: 0.44
      ans4:
        value: 1.05
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

## Attribution

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).