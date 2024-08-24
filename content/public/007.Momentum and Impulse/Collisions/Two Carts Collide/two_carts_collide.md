---
title: Two Carts Collide
topic: Momentum and Impulse
author: Firas Moosvi
source: PHYS 111 2019W1 GPS XI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.3.1.2
- 7.3.1.3
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- NR
- JR
assets:
- graph1.png
- graph2.png
part1:
  type: file-upload
  pl-customizations:
    file-names: part1.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $(I_{\text{1 on 2}})_x = $
    suffix: $\rm{Ns}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{2xf} = $
    suffix: $\rm{m/s}$
part4:
  type: file-upload
  pl-customizations:
    file-names: part4.pdf
part5:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{1xf} = $
    suffix: $\rm{m/s}$
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{1xi} = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Two Carts Collide
        units: $\rm{m/s}$
      m1: 1.5
      m2: 370
      vi: -3
      part5:
        ans1:
          value: Magnets
          feedback: Not quite - Try again!
        ans2:
          value: Springs
          feedback: Not quite - Try again!
        ans3:
          value: Clay
          feedback: Correct! Clay would allow the carts to try to stick together following
            the collision!
        ans4:
          value: Velcro
          feedback: Correct! Velcro would allow the carts to try to stick together
            following the collision!
---
# {{ params.vars.title }}
Two carts collide on a frictionless track aligned with the $x$-axis. The force versus time graph for the force exerted by cart 1 on cart 2 is shown in the figure below.

<img src="graph1.png" width=400 alt="The force versus time graph for the force exerted by cart 1 on cart 2. The vertical axis is labelled force in newtons and the horizontal axis is labelled time in seconds. From 1 second to 2 seconds, the force increases linearly from 0 newtons to 0.4 newtons. From 2 seconds to 3 seconds, the force increases linearly from 0.4 newtons to 0.6 newtons. From 3 seconds to 4 seconds, the force decreases linearly from 0.6 newtons to 0.4 newtons. From 4 seconds to 5 seconds, the force decreases linearly from 0.4 newtons to 0 newtons. From 5 seconds to 6 seconds, the force decreases linearly from 0 newtons to negative 0.1 newtons. From 6 seconds to 7 seconds, the force increases linearly from negative 0.1 newtons to 0 newtons.">

## Part 1

Sketch the force versus time graph for the force exerted by cart 2 on cart 1 on the axes below.
Do this by downloading the image (right-click $\to$ save image as) and drawing on it.
Upload your graph as a pdf titled "part1.pdf". Be sure to label the graph $F\_{\text{2 on 1}}$ and put numbers on the vertical axis.

<img src="graph2.png" width=400 alt="Axes for a force versus time graph. The vertical axis is labelled force in newtons, but no numerical values have been labelled. The horizontal axis is labelled time in seconds, with 0 seconds at the origin and each tick mark denoting a 1 second interval.">

### Answer Section

File upload box will be shown here.

## Part 2

Find the $x$-component of the impulse that cart 1 exerts on cart 2 $(I\_{\text{1 on 2}})\_x$.

### Answer Section

Please enter in a numeric value in $\rm{kg \cdot m / s}$.

## Part 3

If cart 2 has a mass of {{ params.m2 }} $\rm{g}$ and an initial of velocity along the $x$-axis of $v\_{2xi} = ${{ params.vi }} $\rm{m/s}$, find the $x$-component of cart 2's velocity following the collision $v\_{2xf}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

Assuming that cart 1 starts to the left of cart 2 (and the positive x-axis is to the right), label the regions of the force vs. time graph you sketched in part 1 as having repulsive or attractive forces.
Re-upload your image as a pdf titled "part4.pdf".

### Answer Section

File upload box will be shown here.

## Part 5

What could cause an attractive force between the carts? (We have four end types on our carts: magnets, springs, clay, or Velcro).

### Answer Section

Select all the choices that apply.
Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part5.ans1.value }}
- {{ params.part5.ans2.value }}
- {{ params.part5.ans3.value }}
- {{ params.part5.ans4.value }}

## Part 6

If the collision was perfectly inelastic, what would be the $x$-component of the velocity of cart 1 after the collision $v\_{1xf}$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 7

If cart 1 had a mass of {{ params.m1 }} $\rm{kg}$ and underwent a perfectly inelastic collision, what was the $x$-component of its initial velocity $v\_{1xi}$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)