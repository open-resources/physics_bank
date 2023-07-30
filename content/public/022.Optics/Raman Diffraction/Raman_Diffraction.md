---
title: Raman Diffraction
topic: Optics
author: John Hopkinson
source: Phys122 2022S Tutorial 11 Q2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 22.4.4.1
- 22.4.4.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- JR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Raman Diffraction
    params_lambda1: 900
    params_lambda2: 600
    params_part1_ans1_value: The diffraction angle is larger for the $900$ $\rm{nm}$
      light.
    params_part1_ans1_feedback: Correct, since $d\sin(\theta) = m\lambda$ where $m$
      is an integer, larger wavelengths $\lambda$ diffract at larger angles $\theta$
      for fixed slit spacing $d$
    params_part1_ans2_value: The diffraction angle is smaller for the $900$ $\rm{nm}$
      light.
    params_part1_ans2_feedback: No, write an expression for the angles at which constructive
      interference occurs in terms of the spacing between slits $d$, the angle $\theta$,
      and the wavelength $\lambda$.
    params_part1_ans3_value: The diffraction angle is the same for both the $900$
      $\rm{nm}$ and $600$ $\rm{nm}$ light.
    params_part1_ans3_feedback: No, diffraction angles do depend on the wavelength
      of light.
    params_part1_ans4_value: Light doesn't exist outside of the visible range from
      $400$ $\rm{nm}$ to $700$ $\rm{nm}$.
    params_part1_ans4_feedback: Light between $400$ $\rm{nm}$ and $700$ $\rm{nm}$
      is visible to humans, but the electromagnetic spectrum (light) does not have
      limits.
    params_part1_ans5_value: Light doesn't diffract since it is a praticle.
    params_part1_ans5_feedback: While light does have a particle nature, it is also
      has been observed to diffract.
---
# {{ params_vars_title }}
A diffraction grating is used in Raman spectroscopy to distinguish between ${{ params_lambda1 }}$ $\rm{nm}$ and ${{ params_lambda2 }}$ $\rm{nm}$ light.

## Part 1

Which of the statements below is true?

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)