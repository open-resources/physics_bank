---
title: Collision of Objects A and B
topic: Momentum and Impulse
author: Jake Bobowski
source: 2017 Final Q17
template_version: 1.1
attribution: standard
outcomes:
- 7.4.1.0
- 7.4.1.1
- 7.4.1.2
- 8.2.1.0
- 8.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets: null
part1:
  type: symbolic-input
  pl-customizations:
    label: $v_a = $
    variables: v, j_hat, i_hat
    weight: 1
    allow-blank: false
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
part3:
  type: symbolic-input
  pl-customizations:
    label: $K = $
    variables: v
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $K = $
    variables: v
    weight: 1
    allow-blank: false
myst:
  substitutions:
    params_vars_title: Collision of Objects A and B
    params_vars_name: Mateo
    params_v1: 5
    params_v2: 3
    params_m_a: 6
    params_m_b: 4
    params_part2_ans1_value: 'Yes'
    params_part2_ans2_value: 'No'
---
# {{ params_vars_title }}
{{ params_vars_name }} observes object A, which has mass ${{params.m_a}}$ and velocity $v_0 \vec{i}$, collide with object B, which has mass {{params.m_b}} $kg$ and a velocity  1/{{params_v1}} $v_0 \vec{j}$.
Following the collision, object B has a velocity of 1/{{params_v2}} $$v_0 \vec{i}$$.

Use the following table as a reference for each variable:

| $Variable$ | Use   |
|----------|-------|
| $v_0$  | v  |
| $\hat{i}$ | i_hat |
| $\hat{j}$ | j_hat |

## Part 1

Determine the velocity of object A after the collision.

### Answer Section

Please enter in a value in {{ params.vars.units }}.

## Part 2

Is this collision elastic?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

## Part 3

Express the change in the kinetic energy in terms of $v_0$ (use v for $v_0$ ).

### Answer Section

## Part 4

Suppose a second person observes the same collision.
This second observer, however, is moving with a velocity of $$v\_{2nd} = v_0 \vec{i} - v_0 \vec{j}$$ m/s relative to {{ params_vars_name }}.
What is the change in kinetic energy that this second observer measures?

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)