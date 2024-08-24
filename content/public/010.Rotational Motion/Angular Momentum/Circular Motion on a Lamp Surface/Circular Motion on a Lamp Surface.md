---
title: Circular Motion on a Lamp Surface
topic: Rotational Motion
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.9.1.0
- 6.3.1.3
- 6.3.1.4
- 6.5.1.3
- 7.5.3.0
- 8.5.1.2
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
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{stable}= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_{1\ \min}= $
    suffix: $m_2\ \rm{kg}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_{1\ \max}= $
    suffix: $m_2\ \rm{kg}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{stable new}= $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
part6:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      m_2: 10.2
      m_1: 11.2
      theta: 32
      l: 4.0
      s: 1.0
      u: 2.41
      part6:
        ans1:
          value: True because work is done by the rope attached to mass $m_2$ which
            changes the total energy of the system.
        ans2:
          value: False, because the change in kinetic energy and gravitational potential
            energy of mass $m_2$ has been offset by a corresponding change in the
            K.E and G.P.E of mass $m_1$.
---
# Circular Motion on a Lamp Surface
An object of mass $m_2 = {{ params.m_2 }}\ \rm{kg}$ is attached to a freely hanging load of mass $m_1 = {{ params.m_1 }}\ \rm{kg}$ suspended vertically through a light inextensible rope of length $L = {{ params.l }}\ \rm{m}$. The object is also lying on a frictionless inverted funnel surface akin to the top surface of a lamp as illustrated below.

<img src="part1.png" width=600>

## Part 1

If the object is accelerated from rest to a speed $v$ in the direction shown, determine the speed $v\_{stable}$ of stable orbit of the rotating object about the vertical axis of the funnel in the position shown above.<br>
Treat the object and load as particles and neglect the radius of the pulley and air resistance.<br>
$\theta = {{ params.theta }}^{\circ}$, $s = {{ params.s }}\ \rm{m}$

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 2

What is the **minimum** mass of the hanging load($m_1$) for the rotating object($m_2$) to **attain a stable orbit** and **remain in contact** with the surface?<br>
Express your answer as a multiple of mass $m_2$.

### Answer Section

Please enter in a numeric value.

## Part 3

What is the **maximum** mass of the hanging load($m_1$) for the rotating object($m_2$) to **attain a stable orbit** and **remain in contact** with the surface?<br>
Express your answer as a multiple of mass $m_2$.

### Answer Section

Please enter in a numeric value.

## Part 4

Using conservation of angular momentum determine the final radius of stable orbit gained by mass $m_2$ when it is projected with a speed of $u = {{ params.u }}\ \rm{m/s}$ at a distance of $s = {{ params.s }}\ \rm{m}$ from the pulley.

<img src="part2.png" width=600>

<i>Does your answer confirm the inference in part 4?</i>

### Answer Section

Please enter in a numeric value in $m$.

## Part 5

What is the new speed of the final stable orbit gained by mass $m_2$?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 6

It seems attaining a stable orbit requires external work to be done on the system since the speed of mass $m_2$ has changed from its initial speed, therefore total mechanical energy(K.E and G.P.E) has **NOT** been conserved.<br>
Is this true or false?

### Answer Section

- {{ params.part7.ans1.value }}
- {{ params.part7.ans2.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)