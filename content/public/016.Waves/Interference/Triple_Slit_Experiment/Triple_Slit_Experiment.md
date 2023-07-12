---
title: Triple Slit Experiment
topic: Waves
author: John Hopkinson
source: Phys 122 2017W2 GPS vI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 22.3.3.1
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
- JR
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.01
    weight: 1
    allow-blank: true
    label: $(y_{1}-y_{0}) = $
    suffix: $\rm{mm}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.001
    weight: 1
    allow-blank: true
    label: $(y_{10}-y_{9}) = $
    suffix: $\rm{mm}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.01
    weight: 1
    allow-blank: true
    label: $(y_{1}-y_{0})_{\text{small angle}} \approx$
    suffix: $\rm{mm}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.001
    weight: 1
    allow-blank: true
    label: $(y_{10}-y_{9})_{\text{small angle}} \approx$
    suffix: $\rm{mm}$
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
    params_vars_title: Triple Slit Experiment
    params_m: 2
    params_part5_ans1_value: It is a good approximation to the spacing between the
      $m = 0$ and $ m = $ 2 peak, but not a great approximation to the spacing between
      the $m = 9$ and $ m = 10$ peak as the angle for $y_{10}$ is just outside the
      range of validity of the small angle approximation.
    params_part5_ans2_value: It is a good approximation to both spacings since the
      angles remain small out to $m = 10$.
    params_part5_ans3_value: It is a not a good approximation either angle as one
      cannot meaningfully use the small angle approximation in diffraction problems
      even when the wavelength is small relative to the slit spacing.
    params_part6_ans1_value: The spacing between the maxima would increase.
    params_part6_ans2_value: The spacing between the maxima would not change.
    params_part6_ans3_value: The spacing between the maxima would decrease.
---
# {{ params_vars_title }}
A triple-slit experiment has a slit spacing $d = 20 \rm{\mu m}$ and is illuminated by a laser of wavelength $\lambda = 500 \rm{nm}$ and is a distance $L = 10 \rm{cm}$ from a screen.

<!-- Button trigger modal -->

<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong">
  Hint
</button>

<!-- Modal -->

<div class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
  <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Hint</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
          Diffraction from multiple slits (two, three, four, ..., diffraction grating) shows constructive interference (bright peaks) when the path length difference $\Delta r = d\sin(\theta_m) = m\lambda$, where $m$ (an integer) is the order of the diffraction maximum, $\theta_m$ is the angle relative to the normal vector defining the plane of the slits, and $\lambda$ is the wavelength of the light. To find the distance of the $m^{\text{th}}$ order diffraction maximum from the central maximum on a screen a perpendicular distance $L$ from the slits, one can write $y_m = L\tan(\theta_m)$.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
    </div>
  </div>
</div>

## Part 1

Without using the small angle approximation calculate the spacing between the $m = 0$ and $m = {{ params_m }} $ peaks.

### Answer Section

Please enter in a numeric value in $\rm{mm}$.

### pl-submission-panel

{{feedback.part1_ans}}

## Part 2

Without using the small angle approximation calculate the spacing between the $m = 9$ and $m = 10$ peaks.

### Answer Section

Please enter in a numeric value in $\rm{mm}$.

### pl-submission-panel

{{feedback.part2_ans}}

## Part 3

In the small angle approximation $\tan(\theta) = \sin(\theta) = \theta$, where $\theta$ is in radians. What is the spacing between the $m = 0$ and $m = {{ params_m }}$ peaks in the small angle approximation?

### Answer Section

Please enter in a numeric value in $\rm{mm}$.

### pl-submission-panel

{{feedback.part3_ans}}

## Part 4

What is the spacing between the $m = 9$ and $m = 10$ peaks in the small angle approximation?

### Answer Section

Please enter in a numeric value in $\rm{mm}$.

### pl-submission-panel

{{feedback.part4_ans}}

## Part 5

Based on your results in Parts 1-4 is the small angle approximation a good approximation for the spacing between the $m = 0$ and $m = {{ params_m }}$ peaks and the $m = 9$ and $m = 10$ peaks?

### Answer Section

- {{ params_part5_ans1_value }}
- {{ params_part5_ans2_value }}
- {{ params_part5_ans3_value }}

## Part 6

If the colour of the laser changed to purple with a wavelength $\lambda = 400 \rm{nm}$, how would the spacing change?

### Answer Section

- {{ params_part6_ans1_value }}
- {{ params_part6_ans2_value }}
- {{ params_part6_ans3_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)