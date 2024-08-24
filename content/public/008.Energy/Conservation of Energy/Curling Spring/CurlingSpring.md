---
title: Curling Rock Hits a Spring
topic: Energy
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- null
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
- RG
- JR
- APSC181
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W = $
    suffix: \rm{J}
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: \rm{m/s}
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      vars:
        title: Curling Rock Hits a Spring
        units: J
      m: 19.1
      d: 2
      mu: 0.1
      k: 357
---
# {{ params.vars.title }}
A curler is practicing for the national curling championships to get the perfect momentum and strength on the push of a curling rock. The rock has a mass of $m = {{ params.m }} \ \rm{kg}$ and hits a spring target at the end. Find the work done by the spring, and the speed of the rock when it reached the spring, if the spring constant is $k = {{ params.k }} \ \rm{N/m}$ and the spring compresses $d = {{ params.d }} \ \rm{cm}$. The coefficient of friction on rough ice sheet is $\mu = {{ params.mu }}$.

## Part 1

What is the work done by the spring?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

With what velocity does the rock impact the spring?

### Answer Section

Please enter in a numeric value in $\ \rm{m/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)