---
title: Bird Flying Speed
topic: Math
author: Reza Khanbabaie
source: PHYS 112 Describing Motion Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.1.1.0
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
- PW
assets:
- sample.html
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{eagle} = $
    suffix: $km/h$
part2:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
substitutions:
  params:
    vars:
      title: Bird Flying Speed
      units: $km/h$
    m_1: 5
    v_1: 75
    m_2: 3
---
# {{ params.vars.title }}
To predict the flying speed of an eagle, we can use the relationship between the flying speed ($v$) and the mass ($m$) of birds. It has been reported that in steady flight, the flying speed of birds is related to their mass as $v \propto m^{-1/4}$.

## Part 1

If a {{ params.m_1 }} $kg$ eagle flies at a speed of {{ params.v_1 }} $km/h$, how fast do you expect a {{ params.m_2 }} $kg$ eagle to fly?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Is your answer reasonable? Why?

### Answer Section

Answer in 1-2 sentences, and try to use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)