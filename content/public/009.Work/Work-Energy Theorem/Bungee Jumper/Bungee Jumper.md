---
title: Bungee Jumper
topic: Work
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.3.1.2
- 6.5.1.1
- 9.2.1.0
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
    label: $y_{max}= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k_{max}= $
    suffix: $ \rm{N/m}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_m: 84
    params_k: 16
    params_l: 110
    params_h1: 380.0
---
# Bungee Jumper
A bungee jumper comprises of a person attached to a rubber cord who then releases himself off a cliff at a high altitude above sea level as shown in the image below.

<img src="part1.png" width=600>

## Part 1

Treating the rubber cord as the equivalent of a linear spring with original un-stretched length $L = {{ params_l }} \ \rm{m}$ and spring stiffness constant $k = {{ params_k }}\ \rm{N/m}$, and neglecting any forces in the cord whilst it is slackened, determine the maximum vertical displacement from the cliff.<br>
Treat the person as a particle with mass $m$, and neglect the mass of the cord and any resistive forces.<br>
$m = {{ params_m }} \ \rm{kg}$, $h_1= {{ params_h1 }}\ \rm{m}$

### Answer Section

Please enter in a numeric value in $m$.

## Part 2

If the maximum possible upward acceleration that can safely be applied to a person is $2g$, what is the maximum value of the spring stiffness constant for this rope of initial length $L$?

### Answer Section

Please enter in a numeric value in $N/m$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)