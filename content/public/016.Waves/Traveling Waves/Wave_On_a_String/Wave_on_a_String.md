---
title: Traveling Wave on a String
topic: Waves
author: John Hopkinson
source: Physics 2019W2 First-Test Q1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 16.1.1.3
- 16.1.1.6
- 16.1.1.7
difficulty:
- intermediate
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Traveling Wave on a String
      b: 2
      c: 25
      d: 10
      wave_equation: D(x,t) = 2.00 cm * cos(25.0 rad/s * t - 10.0 rad/m * x + π rad)
      part1:
        ans1:
          value: '|Vᵧₘₐₓ| = 42,   |Vₓ|= 24'
          feedback: This is a random number, you probably selected this choice by
            mistake! Try again
        ans2:
          value: '|Vᵧₘₐₓ| = 0.5,   |Vₓ| = 2.5'
          feedback: Correct!
        ans3:
          value: '|Vᵧₘₐₓ| = 50.0,   |Vₓ|= 2.5'
          feedback: Check your units!
        ans4:
          value: '|Vᵧₘₐₓ| = 0.24,   |Vₓ|= 2.4'
          feedback: There is mix in your chosen calculation values
        ans5:
          value: '|Vᵧₘₐₓ| = 0.5,   |Vₓ|= 0.08'
          feedback: Check the your Vₓ value
        ans6:
          value: '|Vᵧₘₐₓ| = 0.02,   |Vₓ|= 2.0'
          feedback: Try again!
---
# {{ params.vars.title }}
A traveling wave on a string satisfies
{{ params.wave_equation }}

## Part 1

Find the maximum speed that any part of this string moves at, ($|v\_{y,max}|$), and the speed that energy moves down this string at, ($|v_x|$).

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)