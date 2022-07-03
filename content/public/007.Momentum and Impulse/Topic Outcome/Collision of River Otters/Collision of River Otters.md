---
title: Collision of River Otters
topic: Momentum and Impulse
author: John Hopkinson
source: PHYS 112 2020W Final Q8
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.2.1.1
- 7.2.1.2
- 7.5.1.3
- 7.5.1.4
- 7.5.1.5
- 7.5.1.9
- 7.6.1.0
- 7.6.1.1
- 7.6.1.2
- 7.4.1.2
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
- PW
assets:
- riverotters.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_{ixs}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_{iys}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_{ixl}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_{iyl}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $P_{fx}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $P_{fy}= $
    suffix: $kg \cdot m/s$
    comparison: sigfig
    digits: 3
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^{\circ}$
    comparison: sigfig
    digits: 3
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_f= $
    suffix: $m/s$
part9:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Collision of River Otters
    m_s: 3.95
    m_l: 7.88
    vis: 4.28
    vil: 6.69
    theta_i: 48.1
    part9:
      ans1:
        value: Kinetic energy is lost in this collision.
      ans2:
        value: Kinetic energy is gained in this collision.
      ans3:
        value: Kinetic energy remains constant in this collision.
---
# {{ params.vars.title }}
Two river otters collide while sliding across frictionless ice and get tangled together following the (perfectly inelastic) collision as shown in the figure, where a coordinate system has been defined.

The smaller otter ($m_s =$ {{ params.m_s }} $kg$) is initially moving at $v\_{i_s} = $ {{ params.vis }} $m/s$ along the x-axis, while the larger otter ($m_l =$ {{ params.m_l }} $kg$) is initially moving at $v\_{i_l} = $ {{ params.vil }} $m/s$, $\theta_i=${{ params.theta_i }}$^{\circ}$ counterclockwise from the x-axis.

<img src="riverotters.png" alt="Figure of two river otters before and after collision. The coordinate system is a traditional cartesian plane. The two otters tangle after collision and move with velocity v f at an angle theta with respect to the horizontal axis." width=400>

## Part 1

Find the $x$-component of the initial momentum of the smaller otter.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 2

Find the $y$-component of the initial momentum of the smaller otter.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 3

Find the $x$-component of the initial momentum of the larger otter.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 4

Find the $y$-component of the initial momentum of the larger otter.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 5

Find the $x$-component of the total final momentum of the tangled otters in component form.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 6

Find the $y$-component of the total final momentum of the tangled otters in component form.

### Answer Section

Please enter in a numeric value in $kg\cdot m/s$.

## Part 7

What direction do the river otters end up heading in, relative to the $x$-axis as defined in the figure?

### Answer Section

Please enter in a numeric value in degrees.

## Part 8

What is the speed of the otters after this collision?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 9

Is kinetic energy lost, gained, or does it remain constant in this collision?

If the difference in kinetic energy is less than 0.05, consider that kinetic energy has remained unchanged.

### Answer Section

- {{ params.part9.ans1.value}}
- {{ params.part9.ans2.value}}
- {{ params.part9.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)