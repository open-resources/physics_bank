---
title: Slider in a Rotating Tube
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 15, Q2
template_version: 1.2
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.8
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC181
- Lecture Activities
- JR
assets:
- Slider in a rotating Tube.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T = $
    suffix: N
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{\theta} = $
    suffix: N
substitutions:
  params:
    vars:
      title: Slider in a Rotating Tube
    m: 0.19
    w: 4
    wdot: -8
    r: 0.62
    rdot: -2.0
    rddot: 3.3
---
# {{ params.vars.title }}
<img src="Slider in a rotating Tube.png" alt="A vertical hollow tube rotating about its vertical axis at omega rad per second is connected to a horizontal hollow tube in which a slider P moves under control of a string. The distance from the slider to the point of connection is R. The tension in the string acts downwards." width=200>

The hollow tube above rotates about its vertical axis at $\omega=\dot{\theta}={{ params.w }}rad/s$ and $\dot{\omega}=\ddot{\theta}={{ params.wdot }}rad/s^2$. A small ${{ params.m }}kg$ slider P moves inside the horizontal portion under the control of a string which is being pulled out the bottom of the tube. If $r= {{ params.r}}m$, $\dot{r}= {{ params.rdot }}m/s$,and $\ddot{r}={{params.rddot}}m/s^2$, Determine the tension $T$ in the string and the magnitude of the horizontal force $F\_{\theta}$ exerted on the tube by the slider.

## Part 1

### Answer Section

Please enter in a numeric value in Netwons.

## Part 2

### Answer Section

Please enter in a numeric value in Newtons.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)