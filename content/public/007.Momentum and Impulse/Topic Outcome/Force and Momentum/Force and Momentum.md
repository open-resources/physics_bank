---
title: Force and Momentum
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Final Q8
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.5.1.1
- 6.5.1.2
- 7.2.1.1
- 7.2.1.4
- 7.2.1.5
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- average
tags:
- PW
- final_exam
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Force and Momentum
      units: N
    p_i: -3t^2 + 3t
    p_j: 2t^2 - 2t
    time: 12.1
    part1:
      ans1:
        value: 0
      ans2:
        value: (-69.6$\hat\imath$ + 46.4$\hat\jmath$)
      ans3:
        value: (69.6$\hat\imath$ - 46.4$\hat\jmath$)
      ans4:
        value: (-69.6$\hat\imath$ - 46.4$\hat\jmath$)
      ans5:
        value: (69.6$\hat\imath$ + 46.4$\hat\jmath$)
      ans6:
        value: (139.2$\hat\imath$ + 46.4$\hat\jmath$)
---
# {{ params.vars.title }}
The momentum of an object as a function of time is given by $\vec{p} = (${{ params.p_i }}$)\hat{\imath} + (${{ params.p_j }}$)\hat{\jmath}$ where $p$ is in $kg\cdot m/s$ and $t$ is in seconds.

## Part 1

What is the net force on the object at $t=$ {{ params.time }} $s$?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)