---
title: Exponential Damping 1
topic: Oscillations
author: John Hopkinson
source: PHYS112 T2 Q1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
outcomes:
- 15.5.1.1
- 15.5.1.0
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
- MP
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\tau = $
    suffix: s
substitutions:
  params:
    vars:
      title: Exponential Damping 1
      units: s
    m: 1
    b: 2
    k: 5
---
# {{ params.vars.title }}
A ${{params.m}}$ kg mass oscillates on a ${{params.k}}$ N/m spring. The damping constant of this spring is $b$ = ${{params.b}}$ kg/s.

## Useful Info

For slowly moving objects we've seen that the drag force grows in proportion to the velocity, $\overrightarrow{D} = -b\overrightarrow{v}$, where $b$ is the damping constant and $\overrightarrow{v}$ is the velocity of the object.

The net force acting on a slowly moving mass attached to a massless spring in the presence of a drag force (for motion along $x$ relative to an equilibrium point $x_0$) can be written as:

\begin{equation}
F\_{net,x} = -b\frac{dx}{dt} - kx=ma = m\frac{d^2x}{dt^2}.
\end{equation}
The solution of this differential equation is found to be \begin{equation}
x(t) = Ae^{-\frac{bt}{2m}} \cos(\omega t) = Ae^{-\frac{t}{2\tau}} \cos(\omega t)= A(t) \cos(\omega t),
\end{equation} where $A$ is the initial amplitude of the oscillation, $\tau$ is the time constant, $A(t)$ is the time-dependent amplitude of the oscillation, and $\omega = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}}$ is the angular frequency of the damped oscillation.

## Part 1

Find the time constant, $\tau$, of this spring.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)