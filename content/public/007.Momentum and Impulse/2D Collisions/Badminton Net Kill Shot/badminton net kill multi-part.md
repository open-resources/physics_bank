---
title: Badminton Net Kill Shot
topic: Momentum and Impulse
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.3
- 7.6.1.0
- 7.6.1.2
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
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\alpha= $
    suffix: $^{\circ}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{racket}= $
    suffix: $\rm{ms^{-1}}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $e= $
    suffix: $N/A$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_u_s: 7.5
    params_h: 2.9
    params_v_s: 4.33
    params_theta: 6.6
---
# Badminton Net Kill Shot
In a game of badminton, to counter a weak lift shot, the receiver can orient their racket at certain angle relative to the vertical. Thus, he/she is able to utilize the incoming momentum of the shuttle and principles of oblique impacts to return the shuttle at a steep angle without exerting an additional impulse. This agile shot is termed as a badminton net kill shot due to its play in close proximity to the net.

<img src="part1.png" width=600>

## Part 1

Treat the racquet and shuttle as particles with masses $0.5\ \rm{kg}$, $0.1\ \rm{kg}$ respectively in a vertical plane. Assume the racquet is stationary before the collision. Neglect aerodynamic drag and effects of gravity at the point of collision.
<br>
<br>
Calculate the angle($\alpha$) with which the racquet has to be oriented relative to the collision to achieve the desired trajectory as shown below.
<br>
$\theta = {{ params_theta }}^{\circ}$, $u\_{shuttle} = {{ params.u_s }}\ \rm{ms^{-1}}$ , $v\_{shuttle} = {{ params.v_s }}\ \rm{ms^{-1}}$, $h = {{ params_h }}\ \rm{m}$, $h\_{net} = 1.524\ \rm{m}$, $x = 1.626\ \rm{m}$
<br>
<i>You may have to use the compound angle identity:</i> $sin⁡(A \pm B) = sin(⁡A)cos(B) \pm cos(⁡A)sin(⁡B)$

### Answer Section

Please enter in a numeric value in $\circ$.

## Part 2

Determine the the magnitude of the final velocity of the racket. Treat the badminton racket as a rigid body.

### Answer Section

Please enter the value of $v\_{racket}$ in $ms^{-1}$.

## Part 3

Determine the coefficient of restitution($e$) between the racket and the shuttle.

### Answer Section

Please enter the value of $e$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)