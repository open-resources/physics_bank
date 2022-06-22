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
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- MP
assets:
- Q6.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta y= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Flying Squid
      units1: m/s
      units2: m
    m1: 0.3
    m2: 0.83
    v: 11
---
# {{ params.vars.title }}
The Japanese flying squid, shown in the photograph below, is able to "jump" off the surface of the sea by taking water into its body cavity and then ejecting the water downward. A Japanese flying squid is able to eject ${{params.m1}} kg$ of water with a speed of ${{params.v}} m/s$.

<img src="Q6.png" width=300 alt = "Japanese flying squid">

## Part 1

If a Japanese flying squid that has a mass of ${{params.m2}} kg$ without water in its cavity "jumps" from rest off of the surface of the sea, what will its speed be immediately after ejecting the water?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

What maximum height above the surface of the sea will the same Japanese flying squid reach?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)