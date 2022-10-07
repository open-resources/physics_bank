---
title: Brick and spring on a conveyor
topic: Force
author: Jake Bobowski
source: Final 2016 Q2  P2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 11.5.1.1
- 6.7.1.0
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
- AK
- NR
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: freebody.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a=$
    suffix: $\rm{m/s^2}$
part3:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer3.html
    quill-theme: snow
    directory: clientFilesQuestion
part4:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer4.html
    quill-theme: snow
    directory: clientFilesQuestion
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta x=$
    suffix: $\rm{m}$
substitutions:
  params:
    vars:
      title: Brick and spring on a conveyor
      part2:
        units: $m/s^2$
      part5:
        units: m
    b: 4
    spring: 3
    k: 6.2
    u_k: 0.16
    u_s: 0.69
---
# {{ params.vars.title }}
I decide to set up a very elaborate physics apparatus consisting of a {{ params.b}} kg brick, which is attached to the wall with a spring, placed on a conveyor belt. The end of the spring starts out {{params.spring}} m from the wall, and its rest length is {{params.spring}} m. The spring constant of the spring is k = {{params.k}} $N \over m$. The coefficient of kinetic (sliding) friction is $\mu_k$ = {{params.u_k}}, and the coefficient of static friction is $\mu_s$ = {{params.u_s}}.

## Part 1

I turn the conveyor belt on to accelerate the brick gently forwards in such a way that the brick stays IN PLACE upon the belt. Draw a free body diagram for the situation. When uploading your diagram, make sure that it is a pdf, titled, "freebody.pdf".

### Answer Section

File upload box will be shown here.

## Part 2

What is the maximum possible acceleration the belt can have for the brick to stay in place upon it WHEN THE BRICK IS {{params.spring}} m from the wall?

### Answer Section

Please enter in a numeric value in {{ params.vars.part2.units }}.

## Part 3

Explain your answer from the previous section.

### Answer Section

Answer in 3-4 sentences, try and use full sentences.

## Part 4

What would have happened to the brick (when it is {{params.spring}} m from the wall) if I had set the conveyor belt to accelerate more rapidly than your answer from part 2? (Explain with words and numbers)

### Answer Section

Answer in 3-4 sentences, try and use full sentences.

## Part 5

Once the brick has moved too far from its original location, the spring will begin to pull it back towards the wall. The brick will then move back and forth until it settles down to a new equilibrium position. Determine the location of the final equilibrium position in relation to the wall.

### Answer Section

Please enter in a numeric value in {{ params.vars.part5.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)