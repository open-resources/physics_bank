---
title: Displacement and Potential Energy of an Oscillator
topic: Oscillations
author: Jake Bobowski
source: 2013 Practice Final Q2
template_version: 1.1
attribution: standard
outcomes:
- 15.2.2.0
- 15.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: symbolic-input
  pl-customizations:
    variables: A,T
    label: $x = \pm $
    weight: 1
    allow-blank: false
substitutions:
  params:
    vars:
      title: Displacement and Potential Energy of an Oscillator
    choice: half
---
# {{ params.vars.title }}
## Question Text

A simple harmonic oscillator has a displacement as a function of time given by $x(t) = A\cos(\frac{2\pi t}{T})$. When {{ params.choice }} of the oscillator's energy is potential energy, what is its displacement from equilibrium?

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| $Variable$ | Use   |
|----------|-------|
| $A$  | A  |
| $T$  | T  |

### Answer Section

{{ substitutions.part1.label }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)