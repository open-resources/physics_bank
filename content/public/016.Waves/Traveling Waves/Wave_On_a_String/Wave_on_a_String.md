---
title: Traveling Wave on a String
topic: Waves
author: John Hopkinson
source: Physics 2019W2 Mid-term 1 Q1
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
    params_vars_title: Traveling Wave on a String
    params_b: 6
    params_c: 17
    params_d: 9
    params_wave_equation: cos
    params_part1_ans1_value: '|Vᵧₘₐₓ| = 42,   |Vₓ|= 24'
    params_part1_ans1_feedback: This is a random number, you probably selected this
      choice by mistake! Try again
    params_part1_ans2_value: '|Vᵧₘₐₓ| = 1.02,   |Vₓ| = 1.89'
    params_part1_ans2_feedback: Correct!
    params_part1_ans3_value: '|Vᵧₘₐₓ| = 102.0,   |Vₓ|= 1.89'
    params_part1_ans3_feedback: Check your units!
    params_part1_ans4_value: '|Vᵧₘₐₓ| = 1.06,   |Vₓ|= 2.4'
    params_part1_ans4_feedback: There is mix in your chosen calculation values
    params_part1_ans5_value: '|Vᵧₘₐₓ| = 1.02,   |Vₓ|= 0.353'
    params_part1_ans5_feedback: Check the your Vₓ value
    params_part1_ans6_value: '|Vᵧₘₐₓ| = 0.06,   |Vₓ|= 2.65'
    params_part1_ans6_feedback: Try again!
---
# {{ params_vars_title }}
A traveling wave on a string satisfies
$D(x,t) = {{ params_b }}\text{ cm}\ {{ params.wave_equation}}({{ params_c }}\text{ rad/s } t - {{ params_d }} \text{ rad/m } x + \pi \text{ rad })$.

## Part 1

Find the maximum speed that any part of this string moves at, ($|v\_{y,max}|$), and the speed that energy moves down this string at, ($|v_x|$).

### Answer Section

- {{ params_part1_ans1_value }} {{ params.vars.units}}
- {{ params_part1_ans2_value }} {{ params.vars.units}}
- {{ params_part1_ans3_value }} {{ params.vars.units}}
- {{ params_part1_ans4_value }} {{ params.vars.units}}
- {{ params_part1_ans5_value }} {{ params.vars.units}}
- {{ params_part1_ans6_value }} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)