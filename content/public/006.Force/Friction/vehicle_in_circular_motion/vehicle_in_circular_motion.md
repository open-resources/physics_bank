---
title: Vehicle in Circular Motion
topic: Force
author: John Hopkinson
source: PHYS 112 2019W1 GPS 7
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
gradingMethod: Manual
outcomes:
- 5.6.3.0
- 6.3.1.2
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
- EX
assets:
- diagram1.png
- diagram2.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
part3:
  type: file-upload
  pl-customizations:
    file-names: fbd1.pdf
part4:
  type: number-input
  pl-customizations:
    rtol: 0.02
    weight: 1
    allow-blank: true
    label: $F_{friction} = $
    suffix: $\rm{N}$
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max} = $
    suffix: $\rm{m/s}$
part6:
  type: file-upload
  pl-customizations:
    file-names: fbd2.pdf
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{friction} = $
    suffix: $\rm{N}$
substitutions:
  params:
    vars:
      title: Vehicle in Circular Motion
      vehicle: van
    m: 1700.0
    v: 90.0
    r: 110.0
    theta: 21.0
    f_s: 0.6
    f_k: 0.4
    f_r: 0.02
    part1:
      ans1:
        value: centre, kinetic
        feedback: Close! Consider if the tires are rolling or sliding.
      ans2:
        value: outside, static
        feedback: Close! Consider why the vehicle is able to travel in a circle.
      ans3:
        value: centre, static
        feedback: Great! You got it!
      ans4:
        value: outside, kinetic
        feedback: 'Consider why the vehicle is able to travel in a circle, and if
          its tires are rolling or sliding. '
---
# {{ params.vars.title }}

## Part 1

A {{params.vars.vehicle}} of mass {{params.m}} $\rm{kg}$ in uniform circular motion accelerates towards the \_\_\_\_\_\_\_\_\_ of the circle due to the force of \_\_\_\_\_\_\_\_\_\_  friction between the {{params.vars.vehicle}}'s tires and the road. Please fill in the blanks with one of the options below (The choices are presented in the same order as they should appear in the sentence.)

Fig. 1
<img src="diagram1.png" alt = "The left side of the image is a diagram labelled 'Top view of vehicle in uniform circular motion' with a circle below. There is a top view of a vehicle on the leftmost point on the circle (180 degrees from the 0 position) with the y axis extending upwards from the vehicle, and the x axis extending similarly towards the right. The right side of the image is titled 'Rear view of vehicle in uniform circular motion' and contains two axes, z (upwards) and x (rightwards) which cross perpendicularly to form a four quadrant graph. At the origin of this graph is a rear-view symbol of the vehicle." width= 500>

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Part 2

If the {{params.vars.vehicle}} moves at {{params.v}} $\rm{km/h}$ around a circle of radius {{params.r}} $\rm{m}$, find the acceleration of the {{params.vars.vehicle}} in SI units.

### Answer Section

Please enter in a numeric value.

## Part 3

Draw a free body diagram in the $xz$ plane (the plane shown on the right of Fig.1) to show the forces acting on the {{params.vars.vehicle}} in the directions perpendicular to the {{params.vars.vehicle}}'s motion. Please upload a pdf titled "fbd1".

### Answer Section

File upload box will be shown here.

## Part 4

Find the size of the frictional force that keeps the {{params.vars.vehicle}} in circular motion.

### Answer Section

Please enter in a numeric value.

## Part 5

Above what speed would the {{params.vars.vehicle}}'s frictional force be overcome as the {{params.vars.vehicle}} tries to follow this curve?

$\mu_s =$ {{params.f_s}}, $\mu_k =$ {{params.f_k}}, $\mu_r =$ {{params.f_r}}

### Answer Section

Please enter in a numeric value.

## Part 6

If the curve was banked toward the centre of the circle at an angle of {{params.theta}}$^{\circ}$ as shown on the right of Fig. 2, draw a free body diagram for the forces acting on the {{params.vars.vehicle}} in the directions perpendicular to the direction of motion as the {{params.vars.vehicle}} moves around the circle at {{params.v}} $\rm{km/h}$.

Please upload a pdf titled "fbd2".

Fig. 2
<img src="diagram2.png" alt = "The left side of the image is a diagram labelled 'Top view of vehicle in uniform circular motion' with a circle below.  There is a top view of a vehicle on the leftmost point on the circle (180 degrees from the 0 position) with the y axis extending upwards from the vehicle, and the x axis extending similarly towards the right. The right side of the image is titled 'Rear view of vehicle in uniform circular motion' and contains two axes, z (upwards) and x (rightwards) which cross perpendicularly to form a four quadrant graph. At the origin of this graph is a rear-view symbol of a vehicle, angled downwards below the positive x-axis at an angle labelled as theta." width= 500>

### Answer Section

File upload box will be shown here.

## Part 7

Resolving your vectors, solve for the force of friction required to keep the {{params.vars.vehicle}} in uniform circular motion at this speed with the banked curve.

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)