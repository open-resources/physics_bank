---
title: Charge Distributions
topic: Electrostatics
author: John Hopkinson
source: Phys 122 2020 GPS VIII
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.6.1.2
- 18.6.1.3
- 18.6.1.4
- 18.11.2.4
- 18.11.5.1
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
assets:
- charge_distributions.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $r_{1} = $
    variables: R, d, x, k, Q, zero
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $V_{P} = $
    variables: R, d, x, k, Q, zero
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  pl-customizations:
    label: $E_{P,x} = $
    variables: R, d, x, k, Q, zero
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $V_{P}(x = -\frac{d}{2}) = $
    variables: R, d, x, k, Q, zero
    weight: 1
    allow-blank: false
part5:
  type: symbolic-input
  pl-customizations:
    label: $E_{P,x}(x = -\frac{d}{2}) = $
    variables: R, d, x, k, Q, zero
    weight: 1
    allow-blank: false
myst:
  substitutions:
    params_vars_title: Charge Distributions
---
# {{ params_vars_title }}
Two thin rings of radius $R$ and charges $Q_1 = Q$ and $Q_2 = -Q$ are centred along the $x$-axis as shown in the figure below.

<img src="charge_distributions.png" width=400 alt="Two thin rings of radius R are concentric with the x axis. One ring of charge Q1 equal to Q has an x position of -d, while the other ring of charge Q2 equal to -Q has an x position of 0. A point P is shown at some positive value of x with a distance r1 to the ring of charge Q1 at an x position of -d.">

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
          Along the axis of symmetry of a uniformly charged ring, we've seen that the electric potential can be expressed as $V = \frac{kQ}{r}$, where $r$ is the distance to a point on the axis of symmetry of the ring from any point on the ring, $Q$ is the total charge on the ring, and $k$ is Coulomb's constant.  When we have more than one ring, we can use regular addition to add the contributions to the total electric potential of each ring, accounting for the charge on each ring and the distance of each ring's charges from the point of interest.  To calculate electric fields along this line of symmetry we know that the electric field is the negative of rate of change of the electric potential with respect to position.  Along our axis of symmetry (the $x$-axis in this problem) this means that the electric field is given by $E_x = -\frac{dV}{dx}$.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
    </div>
  </div>
</div>

## Part 1

Write an expression in terms of $x$, $d$ and $R$ for the distance, $r_1$, for the distance of any point on ring 1 from point $P$.
Note that this is a right-angled triangle so you can use the pythagorean theorem.

Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $R$ | R   |
| $d$ | d   |
| $x$ | x   |
| $k$ | k   |
| $Q$ | Q   |

**If the answer is 0, enter "zero"**.

### Answer Section

### pl-submission-panel

{{feedback.part1_ans}}

## Part 2

Write an expression for the electric potential at point $P$ due to the two thin rings in terms of $Q$, $R$, $d$ and $x$.

Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $R$ | R   |
| $d$ | d   |
| $x$ | x   |
| $k$ | k   |
| $Q$ | Q   |

**If the answer is 0, enter "zero"**.

### Answer Section

### pl-submission-panel

{{feedback.part2_ans}}

## Part 3

From your expression for the potential energy find the electric field at point $P$.
Note that it points along the $x$-axis, and remember to use the chain rule.

Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $R$ | R   |
| $d$ | d   |
| $x$ | x   |
| $k$ | k   |
| $Q$ | Q   |

**If the answer is 0, enter "zero"**.

### Answer Section

### pl-submission-panel

{{feedback.part3_ans}}

## Part 4

When $x = -\frac{d}{2}$ evaluate the electric potential.

Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $R$ | R   |
| $d$ | d   |
| $x$ | x   |
| $k$ | k   |
| $Q$ | Q   |

**If the answer is 0, enter "zero"**.

### Answer Section

### pl-submission-panel

{{feedback.part4_ans}}

## Part 5

When $x = -\frac{d}{2}$ evaluate the electric field.

Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $R$ | R   |
| $d$ | d   |
| $x$ | x   |
| $k$ | k   |
| $Q$ | Q   |

**If the answer is 0, enter "zero".**

### Answer Section

### pl-submission-panel

{{feedback.part5_ans}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)