---
title: Tug of War
topic: Force
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
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
- PJ
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Tug of War
      numberOfChildren: 4
      adultWeight: 217
      adultForce: 305
      childWeights: ' $63\ \rm{lb}$, $70\ \rm{lb}$, $56\ \rm{lb}$, $58\ \rm{lb}$'
      childForces: ' $104\ \rm{N}$, $124\ \rm{N}$, $141\ \rm{N}$, $99\ \rm{N}$'
---
# {{ params.vars.title }}
In a game of tug of war, two teams pull on opposite sides of a rope to tug the opposing team towards them.
One team is made of {{params.numberOfChildren}} children.
Their weights are {{params.childWeights}}, and they pull with forces of {{params.childForces}}.
On the other side, a ${{params.adultWeight}} \ \rm{lb}$ adult pulls the rope with a force of ${{params.adultForce}} \ \rm{N}$.

## Part 1

What is the acceleration of the rope with the people?
Give a positive answer if it moves towards the adult, and negative if it moves towards the children.

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)