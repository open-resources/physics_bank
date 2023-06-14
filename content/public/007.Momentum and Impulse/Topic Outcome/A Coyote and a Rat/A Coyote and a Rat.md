---
title: A Coyote and a Rat
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2017W1 002 Final Q15
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 4.1.1.1
- 4.9.1.0
- 7.2.1.1
- 7.5.1.3
- 7.5.1.4
- 7.5.1.9
- 6.1.1.4
- 6.3.1.2
- 6.7.1.0
- 6.9.1.3
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- PW
- JR
- final_exam
assets: null
part1:
  type: symbolic-input
  pl-customizations:
    label: $x_{\text{coyote}}(t) = $
    variables: t, dx, vr, ac
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $v_{\text{coyote}}(t) = $
    variables: t, dx, vr, ac
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  pl-customizations:
    label: $x_{\text{rat}}(t) = $
    variables: t, dx, vr, ac
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $v_{\text{rat}}(t) = $
    variables: t, dx, vr, ac
    weight: 1
    allow-blank: false
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{\text{catch}} = $
    suffix: $\rm{s}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{\text{coyote}}(t_{\text{catch}}) = $
    suffix: $\rm{m/s}$
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{\text{rat}}(t_{\text{catch}}) = $
    suffix: $\rm{m/s}$
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x_{\text{coyote}}(t_{\text{catch}}) = $x_{\text{rat}}(t_{\text{catch}})
      = $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: A Coyote and a Rat
    params_d_x: 30
    params_v_r: 8
    params_a_c: 8
---
# {{ params_vars_title }}
A coyote notices a rat running past it, toward a bush where the rat will be safe.
The rat is running with a constant velocity of $v\_{\text{rat}} = {{ params.v_r }} \rm{m/s}$ and the coyote is at rest, $\Delta x = {{ params.d_x }} \rm{m}$ to the left of the rat.
However, at $t=0 \rm{s}$, the coyote begins running to the right, in pursuit of the rat, with an acceleration of $a\_{\text{coyote}} = {{ params.a_c }} \rm{m/s^2}$.

Set your reference frame to be located with the origin at the original location of the coyote and the rightward direction corresponding to the positive $x$-direction.

## Part 1

Write the position of the coyote as a function of time $x\_{\text{coyote}}(t)$. Do not plug in numerical values for this part.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For                 | Use |
|---------------------|-----|
| $t$                 | t   |
| $\Delta x$          | dx  |
| $v\_{\text{rat}}$    | vr  |
| $a\_{\text{coyote}}$ | ac  |

### Answer Section

## Part 2

Write the velocity of the coyote as a function of time $v\_{\text{coyote}}(t)$. Do not plug in numerical values for this part.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For                 | Use |
|---------------------|-----|
| $t$                 | t   |
| $\Delta x$          | dx  |
| $v\_{\text{rat}}$    | vr  |
| $a\_{\text{coyote}}$ | ac  |

### Answer Section

## Part 3

Write the position of the rat as a function of time $x\_{\text{rat}}(t)$. Do not plug in numerical values for this part.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For                 | Use |
|---------------------|-----|
| $t$                 | t   |
| $\Delta x$          | dx  |
| $v\_{\text{rat}}$    | vr  |
| $a\_{\text{coyote}}$ | ac  |

### Answer Section

## Part 4

Write the velocity of the rat as a function of time $v\_{\text{rat}}(t)$. Do not plug in numerical values for this part.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| For                 | Use |
|---------------------|-----|
| $t$                 | t   |
| $\Delta x$          | dx  |
| $v\_{\text{rat}}$    | vr  |
| $a\_{\text{coyote}}$ | ac  |

### Answer Section

## Part 5

At what time does the coyote catch the rat $t\_{\text{catch}}$?

### Answer Section

Please enter in a numeric value in $\rm{s}$.

## Part 6

At this time, what is the velocity of the coyote $v\_{\text{coyote}}(t\_{\text{catch}})$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 7

At this time, what is the velocity of the rat $v\_{\text{rat}}(t\_{\text{catch}})$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 8

What is the location at which the coyote will catch the rat $x\_{\text{coyote}}(t\_{\text{catch}}) = x\_{\text{rat}}(t\_{\text{catch}})$?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)