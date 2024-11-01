---
title: Diffraction Part 3
topic: Optics
author: John Hopkinson
source: GPS V 2020 Phys122
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
showCorrectAnswer: false
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
    params:
      vars:
        title: Diffraction
      d: 60
      part1:
        ans1:
          value: It doesn't hold at all
          feedback: Make sure that your calculator is in radian mode
        ans2:
          value: Four digits
          feedback: This means that the small angle approximation is very good for
            small angles
        ans3:
          value: Two digits
          feedback: Hmm, not quite!
        ans4:
          value: One digit
          feedback: Hmm, not quite!
---
# {{ params.vars.title }}
Photographs of the diffraction of a red laser of wavelength $\lambda = 650$ nm are shown in figures (i) and (ii). A line of length $7$ cm indicates the length scale on the screen.

<img src="gratings.png" height = 500px>

## Useful Info

When monochromatic light of wavelength $\lambda$ passes through a double slit of separation $d$, <strong>constructive</strong> interference occurs at angles $\theta_m$, where $d\sin\theta_m = m\lambda$  and $m = {0, 1, 2, ...}$ is an integer.  This same relation holds true for light passing through a diffraction grating.  Light passing through a single slit will <strong>destructively</strong> interfere at angles $a\sin\theta_p = p \lambda$, where $p = {1, 2, 3, ..}$ is a non-zero integer and $a$ is the slit width. If a screen is placed at a distance $L$ behind the slit(s)/grating, bright and dark lines are observed at a distance $y$ from the central maximum given by  $y = L\tan\theta$.  When the small angle approximation $\theta \approx \sin\theta \approx \tan\theta$ is valid ($\theta \ll 1$ expressed in radians), one expects a double-slit pattern to display equally spaced bright maxima, whereas a single-slit pattern exhibits a central maximum that is twice as wide as the subsequent maxima.

## Part 1

If the screen was {{params.d}} cm away from the diffraction that caused these patterns, to how many digits after the decimal would the small angle approximation ($\theta \approx$ tan$^{-1} \theta$) hold for the largest angle?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)