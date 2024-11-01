---
title: Rock on a String
topic: Rotational Dynamics
author: Jake Bobowski
source: 2012 Midterm 2 Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.2
- 10.1.1.1
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- MP
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Rock on a String
        units: m/s
      m: 1.25
      r: 41
      T: 300
      part1:
        ans1:
          value: 10.0
        ans2:
          value: 0.0
        ans3:
          value: 17.0
        ans4:
          value: -10.0
        ans5:
          value: 30.0
---
# {{ params.vars.title }}
A child ties a {{params.m}} kg rock to the end of a string and whirls it at a constant speed in a horizontal circle of radius {{params.r}} cm.

## Part 1

What, approximately, is the maximum speed at which the rock may be whirled if the string will break when the tension exceeds {{params.T}} N?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)