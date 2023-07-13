---
title: Diffraction Part 1
topic: Optics
author: John Hopkinson
source: GPS V 2020 Phys122
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
outcomes:
- 22.4.2.1
- 22.4.2.2
- 22.4.3.0
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
- MP
assets:
- gratings.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Diffraction Part 1
    params_Lambda: 650
    params_L: 7
    params_part1_ans1_value: This is diffraction from a diffraction grating since
      it is bright enough for us to see.
    params_part1_ans1_feedback: While diffraction is brighter when more slits are
      involved, it is still possible to observe diffraction from double and single
      slits.
    params_part1_ans2_value: This is diffraction from a double slit since the maxima
      are equally spaced
    params_part1_ans2_feedback: The maxima would be equally spaced if this were diffraction
      from a double slit.  Are they equally spaced?
    params_part1_ans3_value: This is diffraction from a double slit since the central
      maximum is twice the width of the subsequent maxima.
    params_part1_ans3_feedback: The maxima produced by a double slit should be equally
      spaced.
    params_part1_ans4_value: This is diffraction from a single slit since the maxima
      are equally spaced.
    params_part1_ans4_feedback: Here the maxima are not equally spaced.
    params_part1_ans5_value: This is diffraction from a single slit since the central
      maximum is twice the width of subsequent maxima.
---
# {{ params_vars_title }}
Photographs of the diffraction of a red laser of wavelength $\lambda = 650$ nm are shown in figures (i) and (ii). A line of length $7$ cm indicates the length scale on the screen.

<img src="gratings.png" height = 500px>

## Useful Info

When monochromatic light of wavelength $\lambda$ passes through a double slit of separation $d$, <strong>constructive</strong> interference occurs at angles $\theta_m$, where $d\sin\theta_m = m\lambda$  and $m = {0, 1, 2, ...}$ is an integer.  This same relation holds true for light passing through a diffraction grating.  Light passing through a single slit will <strong>destructively</strong> interfere at angles $a\sin\theta_p = p \lambda$, where $p = {1, 2, 3, ..}$ is a non-zero integer and $a$ is the slit width. If a screen is placed at a distance $L$ behind the slit(s)/grating, bright and dark lines are observed at a distance $y$ from the central maximum given by  $y = L\tan\theta$. When the small angle approximation $\theta \approx \sin\theta \approx \tan\theta$ is valid ($\theta \ll 1$ expressed in radians), one expects a double-slit pattern to display equally spaced bright maxima, whereas a single-slit pattern exhibits a central maximum that is twice as wide as the subsequent maxima.

## Part 1

Is the diffraction of this laser from a diffraction grating, a double slit or single slit?

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)