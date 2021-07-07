---
title: Wheel of Fortune
topic: Rotational Motion
author: Jake Bobowski
source: 2016 Final Q2
template_version: 1.0
attribution: standard
outcomes:
- 9.1.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
assets:
- wheel_of_fortune.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      units: rad/s
      title: Wheel of Fortune
    w_i: 0.79
    t: 6
    w_int: 4
    part1:
      ans1:
        value: 1.24
      ans2:
        value: 1.11
      ans3:
        value: 2.23
      ans4:
        value: $\pi$/4
---
# {{ params.vars.title }}
I want to win a game of Wheel-of-Fortune.
The grand prize is initially located at a position at the top of the wheel (shown) and I only win if the wheel stops when the prize is at the position to the right ($\theta$ = 0).I note that when another contestant set the wheel spinning at $w_i = {\pi \over {{params.w_int}}} {rad\over s}$, it takes {{params.t}} seconds to stop.
## Part 1

With which initial velocity should I spin the wheel to win the prize?

<img src="wheel_of_fortune.png" alt="Image of a wheel showing the winning section to be between the top center of the wheel, and approximately 10 degrees to the left." width=300>

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)