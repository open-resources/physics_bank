---
title: Frequency/Period of Oscillation
topic: Oscillations
author: John Hopkinson
source: Physics 122 Midterm 1 Q2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 15.4.1.1
difficulty:
- undefined
randomization:
- 2
- 4
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets:
- hangingdisk.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $= $
    variables: M, g, r
    weight: 1
    allow-blank: false
myst:
  substitutions:
    params_vars_title: Frequency/Period of Oscillation
    params_R: 8
    params_pendulum: ' period of oscillation of this physical pendulum.'
---
# {{ params_vars_title }}
A solid disk of mass $M$ and radius $R$ is swung from a massless string of length $R$ through a small angle as shown in Figure; Let $R$={{ params_R }}r.

<img src="hangingdisk.png" width="200" alt="A physical pendulum. The massless string is attached to the end of the solid disk of mass M. The center of the mass of the solid disk is indicated by the dot at its center">

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
          The moment of inertia about the center of a solid disk is given by \(I_{\text{cm}} = \frac{1}{2} MR^2\), and the moment of inertia about a parallel axis a distance \(l\) away from the center of an object is given by \(I = Ml^2 + I_{\text{cm}}\).
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
    </div>
  </div>
</div>

## Part 1

Find the {{ params_pendulum }}

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For  | Use|
|----- |----|
| $M$  | M  |
| $r$  | r  |
| $g$  | g  |

### Answer Section

### pl-submission-panel

### pl-answer-panel

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)