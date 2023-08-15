---
title: Wave on a String 1
topic: Waves
author: John Hopkinson
source: Phys 122 2017WT2 Tutorial 4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 16.1.1.0
- 16.1.1.1
- 16.3.1.1
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
- DM
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $ \pi m$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: null
part3:
  type: symbolic-input
  pl-customizations:
    label: $y = $
    variables: A
    weight: 1
    allow-blank: false
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: null
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
part6:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_d: 13
    params_vars_title: Wave on a String 1
    params_part5_ans1_value: Potential energy
    params_part5_ans2_value: Kinetic energy
    params_part5_ans3_value: Both potential and kinetic energy
    params_part5_ans4_value: Neither potential nor kinetic energy
    params_part6_ans1_value: Potential energy
    params_part6_ans2_value: Kinetic energy
    params_part6_ans3_value: Both potential and kinetic energy
    params_part6_ans4_value: Neither potential nor kinetic energy
---
# {{ params_vars_title }}

## Useful Info

Waves on a string satisfy $v = f \psi = w/k = \sqrt{T_s u}$ , where $f$ is the frequency of the source, $ \psi $ is the wavelength of the sinusoidal oscillation, $w = 2 \pi f = 2 \pi /T$ is the angular frequency, and $k = 2 \pi / \psi $ is the wavenumber, $T_s$ is the tension in the string, and $u$ is the linear density (mass per unit length) of the string. The speed of a wave on a string is a property of the string (its tension and mass per unit length). Standing waves on strings are only possible at frequencies where reflections from both ends of the string reinforce to produce nodes and antinodes at particular locations. A string fixed at both ends has nodes at both ends- a displacement of zero at all times at these locations. The fundamental frequency is the lowest frequency oscillation consistent with the boundary conditions. For a given string (of known tension and mass per unit length) the velocity is fixed, so the longest wavelength (or smallest wavenumber) oscillation corresponds to the lowest or fundamental frequency.

## Part 1

A standing wave on a string fixed at x = 0.00m and at x = {{params_d}}m satisfies y(x, t) = 2Asin(kx)cos(t).

At $x = 0.10 m$, a fixed string implies that $y(x = 0.1,t) = 0$. What values of the wave number, $k$, are possible? Express your answer as a formula in terms of a number, $ \pi $, and $m$, with units of $rad/m$.

### Answer Section

Please enter a numeric value in $ \pi m$.

### pl-submission-panel

{{ feedback.part1_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 2

For the fundamental frequency (or first harmonic), what value of $m$ should be chosen?

Note that the longest wavelength allowed by the boundary conditions is associated with the fundamental frequency of the oscillation on the string.

### Answer Section

Please enter in a numeric value in $m$.

### pl-submission-panel

{{ feedback.part2_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 3

For the fundamental frequency, what is the displacement (the value of $y$) of this wave at $x = 0.05 m$ at $t = 0 s$? Express your answer as a formula in terms of numbers and A.

$w = (2 \pi )/T$

### Answer Section

### pl-submission-panel

{{ feedback.part3_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 4

For the fundamental frequency, what is the displacement (the value of $y$) of this wave at $x = 0.05 m$ at $t = T/4$, where $T$ is the period of the fundamental mode?

### Answer Section

### pl-submission-panel

{{ feedback.part4_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 5

For the fundamental frequency, what type(s) of energy does this wave have at $t = 0 s$?

### Answer Section

- {{ params_part5_ans1_value }}
- {{ params_part5_ans2_value }}
- {{ params_part5_ans3_value }}
- {{ params_part5_ans4_value }}

### pl-submission-panel

{{ feedback.part5_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Part 6

For the fundamental frequency, what type(s) of energy does this wave have at $t = T/4 s$?

### Answer Section

- {{ params_part6_ans1_value }}
- {{ params_part6_ans2_value }}
- {{ params_part6_ans3_value }}
- {{ params_part6_ans4_value }}

### pl-submission-panel

{{ feedback.part6_ans }}

### pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.
Please remove this section if it is not application for this question.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)