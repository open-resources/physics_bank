---
title: Test Uranium Fragments
topic: Momentum and Impulse
author: Jake Bobowski
source: 2017 Midterm 1 (002) Q6
template_version: 1.1
attribution: standard
outcomes:
- 7.2.1.1
- 7.5.1.4
- 7.5.1.9
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
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: amu
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: amu
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Test Uranium Fragments
      units: amu
    frag_speed: 1.8
    dn_speed: 3.37
    orig_mass: $^{232}\mathrm{U}$
---
# {{ params.vars.title }}
A radioactive {{params.orig_mass}} uranium nucleus is initially at rest.
It spontaneously disintegrates into a small fragment that is ejected with a measured speed of {{params.frag_speed}}$ \times 10^7 \ m/s$ and a daughter nucleus that recoils with a measured speed of {{params.dn_speed}}$ \times 10^5 \ m/s$.
The mass of the original uranium nucleus is {{params.orig_mass}} amu (atomic mass units).

## Part 1

What is the mass of the ejected fragment?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the mass of the daughter nucleus?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)