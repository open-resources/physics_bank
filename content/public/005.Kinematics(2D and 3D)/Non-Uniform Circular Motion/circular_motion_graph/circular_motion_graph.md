---
title: Circular Motion Graph
topic: Non-Uniform Circular Motion
author: John Hopkinson
source: PHYS 112 2019W1 GPS IX
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
- 5.6.2.0
- 5.6.3.0
- 5.7.1.1
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
- EX
assets:
- diagram.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_c = $
    suffix: $\rm{m/s^2}$
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_t = $
    suffix: $\rm{m/s^2}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
part7:
  type: multiple-choice
  pl-customizations:
    weight: 1
part8:
  type: multiple-choice
  pl-customizations:
    weight: 1
part9:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta \theta = $
    suffix: $\rm{rad}$
substitutions:
  params:
    vars:
      title: Circular Motion Graph
    r: 4
    t: 0.8
    wmax: 10
    part1:
      ans1:
        value: $t = 0\rm{s} $ to $ t = 1\rm{s}$, positive
        feedback: Hmm... try again.
      ans2:
        value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, positive
        feedback: Hmm... try again.
      ans3:
        value: $t = 1\rm{s} $ to $ t = 2\rm{s}$, positive
        feedback: Great, you got it!
      ans4:
        value: $t = 2\rm{s} $ to $ t = 3\rm{s}$, positive
        feedback: Hmm... try again.
      ans5:
        value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, negative
        feedback: Hmm... try again.
    part2:
      ans1:
        value: $t = 0\rm{s} $ to $ t = 1\rm{s}$, positive
        feedback: Great, you got it!
      ans2:
        value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, positive
        feedback: Hmm... try again.
      ans3:
        value: $t = 1\rm{s} $ to $ t = 2\rm{s}$, positive
        feedback: Hmm... try again.
      ans4:
        value: $t = 2\rm{s} $ to $ t = 3\rm{s}$, positive
        feedback: Hmm... try again.
      ans5:
        value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, negative
        feedback: Hmm... try again.
    part7:
      ans1:
        value: Tangential to the circle
        feedback: Great, you got it!
      ans2:
        value: Radially inwards to the centre of the circle
        feedback: Hmm... try again.
      ans3:
        value: Radially outwards to the centre of the circle
        feedback: Hmm... try again.
    part8:
      ans1:
        value: Tangential to the circle
        feedback: Hmm... try again.
      ans2:
        value: Radially inwards to the centre of the circle
        feedback: Great, you got it!
      ans3:
        value: Radially outwards to the centre of the circle
        feedback: Hmm... try again.
---
# {{ params.vars.title }}
<img src="diagram.png" alt= "A graph of angular velocity (rad/s) vs. time (s). At 0s, it is -10 rad/s, with a constant linear slope towards 0 rad/s at 1s and 10 rad/s at 2s (this shape: /). From 2s to 3s, it is a constant 10 rad/s, producing a horizontal slope (-). "> 

The angular velocity of an object in circular motion at a distance $r =$ {{params.r}} $\rm{m}$ from the point of rotation is shown in Fig. 1.

## Part 1

Choose the option which correctly states at which times the object is speeding up and the sign of its angular acceleration during this period.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Part 2

Choose the option which correctly states at which times the object is slowing down and the sign of its angular acceleration during this period.

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}

## Part 3

Find the speed of the object at $t = 2 \rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 4

Find the magnitude of the centripetal acceleration at $t = $ {{params.t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 5

Find the tangential acceleration at $t = $ {{params.t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 6

Find the magnitude of the total acceleration at $t = $ {{params.t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 7

At $t = 1 \rm{s}$, what is the direction of the acceleration?

### Answer Section

- {{ params.part7.ans1.value }}
- {{ params.part7.ans2.value }}
- {{ params.part7.ans3.value }}

## Part 8

At $t = 2.5 \rm{s}$, what is the direction of the acceleration?

### Answer Section

- {{ params.part8.ans1.value }}
- {{ params.part8.ans2.value }}
- {{ params.part8.ans3.value }}

## Part 9

What is the angular displacement from $t = 0 \rm{s}$, to $t = 1 \rm{s}$?

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)