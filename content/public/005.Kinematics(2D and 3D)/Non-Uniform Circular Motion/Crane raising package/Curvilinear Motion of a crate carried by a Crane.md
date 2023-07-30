---
title: Curvilinear Motion of a crate carried by a Crane
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.1
- 4.9.1.2
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
- RG
assets:
- crane.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_2= $
    suffix: $\rm{ms^{-1}}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_n= $
    suffix: $\rm{ms^{-2}}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_r= $
    suffix: $\rm{ms^{-2}}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_v_0: 37
    params_a: 2
    params_s: 99.2632288452649
    params_m: 15
    params_w: 637
---
# Curvilinear Motion of a crate carried by a crane
A crane moves a crate through point A with a speed of ${{ params.v_0 }}\ \rm{ms^{-1}}$ and increases the speed constantly at a rate of ${{ params_a }}\ \rm{ms^{-2}}$.<br>Find the magnitude of the crate's acceleration when the arc length is ${{ params_s }}\ \rm{m}$ and when $x_0 =0 \ \rm{m}$. <br>The equation of the arc is $y= m - \frac{x^{2}}{w}$
<br>
$w = {{ params_w }}\ \rm{m}$, $m = {{ params_m }}\ \rm{m}$

<img src="crane.png" width=600>

## Part 1

Find the speed $v_2$ when $x = 0\ \rm{m}$.

### Answer Section

Please enter the speed in $ms^{-1}$.

## Part 2

Find the radius of curvature.

### Answer Section

Please enter the radius in $m$.

## Part 3

Find $a_n$ at the same point.

### Answer Section

Please enter the acceleration in $ms^{-2}$.

## Part 4

Find the total acceleration.

### Answer Section

Please enter the acceleration in $m^s{-2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)