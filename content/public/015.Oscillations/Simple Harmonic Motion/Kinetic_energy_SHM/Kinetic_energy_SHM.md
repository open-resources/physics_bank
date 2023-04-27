---
title: Kinetic energy from velocity in SHM
topic: Oscillations
author: John Hopkinson
source: Phys122 2022S T8 Q1 V1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 15.2.1.0
- 15.2.2.0
difficulty:
- medium
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- average
tags:
- HZ
assets:
- koscillate.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T = $
    suffix: $\rm{s}$
    comparison: sigfig
    digits: 2
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
    fixed-order: true
myst:
  substitutions:
    params_vars_title: Kinetic energy from velocity in SHM
    params_vars_units: $rm\{s}$
    params_part2_ans1_value: Figure A
    params_part2_ans1_feedback: What is the period of oscillation of the velocity?  How
      long should it be between zeroes of the kinetic energy?  Are the periods of
      oscillation of the energy and velocity the same?
    params_part2_ans2_value: Figure B
    params_part2_ans2_feedback: What is the period of oscillation of the velocity?  How
      long should it be between zeroes of the kinetic energy?  Are the periods of
      oscillation of the energy and velocity the same?
    params_part2_ans3_value: Figure C
    params_part2_ans3_feedback: Great! You got it.
    params_part2_ans4_value: Figure D
    params_part2_ans4_feedback: Can the kinetic energy $K = \frac{1}{2}mv^2$ ever
      be negative?
    params_part2_ans5_value: Figure E
    params_part2_ans5_feedback: At the time when the velocity is first zero, is the
      kinetic energy at its maximum or minimum?
---
# {{ params_vars_title }}

## Part 1

For a simple harmonic oscillator with velocity $v_x(t) = v\_{max}\sin(\frac{2\pi t}{12} - \frac{\pi}{3})$, find the period of oscillation of the velocity.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Identify which of the below graphs represents the kinetic energy as a function of time for a simple harmonic oscillator with velocity $v_x(t) = v\_{max}\sin(\frac{2\pi t}{12} - \frac{\pi}{3})$.

<img src="koscillate.png" alt="Image of five graphs. The five graphs represent the kinetic energy as a function of time for a simple harmonic oscillator. Graph A shows positive kinetic energy at all times with K = 0 at t = 1s. Graph B shows positive kinetic energy at all times with K = 0 at t = 1s. Graph C shows positive kinetic energy at all times with K = 0 at t = 2s. Graph D shows negative kinetic energy at 2s < t < 8s with K = 0 at t = 2s and t = 8s. Graph E shows positive kinetic energy at all times with K = 0 at t = 4s." width = "600" height = "500">

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params_part2_ans4_value }}
- {{ params_part2_ans5_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)