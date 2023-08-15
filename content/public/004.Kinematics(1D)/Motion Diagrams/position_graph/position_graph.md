---
title: Position Graph
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2015W1 GPS2 Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
gradingMethod: Manual
showCorrectAnswer: false
outcomes:
- 1.2.1.7
- 4.3.1.2
- 4.6.1.2
- 4.6.1.4
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
- EX
assets:
- graph.png
part1:
  type: file-upload
  pl-customizations:
    file-names: graph.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.1
    weight: 1
    allow-blank: true
    label: $v_{ax} = $
    suffix: $\rm{m/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.1
    weight: 1
    allow-blank: true
    label: $v_{bx} = $
    suffix: $\rm{m/s}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.1
    weight: 1
    allow-blank: true
    label: $v_{cx} =$
    suffix: $\rm{m/s}$
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Position Graph
    params_part5_ans1_value: There is no sign.
    params_part5_ans1_feedback: 'Please try again! Hint: Try finding the velocities
      before and after point B (recall the definition of acceleration).'
    params_part5_ans2_value: Negative
    params_part5_ans2_feedback: Great! You got it; the velocity $v_x$ is positive
      just before B and negative after B, thus $a_x$ has a negative sign!
    params_part5_ans3_value: Positive
    params_part5_ans3_feedback: 'Please try again! Hint: Try finding the velocities
      before and after point B (recall the definition of acceleration).'
---
# {{ params_vars_title }}
At each of A, B and C on the graph below, estimate the $x$-component of the velocity vector, $v_x$ from the position vs. time graph.

<img src="graph.png" alt = "This is a position vs. time graph. The y-axis is labelled 'x (m)' and the x-axis is labelled 't (s)'. Each grid is 1m and 1s. There is an upside down parabola, with its roots at t = 3s (labelled point A) and 7s (labelled point C). Its vertex is approximately at 2.5m and 5s (labelled point B). The rest of the parabola extends downwards to infinity.">

## Part 1

Draw a tangent line to the graph at each point (A,B,C).

Please save the above image to use for sketching on the graph. Make sure to keep your tangent lines clear.

Upload your final graph as a pdf file titled "graph.pdf".

### Answer Section

File upload box will be shown here.

## Part 2

Please enter your estimation of the $x$-component of the velocity vector $v_x$ at A.

### Answer Section

Please enter in a numeric value.

## Part 3

Please enter your estimation of the $x$-component of the velocity vector $v_x$ at B.

### Answer Section

Please enter in a numeric value.

## Part 4

Please enter your estimation of the $x$-component of the velocity vector $v_x$ at C.

### Answer Section

Please enter in a numeric value.

## Part 5

What sign, if any, does the x-component of the acceleration vector, $a_x$ , have at point B?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)