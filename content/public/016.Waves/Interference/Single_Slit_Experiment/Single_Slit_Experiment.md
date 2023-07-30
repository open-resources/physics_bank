---
title: Single Slit Experiment
topic: Waves
author: John Hopkinson
source: Phys 122 2017W2 GPS vI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 22.4.3.0
- 22.4.3.1
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
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{\mu m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $I_{triple} = $
    suffix: $I_{single}$
myst:
  substitutions:
    params_vars_title: Single Slit Experiment
    params_m: 8
---
# {{ params_vars_title }}
Real multiple slit diffraction patterns experience diffraction effects both from the separation of the slits and the uniform slit width of each slit. This results in the superposition of a single slit pattern on top of the multiple slit pattern, such that the centre of the diffraction pattern remains bright, but the intensity decreases with increasing angle until the first diffraction minimum of the single slit pattern.

<!-- Button trigger modal -->

<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong1">
  Hint
</button>

<!-- Modal -->

<div class="modal fade" id="exampleModalLong1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
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

If the first diffraction minimum of the single slit pattern coincides with the $m = {{ params_m }}$ triple slit maximum, find the slit width $a$ (express your answer to two significant digits).

<!-- Button trigger modal -->

<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong2">
  Hint
</button>

<!-- Modal -->

<div class="modal fade" id="exampleModalLong2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
  <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Hint</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
          For a single slit diffraction pattern minima occur when:
          $$
          p\lambda = a\sin(theta)
          $$
          Where $a$ is the slit width,  $theta$ is  the angle of the single slit minimum, and $p$ is a non-zero integer.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
    </div>
  </div>
</div>

### Answer Section

Please enter in a numeric value in $\rm{\mu m}$.

### pl-submission-panel

{{feedback.part1_ans}}

## Part 2

If the intensity from a single slit is $I\_{single}$, find the intensity of the maximum at $\theta$ = 0 of the triple slit pattern $I\_{triple}$ in terms of $I\_{single}$.

<!-- Button trigger modal -->

<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong3">
  Hint
</button>

<!-- Modal -->

<div class="modal fade" id="exampleModalLong3" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
  <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Hint</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
          The intensity of light from multiple slits grows in proportion to the square of the amplitude of the light wave. For $N$ slits, the intensity grows as $N^2$.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
    </div>
  </div>
</div>

### Answer Section

Please enter in a numeric value in terms of $I\_{single}$.

### pl-submission-panel

{{feedback.part2_ans}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)