---
title: Box Up Ramp
topic: Force
author: John Hopkinson
source: PHYS 112 2020W1 GPS V
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
gradingMethod: Manual
showCorrectAnswer: false
outcomes:
- 6.3.1.2
- 6.3.1.3
- 6.5.1.1
- 6.6.1.2
- 6.7.1.0
- 6.9.1.2
- 6.9.1.3
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
    file-names: fbd.pdf
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
part3:
  type: symbolic-input
  pl-customizations:
    label: $\Sigma F_x =$
    variables: F_ab, f_krb, f_srb, W_eb, N_rb, theta
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $\Sigma F_y = $
    variables: F_ab, f_krb, f_srb, W_eb, N_rb, theta
    weight: 1
    allow-blank: false
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{\textit{A on B}} = $
    suffix: $\rm{N}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{\textit{A on B}} = $
    suffix: $\rm{N}$
part7:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Box Up Ramp
      name: Maya
    f: 178.0
    k: 0.1
    s: 0.4
    ang: 9
    part2:
      ans1:
        value: No, this is not an example of static or dynamic equilibrium.
        feedback: Consider the net force.
      ans2:
        value: This is an example of dynamic equilibrium.
        feedback: Great! You got it.
      ans3:
        value: This is an example of static equilibrium.
        feedback: Is the box at rest or in motion?
    part7:
      ans1:
        value: The box would slow down and come to a rest.
        feedback: Consider the net force in the x axis.
      ans2:
        value: The box would continue to speed up.
        feedback: Great! You got it; since $F_{net_x}$ > 0, the box would continue
          to speed up!
      ans3:
        value: The box would slow down until achieving a constant velocity.
        feedback: Consider the net force in the x axis.
---
# {{ params.vars.title }}
On moving day, {{params.vars.name}} pushes a box weighing {{params.f}} $\rm{N}$ at constant speed up a ramp. They push parallel to the ramp with a force of magnitude $F\_{\textit{A on B}}$ (see the figure below). The ramp makes an angle of $\theta = {{params.ang}}^{\circ}$ with the horizontal direction. The coefficients of static and kinetic friction friction between the box and the ramp are $\mu_s = {{params.s}}$ and  $\mu_k = {{params.k}}$, respectively.

<img src="graph.png" alt = "The top diagram is of a box travelling up an inclined ramp. There is a force vector in the center of the box pointing towards the top of the ramp, parallel to the ramp itself. It is labelled $F_{	extit{A on B}}}$. The bottom diagram is of an empty graph whose x-axis is parallel to the ramp while the y-axis is perpendicular to the ramp.">

## Question Text

Draw a free body diagram for this problem using the labelled axes provided in the figure. Label each force with subscripts indicating the agent of the force and the force on which it acts. Use R for ramp, A for {{params.vars.name}}, E for earth, and B for box. Be sure to consider the force {{params.vars.name}} exerts on the box $F\_{\textit{A on B}}$, the force of kinetic friction $f\_{\textit{k, R on B}}$, the force of static friction $f\_{\textit{s, R on B}}$, the weight of the box $W\_{\textit{E on B}}$, the normal force $N\_{\textit{R on B}}$, and any other forces that may be acting on the box.

### Answer Section

File upload box will be shown here.

## Part 2

Is this an example of static or dynamic equilibrium?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}

## Part 3

From your free body diagram, write Newton's second law equation for the x-components.

Note that it may not be necessary to use every variable and for angles, use their numeric value in degrees. Use the following table as a reference for each variable:

| For                      | Use   |
|--------------------------|-------|
| $F\_{\textit{A on B}}$    | F_ab  |
| $f\_{\textit{k, R on B}}$ | F_krb |
| $f\_{\textit{s, R on B}}$ | F_srb |
| $W\_{\textit{E on B}}$    | W_eb  |
| $N\_{\textit{R on B}}$    | N_rb  |
| $\theta$                 | theta |

### Answer Section

## Part 4

From your free body diagram, write Newton's second law equation for the y-components.

Note that it may not be necessary to use every variable and for angles, use their numeric value in degrees. Use the following table as a reference for each variable:

| For                      | Use   |
|--------------------------|-------|
| $F\_{\textit{A on B}}$    | F_ab  |
| $f\_{\textit{k, R on B}}$ | F_krb |
| $f\_{\textit{s, R on B}}$ | F_srb |
| $W\_{\textit{E on B}}$    | W_eb  |
| $N\_{\textit{R on B}}$    | N_rb  |
| $\theta$                 | theta |

### Answer Section

## Part 5

Solve your equations to find $F\_{\textit{A on B}}$.

### Answer Section

Please enter in a numeric value

## Part 6

If the box started at rest on the ramp, how hard would {{params.vars.name}} have to initially push the box to just overcome the static force of friction?

### Answer Section

Please enter in a numeric value

## Part 7

Once the box started moving, if {{params.vars.name}} maintained the force you found in Part 6, what would happen to the box?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)