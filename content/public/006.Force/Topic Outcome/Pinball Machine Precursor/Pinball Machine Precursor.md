---
title: Pinball Machine Precursor
topic: Force
author: John Hopkinson
source: PHYS 112 2014W Group Problem Solving V Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.4
- 6.12.1.1
- 6.11.2.1
- 6.1.1.5
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
- bagatelle.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{min}= $
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $N/m$
    comparison: sigfig
    digits: 3
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Pinball Machine Precursor
    l_u: 8.11
    l_c: 3.98
    rise: 8.08
    radius: 23
    m_b: 10.0
    part2:
      ans1:
        value: No, because the ball moves parallel to the walls of the track. The
          normal force and displacement are perpendicular.
      ans2:
        value: Yes, because the ball moves parallel to the walls of the track. The
          normal force and displacement are parallel.
      ans3:
        value: No, because the ball moves parallel to the walls of the track. The
          normal force and displacement are parallel.
      ans4:
        value: Yes, because the ball moves parallel to the walls of the track. The
          normal force and displacement are perpendicular.
    part4:
      ans1:
        value: The normal force will be zero wherever the ball first leaves the wall.
      ans2:
        value: The normal force will be equal to $g$.
      ans3:
        value: The normal force will be close to $1 N$.
      ans4:
        value: The normal force will be half of its initial value.
---
# {{ params.vars.title }}
A precursor of pinball machines involved manually pushing down on a ball suspended atop of a spring in a track that allows the ball only to travel up a ramp as shown in the figure.  The unstretched spring has a length of $l_u=$ {{ params.l_u }} $cm$, over the 1.00 $m$ length of the board the track rises by $r=$ {{ params.rise }} $cm$, and the top of the board is circular, with a radius of {{ params.radius }}.0 $cm$.

Treat the ball as a particle of mass $m$ = {{ params.m_b }} $g$, (treating it as a sphere would give a small additional term to the kinetic energy) and ignore friction.

<img src="bagatelle.png" alt="Figure of a ball of length 1 metre with a semi-circular top. The highest point is A and the tangent line to a point B on the circular surface meets a straight vertical line at 45 degrees. The pinball is suspended atop of a spring in a track with a rise of r cm on the right side of the board." width=400>

## Part 1

Write the free body diagram for the ball at the top of the loop, and use this to solve for the minimum speed required by the ball at this point for the ball to remain in circular motion at the top of its arc.

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 2

Can the normal force due to the walls of the track ever do work on the ball?  Explain your answer.

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}
- {{ params.part2.ans4.value}}

## Part 3

If the spring was initially compressed to a length of {{ params.l_c }} $cm$ prior to its release, and it had the minimum speed to remain in circular motion when it reached the top, find the value of the spring constant, $k$.

### Answer Section

Please enter in a numeric value in $N/m$.

## Part 4

A ball leaving the wall at position B will land for 15 points.

What value does the normal force (from the ends of the track) take at the point where the ball first leaves the wall?

### Answer Section

- {{ params.part4.ans1.value}}
- {{ params.part4.ans2.value}}
- {{ params.part4.ans3.value}}
- {{ params.part4.ans4.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)