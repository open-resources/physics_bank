---
title: Power Waves Q1
topic: Waves
author: John Hopkinson
source: Phys122 2018W Final Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 16.5.1.0
- 16.5.1.1
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
- HZ
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Power Waves Q1
      units: $\rm{m}
      r_sun_europa: 7.8
      r_sun_earth: 1.5
      part1:
        ans1:
          value: '5.00'
          feedback: This is a random number, you probably selected this choice by
            mistake! Try again please!
        ans2:
          value: 27.0
          feedback: Great! You got it.
        ans3:
          value: 5.2
          feedback: Hmm, it seems like you forgot to square the radii!
        ans4:
          value: 0.037
          feedback: Hmm, it seems like you got the radii switched! Remember that you
            need to compare the intensity of solar radiation reaching the Earth $I_{Earth}$
            to the solar radiation reaching Europa $I_{Europa}$, not the other way
            around
        ans5:
          value: 0.19
          feedback: Hmm, it seems like you got the radii switched and forgot to square
            them! Remember that you need to compare the intensity of solar radiation
            reaching the Earth $I_{Earth}$ to the solar radiation reaching Europa
            $I_{Europa}$, not the other way around.
---
# {{ params.vars.title }}
One of the moons of Jupiter, Europa, has shown evidence of water plumes coming from its surface. Europa is $ {{ params.r_sun_europa }} \times 10^{11}$ $\rm{m}$ from the sun, while Earth is $ {{ params.r_sun_earth }} \times 10^{11}$ $\rm{m}$ from the sun.

## Part 1

Compare the intensity of solar radiation reaching the Earth $I\_{Earth}$ to the solar radiation reaching Europa $I\_{Europa}$.

$\frac{I\_{Earth}}{I\_{Europa}} =$

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)