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
    params:
      vars:
        title: Raman Diffraction
      lambda1: 750
      lambda2: 550
      part1:
        ans1:
          value: The diffraction angle is larger for the $750$ $\rm{nm}$ light.
          feedback: Correct, since $d\sin(\theta) = m\lambda$ where $m$ is an integer,
            larger wavelengths $\lambda$ diffract at larger angles $\theta$ for fixed
            slit spacing $d$
        ans2:
          value: The diffraction angle is smaller for the $750$ $\rm{nm}$ light.
          feedback: No, write an expression for the angles at which constructive interference
            occurs in terms of the spacing between slits $d$, the angle $\theta$,
            and the wavelength $\lambda$.
        ans3:
          value: The diffraction angle is the same for both the $750$ $\rm{nm}$ and
            $550$ $\rm{nm}$ light.
          feedback: No, diffraction angles do depend on the wavelength of light.
        ans4:
          value: Light doesn't exist outside of the visible range from $400$ $\rm{nm}$
            to $700$ $\rm{nm}$.
          feedback: Light between $400$ $\rm{nm}$ and $700$ $\rm{nm}$ is visible to
            humans, but the electromagnetic spectrum (light) does not have limits.
        ans5:
          value: Light doesn't diffract since it is a praticle.
          feedback: While light does have a particle nature, it is also has been observed
            to diffract.
---
# {{ params.vars.title }}
A diffraction grating is used in Raman spectroscopy to distinguish between ${{ params.lambda1 }}$ $\rm{nm}$ and ${{ params.lambda2 }}$ $\rm{nm}$ light.

## Part 1

Which of the statements below is true?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)