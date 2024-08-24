---
title: Travelling wave derivation
topic: Waves
author: John Hopkinson
source: PHYS 112 2022S T8 Q2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 16.1.1.3
difficulty:
- medium
randomization:
- undefined
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- HZ
assets:
- sample.html
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part2:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
myst:
  substitutions:
    params:
      vars:
        title: Travelling wave derivation
      part1:
        ans1:
          value: Line 1
          feedback: Great! You got it.
        ans2:
          value: Line 2
          feedback: This is just factoring of $\omega$ inside the function so it is
            okay.
        ans3:
          value: Line 3
          feedback: To follow one displacement of the travelling wave as a function
            of time and position you hold the phase constant, so it is valid to set
            the derivative of the phase with respect to time equal to zero to find
            the speed the wave moves at.
        ans4:
          value: Line 4
          feedback: Both the mass and angular frequency do not depend on time for
            the wave, so this derivative has been properly taken and is consistent.
        ans5:
          value: Line 5
          feedback: Rearranging Equation (4) does give $\frac{dx}{dt} = \frac{1}{m\omega}$,
            which would be positive and represent the speed.
---
# {{ params.vars.title }}
A student wants to understand how fast a travelling wave described by $D(x, t) = A\sin(kx - \omega t)$ is moving and carries out the following derivation.

$(1) \quad k = m\omega^{2} \textrm{ so }  D(x,t) = A\sin(m\omega^{2}x - \omega t)$

$(2) \quad D(x,t) = A\sin(\omega(m\omega x - t)) = D\sin\phi$

$(3) \quad 0 = \frac{d\phi}{dt}$

$(4) \quad 0= m\omega \frac{dx}{dt} - \frac{dt}{dt}$

$(5) \quad v = \frac{1}{m\omega}$

## Part 1

Something seems to have gone wrong since their final answer for the speed does not have the correct units. Check any box of line that is incorrect or inconsistent with the previous step. Leave the boxes of lines that are correct empty.

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}
- {{ params.part1.ans3.value}}
- {{ params.part1.ans4.value}}
- {{ params.part1.ans5.value}}

## Part 2

Explain the error in any line you have selected as being incorrect.

### Answer Section

Answer in 1-2 sentences and try to use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)