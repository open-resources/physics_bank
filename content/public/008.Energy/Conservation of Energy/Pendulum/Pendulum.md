---
title: Pendulum
topic: Energy
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.12.1.1
- 8.2.1.1
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
- RG
- PJ
assets:
- Pendulum.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_A= $
    suffix: $ \rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_T= $
    suffix: $ \rm{N}$
myst:
  substitutions:
    params:
      vars:
        title: Pendulum
        units:
          part1: "$\rm{m/s}$"
          part2: "$\rm{N}$"
      m: 49
      l: 3
      theta: 30
      mainText: A gymnast with mass $49 \ \rm{kg}$ steps off a horizontal platform
        to swing on a trapeze with length $3 \ \rm{m}$. At point $A$, the angle formed
        is $30^\circ$.
      part1Text: Find the speed of the gymnast at point $A$
      part2Text: Find the total tension holding the trapeze at point $A$
---
# {{ params.vars.title }}
{{params.mainText}}

<img src="Pendulum.png" width=700 alt="A pendulum made of a ball of mass m on a string of length L. The pendulum starts at horizontal and goes to angle theta." >

## Part 1

{{params.part1Text}}

### Answer Section

Please enter in a numeric value in {{ params.vars.units.part1 }}.

## Part 2

{{params.part2Text}}

### Answer Section

Please enter in a numeric value in {{ params.vars.units.part2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)