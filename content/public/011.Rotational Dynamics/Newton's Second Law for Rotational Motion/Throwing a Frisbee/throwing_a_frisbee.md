---
title: Throwing a Frisbee
topic: Rotational Dynamics
author: John Hopkinson
source: Phys 112 2019W1 Practice Final Q8
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.2.0
- 10.5.2.2
- 11.3.1.4
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
- NR
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\alpha= $
    suffix: $\pi\frac{\rm{rad}}{\rm{s^2}}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\rm{I}= $
    suffix: $\rm{kg \cdot m^2}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\tau_{\rm{net}}= $
    suffix: $\rm{N \cdot m}$
part4:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
substitutions:
  params:
    vars:
      title: Throwing a Frisbee
    dw: 12
    dt: 0.2
    m: 0.158
    d: 0.492
---
# {{ params.vars.title }}
As a frisbee (a flying disk) is released, it is spun so that its angular velocity increases from 0 to {{ params.dw }} $\pi \; \rm{rad/s}$ in {{ params.dt }} $\rm{s}$.

## Part 1

Find the angular acceleration of the frisbee assuming that it is constant over this time interval. Your answer should be a multiple of $\pi$.

### Answer Section

Please enter in a numeric value in $\pi\frac{\rm{rad}}{\rm{s^2}}$.

## Part 2

Assuming that the frisbee is a solid disk of mass $m=$ {{ params.m }} $\rm{kg}$ and diameter $d=$ {{ params.d }} $\rm{m}$, find the moment of inertia of the frisbee about its centre.

### Answer Section

Please enter in a numeric value in $\rm{kg \cdot m^2}$.

## Part 3

Find the net torque acting on the frisbee during this time interval.

### Answer Section

Please enter in a numeric value in $\rm{N \cdot m}$.

## Part 4

Explain what role you think spinning the frisbee has in the stable motion of the frisbee while it is in flight.

### Answer Section

Answer in 2-4 sentences, try and use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)