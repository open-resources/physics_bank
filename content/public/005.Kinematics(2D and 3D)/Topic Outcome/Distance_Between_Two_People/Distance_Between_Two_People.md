---
title: Distance Between Two People
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2014 Final Q10
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.2.1.0
- 4.4.1.0
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- EW
- NR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Distance Between Two People
    params_vars_units: $\rm{m}$
    params_vars_name1: Lorenzo
    params_vars_name2: Emilia
    params_s: 3
    params_ai_1: 2
    params_ai_2: 3
    params_ai_3: 2
    params_aj_1: 1
    params_aj_2: 2
    params_aj_3: 3
    params_bi_1: 2
    params_bi_2: 4
    params_bi_3: 3
    params_bj_1: 5
    params_bj_2: 3
    params_bj_3: 2
    params_part1_ans1_value: 52.0
    params_part1_ans2_value: 26.0
    params_part1_ans3_value: 2700.0
    params_part1_ans4_value: 46
    params_part1_ans5_value: 58
---
# {{ params_vars_title }}
The position of {{ params_vars_name1 }} as a function of time is given by:

$\vec{r_A} =$ ({{ params.ai_1 }}$+${{ params.ai_2 }}$t-${{ params.ai_3 }}$t^2)\hat{\imath} + (${{ params.aj_1 }}$+${{ params.aj_2 }}$t-${{ params.aj_3 }}$t^2)\hat{\jmath}$

{{ params_vars_name2 }}'s position is given by:

$\vec{r_B} =$ ({{ params.bi_1 }}$+${{ params.bi_2 }}$t-${{ params.bi_3 }}$t^2)\hat{\imath} + (${{ params.bj_1 }}$+${{ params.bj_2 }}$t+${{ params.bj_3 }}$t^2)\hat{\jmath}$.

The positions $\vec{r_A}$ and $\vec{r_B}$ are in meters and $t$ is in seconds.

## Part 1

What is the distance between {{ params_vars_name1 }} and {{ params_vars_name2 }} when $t$ = {{ params_s }}?

### Answer Section

- {{ params_part1_ans1_value }} {{ params_vars_units}}
- {{ params_part1_ans2_value }} {{ params_vars_units}}
- {{ params_part1_ans3_value }} {{ params_vars_units}}
- {{ params_part1_ans4_value }} {{ params_vars_units}}
- {{ params_part1_ans5_value }} {{ params_vars_units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)