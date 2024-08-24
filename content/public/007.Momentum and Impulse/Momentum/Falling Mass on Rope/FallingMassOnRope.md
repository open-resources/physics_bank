---
title: Falling Mass on Rope
topic: Momentum and Impulse
author: Patrick Jilek-Rodriguez
source: WebWork
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.1.4
- 7.3.1.4
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
- PJ
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      title: Falling Mass on Rope
      part1:
        ans1:
          value: $mg(t_2-t_1)$
          feedback: Nope
        ans2:
          value: $mv^2/2$
          feedback: Nope
        ans3:
          value: integral of the net force over the stretching time of the rope
          feedback: Well done!
        ans4:
          value: mass multiplied by the average velocity
          feedback: Nope
        ans5:
          value: $mg(L_2-L_1)$
          feedback: Nope
---
# {{ params.vars.title }}

## Part 1

The change in momentum of a falling mass attached to a fixed rope is equal to:

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)