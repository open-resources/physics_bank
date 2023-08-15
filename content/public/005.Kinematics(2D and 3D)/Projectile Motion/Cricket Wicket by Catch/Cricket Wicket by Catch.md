---
title: Cricket Wicket by Catch
topic: Kinematics(2D and 3D)
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.4.1.1
- 5.5.1.0
- 5.5.1.1
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
    label: $$ \dot{R} = $$
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $$ \dot{\phi} = $$
    suffix: $\rm{rad/s}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $ \dot{\theta} = $
    suffix: $\rm{rad/s}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $$ \ddot{R} = $$
    suffix: $m/s^{2}$
    comparison: sigfig
    digits: 2
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $$ \ddot{\theta} = $$
    suffix: $\rm{rad/s^{2}}$
    comparison: sigfig
    digits: 2
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $$ \ddot{\phi} = $$
    suffix: $\rm{rad/s^{2}}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_a: 53
    params_u: 17
    params_d: 50
    params_a_w: 5
---
# Cricket Wicket By Catch
In a game of cricket akin to baseball, a batsman returns the ball bowled on a pitch and scores runs based on the distance travelled by the ball upon exiting the collision with the bat.

## Part 1

If the ball leaves the bat with a speed of $u\ \rm{m/s}$ at an angle $\alpha$ measured up from the horizontal as shown in the image below, determine the value of $$ \dot{R} $$ in $\rm{m/s}$ as observed by a stationary spectator.

<img src="part1.png" width=800>

Treat the ball as a particle and assume an east-ward acceleration awind acting on the ball due to the wind.<br>
$\alpha = {{ params_a }}^\circ$, $u = {{ params_u }}\ \rm{m/s}$, $d = {{ params_d }}\ \rm{m}$, $a\_{wind} = {{ params_a_w }}\ \rm{m/s^{2}}$.

### Answer Section

Please enter in a numeric value in m/s.

## Part 2

Determine the value of $$ \dot{\phi} $$.

### Answer Section

Please enter in a numeric value in rad/s.

## Part 3

Determine the value of $$ \dot{\theta} $$.

### Answer Section

Please enter in a numeric value in rad/s.

## Part 4

Determine the value of $$ \ddot{R} $$.

### Answer Section

Please enter in a numeric value in $ms^{-2}$.

## Part 5

Determine the value of $$ \ddot{\theta} $$.

### Answer Section

Please enter in a numeric value in $rads^{-2}$.

## Part 6

Determine the value of $$ \ddot{\phi} $$.

### Answer Section

Please enter in a numeric value in $rads^{-2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)