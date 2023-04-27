---
title: Stuck Together Collision
topic: Momentum and Impulse
author: John Hopkinson
source: Phys 112 2019W1 Practice Final Q7
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.1.2
- 7.5.1.3
- 7.5.1.4
- 7.5.1.9
- 7.6.1.0
- 7.6.1.1
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
- NR
assets:
- collisioninelastic.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Stuck Together Collision
        units: $^\circ$
      k: 4
      part1:
        ans1:
          value: 14.0
          feedback: Close! Make sure that you don't mix up your horizontal and vertical
            momentum.
        ans2:
          value: 63.4
          feedback: Not quite, try double checking your math again.
        ans3:
          value: 76.0
          feedback: Great! You got it.
        ans4:
          value: 78.7
          feedback: Not quite, try double checking your math again.
        ans5:
          value: 81.9
          feedback: This is a random angle, you probably selected this by mistake!
            Please try again!
---
# {{ params.vars.title }}
A perfectly inelastic collision occurs between an object of mass $m$ initially travelling along the positive $x$-axis at speed $v$, and an object of mass {{ params.k }}$m$ initially travelling along the positive $y$-axis at the same speed $v$. Following the collision the objects stick together and travel at a final speed $v_f$ at an angle $\theta$ degrees from the positive $x$-axis as shown in the figure below.

<img src="collisioninelastic.png" alt="A before picture, displaying a small mass travelling to the right at velocity v and a larger mass travelling up at velocity v, and an after picture, where the two masses are now stuck together and travelling at some velocity v sub f at an angle theta above the positive x-axis." width=400> <br />

## Part 1

The value of the angle $\theta$ is:

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)