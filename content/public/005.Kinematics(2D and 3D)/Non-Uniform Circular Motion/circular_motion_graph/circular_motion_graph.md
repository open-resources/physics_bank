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
myst:
  substitutions:
    params_vars_title: Circular Motion Graph
    params_r: 3
    params_t: 0.5
    params_wmax: 10
    params_part1_ans1_value: $t = 0\rm{s} $ to $ t = 1\rm{s}$, positive
    params_part1_ans1_feedback: Hmm... try again.
    params_part1_ans2_value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, positive
    params_part1_ans2_feedback: Hmm... try again.
    params_part1_ans3_value: $t = 1\rm{s} $ to $ t = 2\rm{s}$, positive
    params_part1_ans3_feedback: Great, you got it!
    params_part1_ans4_value: $t = 2\rm{s} $ to $ t = 3\rm{s}$, positive
    params_part1_ans4_feedback: Hmm... try again.
    params_part1_ans5_value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, negative
    params_part1_ans5_feedback: Hmm... try again.
    params_part2_ans1_value: $t = 0\rm{s} $ to $ t = 1\rm{s}$, positive
    params_part2_ans1_feedback: Great, you got it!
    params_part2_ans2_value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, positive
    params_part2_ans2_feedback: Hmm... try again.
    params_part2_ans3_value: $t = 1\rm{s} $ to $ t = 2\rm{s}$, positive
    params_part2_ans3_feedback: Hmm... try again.
    params_part2_ans4_value: $t = 2\rm{s} $ to $ t = 3\rm{s}$, positive
    params_part2_ans4_feedback: Hmm... try again.
    params_part2_ans5_value: $t = 0\rm{s} $ to $ t = 2\rm{s}$, negative
    params_part2_ans5_feedback: Hmm... try again.
    params_part7_ans1_value: Tangential to the circle
    params_part7_ans1_feedback: Great, you got it!
    params_part7_ans2_value: Radially inwards to the centre of the circle
    params_part7_ans2_feedback: Hmm... try again.
    params_part7_ans3_value: Radially outwards to the centre of the circle
    params_part7_ans3_feedback: Hmm... try again.
    params_part8_ans1_value: Tangential to the circle
    params_part8_ans1_feedback: Hmm... try again.
    params_part8_ans2_value: Radially inwards to the centre of the circle
    params_part8_ans2_feedback: Great, you got it!
    params_part8_ans3_value: Radially outwards to the centre of the circle
    params_part8_ans3_feedback: Hmm... try again.
---
# {{ params_vars_title }}
<img src="diagram.png" alt= "A graph of angular velocity (rad/s) vs. time (s). At 0s, it is -10 rad/s, with a constant linear slope towards 0 rad/s at 1s and 10 rad/s at 2s (this shape: /). From 2s to 3s, it is a constant 10 rad/s, producing a horizontal slope (-). "> 

The angular velocity of an object in circular motion at a distance $r =$ {{params_r}} $\rm{m}$ from the point of rotation is shown in Fig. 1.

## Part 1

Choose the option which correctly states at which times the object is speeding up and the sign of its angular acceleration during this period.

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}

## Part 2

Choose the option which correctly states at which times the object is slowing down and the sign of its angular acceleration during this period.

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params_part2_ans4_value }}
- {{ params_part2_ans5_value }}

## Part 3

Find the speed of the object at $t = 2 \rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 4

Find the magnitude of the centripetal acceleration at $t = $ {{params_t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 5

Find the tangential acceleration at $t = $ {{params_t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 6

Find the magnitude of the total acceleration at $t = $ {{params_t}} $\rm{s}$.

### Answer Section

Please enter in a numeric value.

## Part 7

At $t = 1 \rm{s}$, what is the direction of the acceleration?

### Answer Section

- {{ params_part7_ans1_value }}
- {{ params_part7_ans2_value }}
- {{ params_part7_ans3_value }}

## Part 8

At $t = 2.5 \rm{s}$, what is the direction of the acceleration?

### Answer Section

- {{ params_part8_ans1_value }}
- {{ params_part8_ans2_value }}
- {{ params_part8_ans3_value }}

## Part 9

What is the angular displacement from $t = 0 \rm{s}$, to $t = 1 \rm{s}$?

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)