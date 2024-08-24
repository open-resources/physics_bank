---
title: Direction of Dipole Rotation
topic: Electrostatics
author: John Hopkinson
source: Physics 122 2019 GPSVIII_Part2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.6.1.1
- 18.7.1.2
- 18.2.1.1
difficulty:
- undefined
randomization:
- 0
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets:
- HF.png
- dipoles.png
part1:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
part2:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part3:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
myst:
  substitutions:
    params:
      vars:
        title: Direction of Dipole Rotation
      part2:
        ans1:
          value: The Hydrogen atom now experiences a weaker Electric Field
        ans2:
          value: The Hydrogen atom now experiences a stronger Electric Field
        ans3:
          value: The dipole experiences a net force towards the sphere
        ans4:
          value: The dipole experiences a net force away from the sphere
        ans5:
          value: The dipole will not experience a net torque as r and F are parallel
        ans6:
          value: The dipole will experience a net torque as r and F are parallel
      part3:
        ans1:
          value: There will be a small downward contribution to the net force
        ans2:
          value: There will be a small upward contribution to the net force
        ans3:
          value: The molecule experiences a net torque tending to rotate the dipole
            so that the F atom is closer to charged sphere
        ans4:
          value: The molecule experiences a net torque tending to rotate the dipole
            so that the F atom is further away from charged sphere
        ans5:
          value: Both forces have the same magnitude but not quite opposite directions
        ans6:
          value: Both forces have the same magnitude and opposite directions
---
# {{ params.vars.title }}
Hydrogen fluoride is a polar molecule with a bond length of about 0.92 x 10-10 m and can be roughly modeled as having a point charge of 6.6 x 10-20 C on the hydrogen atom and another of -6.6 x 10-20 C on the fluorine atom.

<img src="dipoles.png" width="400">

## Part 1

What will the HF molecule tend to do if placed in this geometry?

### Answer Section

Answer in 3-4 sentences, try and use full sentences.

## Part 2

A metal sphere is positively charged and has electric field lines as drawn.

<img src="HF.png" width="400">

If the hydrogen fluoride molecule is placed with its axis along one of the field lines (above the sphere), which of the following statements are true?

### Answer Section

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}
- {{ params.part2.ans4.value}}
- {{ params.part2.ans5.value}}
- {{ params.part2.ans6.value}}

## Part 3

If the hydrogen fluoride molecule is placed with its axis perpendicular to the electric field lines, which of the following statements are correct?

### Answer Section

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}
- {{ params.part3.ans3.value}}
- {{ params.part3.ans4.value}}
- {{ params.part3.ans5.value}}
- {{ params.part3.ans6.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)