---
title: Flying Squid
topic: Momentum and Impulse
author: Jake Bobowksi
source: 2013 Midterm 2 002 Q6
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.5.1.4
- 4.1.1.1
- 4.3.1.1
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
assets:
- Q6.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta y= $
    suffix: $m$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Flying Squid
      units1: m/s
      units2: m
    m1: 0.11
    m2: 0.95
    v: 19
---
# {{ params.vars.title }}
The Japanese flying squid, shown in the photograph below, is able to "jump" off the surface of the sea by taking water into its body cavity and then ejecting the water vertically downward. A squid is able to eject {{params.m1}} $kg$ of water with a speed of {{params.v}} $m/s$. Without any water in its cavity, the mass of the squid is {{params.m2}} $kg$.

<img src="Q6.png" width=300 alt = "Japanese flying squid">

## Part 1

If starting from rest at the surface of the sea, what will be the speed of the squid immediately after ejecting the water?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 3

How high above the surface of the sea will the squid rise?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)