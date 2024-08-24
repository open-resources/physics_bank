---
title: Lengths with Same Period
topic: Oscillations
author: John Hopkinson
source: Phys122 2018W2 Test 1 Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 15.4.1.1
- 15.4.1.2
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
- unknown
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Oscillations
      part1:
        ans1:
          value: $R > l > L$
          feedback: Hmm, maybe go back and double-check your algebra.
        ans2:
          value: $l > R > L$
          feedback: Hmm, not quite. Did you try relating the period and $I$?
        ans3:
          value: $L > l > R$
          feedback: Great! You got it.
        ans4:
          value: $L = l = R$
          feedback: Hmm, they all oscillate with the same period, yet the lengths
            all have a different relation to $I$. How are the period and $I$ related?
        ans5:
          value: that we cannot know the relative lengths without knowing the masses
            of the objects
          feedback: We have the moment of inertia for each object... maybe that could
            help.
---
# {{ params.vars.title }}
A thin rod of length $L$ oscillating about its end ($I = \frac13 mL^2$), a hoop of radius $R$ oscillating about its edge ($I=2mR^2$) and a simple pendulum of length $l$ ($I = ml^2$) are all found to have the same period.

## Part 1

This means:

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)