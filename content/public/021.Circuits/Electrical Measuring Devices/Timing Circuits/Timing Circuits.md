---
title: Timing Circuits
topic: Circuits
author: John Hopkinson
source: Physics 122 2019 Final Q6
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.13.1.0
- 21.8.1.0
difficulty:
- easy
randomization:
- 0
taxonomy:
- undefined
span:
- chapter
length:
- short
tags:
- L.K
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Timing Circuits
      part1:
        ans1:
          value: twice the capacitance on the one minute setting.
          feedback: Try again! Use the time constant relationship
        ans2:
          value: four times the capacitance on the one minute setting.
          feedback: Great! You got it. This is because the time constant relationship
            (τ=RC) at fixed R means τ=4τ so C=4C
        ans3:
          value: the same as the capacitance on the one minute setting.
          feedback: Try again! Use the time constant relationship
        ans4:
          value: one half the capacitance on the one minute setting.
          feedback: Try again! Use the time constant relationship
        ans5:
          value: one quarter the capacitance on the one minute setting.
          feedback: Try again! Use the time constant relationship
---
# {{ params.vars.title }}
Toasters have timing circuits.
If you want lightly toasted bread you might choose a time of one minute, while for an evenly brown toasted bagel you might choose a time of four minutes.

## Part 1

If the timing circuit in a toaster has a fixed resistance resistor in series with a variable capacitor, on the four minute setting the capacitance will be:

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)