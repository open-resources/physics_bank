---
title: Understanding Angular Momentum
topic: Momentum and Impulse
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.3.0
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
- TA
- APSC181
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\lvert H \rvert= $
    suffix: $\rm{kg m^2/s}$
myst:
  substitutions:
    params_vars_title: Understanding Angular Momentum
    params_vars_units: kg.m^2/s
    params_m: 0.56
    params_x: 1.25
    params_theta: 49
    params_v: 6.67
    params_t: 3.4
    params_H0: 3.52
    params_H1: 45.47
    params_H2: 41.95
    params_x2: 16.13
    params_y2: 17.12
---
# {{ params_vars_title }}
There is a particle with mass ${{params_m}} \rm{kg}$ hat is travelling with a speed of ${{params_v}} \rm{m/s}$ in the direction $\theta = {{params_theta}}^\circ$ with the x-axis. It starts out at $({{params_x}},0)$.

## Part 1

Calculate the magnitude of the angular momentum of this particle after ${{params_t}}$ seconds.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

### pl-answer-panel

<br>You might have noticed that the angular momentum after ${{params_t}}$ seconds is the same as the angular momentum at $t = 0$ seconds. This is because of the principle of Conservation of Momentum. There was no external moment affecting the particle hence we have Conservation of Momentum.<br><br>

It can be seen if we actually go ahead and find the coordinates after ${{params_t}}$ and calculate the angular momentum that way. $x = x_0 + v\*cos(\theta)*t$ where we find that $x = {{params_x2}}$ and similarly $y =  v*sin(\theta)\*t$ where $y = {{params_y2}}$ m. Now let us find the angular momentum with our new numbers. $\vec{H} = x.\widehat{\mathbf{i}}\times m.v.sin(\theta)\widehat{\mathbf{j}} +  y.\widehat{\mathbf{j}}\times m.v.cos(\theta)\widehat{\mathbf{i}}\Rightarrow \vec{H} = {{params_H1}}.\widehat{\mathbf{k}}-{{params_H2}}.\widehat{\mathbf{k}}$  which is equal to ${{params_H0}}$ {{ params_vars_units }}. <br><br>This is the same as if we did $\vec{H} = {{params_x}}.\widehat{\mathbf{i}}\times m.v.sin(\theta)\widehat{\mathbf{j}}$ where we also get ${{params_H0}}$ {{ params_vars_units }}. <br><br>This demonstrates that nature will always tend to conserve momentum as long as there are no external forces or moments.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)