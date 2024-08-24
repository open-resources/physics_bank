---
title: Current-Carrying Wire
topic: Magnetism
author: John Hopkinson
source: Physics 122 2019 W2 Final Q15
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.1.4
- 19.2.4.0
- 19.2.4.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- L.K
assets:
- magneticswing.png
part1:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $B= $
    suffix: T
myst:
  substitutions:
    params:
      vars:
        title: Current-Carrying Wire Swing
      a: 2
      length: 14
      mass: 14
---
# {{ params.vars.title }}
A current-carrying wire was deflected by a magnetic field as shown in the figure below. The direction of the current at the bottom of the wire is into the screen (as shown by the $\textbf{X}$).

<img src="magneticswing.png" height =300px>

## Part 1

What is the direction of the magnetic field between the plates of the magnet?
Explain how you arrived at your answer specifying what direction fingers pointed and what they represented as you applied the right hand rule.

### Answer Section

## Part 2

If the current-carrying wire makes an angle $10^{\circ}$ relative to the vertical when the current through the wire is ${{ params.a}} \textrm{A}$ , solve for the strength of the magnetic field between the plates.
The length of the bottom of of the current-carrying wire is ${{ params.length}}\textrm{ cm}$, and the swing has a mass of ${{ params.mass}}\textrm{ g}$.
Use a free body diagram to write two equations and solve them for the magnetic field strength.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)