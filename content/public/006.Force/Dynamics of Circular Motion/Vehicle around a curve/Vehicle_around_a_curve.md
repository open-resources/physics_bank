---
title: Vehicle Around a Curve
topic: Force
author: John Hopkinson
source: Phys 112 2018W1 Practice Final Q12
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.5.1.3
- 6.12.1.1
- 6.12.2.0
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
- vehicle_diagrams.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $\Sigma F_x = $
    variables: W, n, theta
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $\Sigma F_y = $
    variables: W, n, theta
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  pl-customizations:
    label: $v = $
    variables: m, g, theta, r
    weight: 1
    allow-blank: false
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Vehicle Around a Curve
    params_vars_vehicle: pickup truck
    params_rad: 106
    params_ang: 9
---
# {{ params_vars_title }}
To ensure that motorists stay on roads with tight turns, it is common to tild (or bank) the roads toward the centre of the turn. A {{ params_vars_vehicle }} going around a banked curve without sliding is shown on the left of the figure below and its corresponding free body diagram is shown on the right of the figure below. In the free body diagram $\vec{W}_{\textit{E on v}}$ is the weight of the {{ params_vars_vehicle }}, $\vec{n}_{\textit{r on v}}$ is the normal force of the road on the {{ params_vars_vehicle }}, and $\vec{F}\_{\textit{net on v}}$ is the net force on the {{ params_vars_vehicle }}. Take the angle to be $\theta = {{ params_ang }}^\circ$ and the radius of curvature (distance from the centre of the circle to the {{ params_vars_vehicle }}) to be $r = {{ params_rad }}$ $\rm{m}$.

<img src="vehicle_diagrams.png" alt="On the left is an image showing a vehicle on a banked curved road. The image shows the back of the vehicle and a cross section of the banked road. The road is banked to the right and makes an angle of theta with the horizontal. On the right is an image of the free body diagram associated with the vehicle on the banked curved road. The normal force of the road on the vehicle makes an angle of theta with the positive y-axis and lies between the positive y-axis and the positive x-axis. The weight of the vehicle is along the negative y-axis. The net force on the vehicle is along the positive x-axis." width=400>

## Part 1

Write the equation for Newton's second law in the $x$-direction.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For                   | Use   |
|-----------------------|-------|
| $W\_{\textit{E on v}}$ | W     |
| $n\_{\textit{r on v}}$ | n     |
| $\theta$              | theta |

### Answer Section

## Part 2

Write the equation for Newton's second law in the $y$-direction.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For                   | Use   |
|-----------------------|-------|
| $W\_{\textit{E on v}}$ | W     |
| $n\_{\textit{r on v}}$ | n     |
| $\theta$              | theta |

### Answer Section

## Part 3

Solve the equations in Part 1 and Part 2 algebraically to determine the speed of the {{ params_vars_vehicle }}.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For      | Use   |
|----------|-------|
| $m$      | m     |
| $g$      | g     |
| $\theta$ | theta |
| $r$      | r     |

### Answer Section

## Part 4

Determine the speed of the {{ params_vars_vehicle }}.

### Answer Section

Please enter in a numeric value in $\rm{m/s}$

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)