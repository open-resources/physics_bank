---
title: Continuous Charge Distributions
topic: Electrostatics
author: John Hopkinson
source: Phys 122 2019 GPSX
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.6.1.2
- 18.6.1.3
- 18.6.1.4
- 18.11.2.4
- 18.11.5.1
difficulty:
- undefined
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- AC
assets:
- piecemeal.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $dV_{1} = $
    variables: R, K, dq1, dq2, q1, q2, z, dv1, dv2, zero, V, E
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $dV_{2} = $
    variables: R, K, dq1, dq2, q1, q2, z, dv1, dv2, zero, V, E
    weight: 1
    allow-blank: false
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
part4:
  type: symbolic-input
  pl-customizations:
    label: $V(z) = $
    variables: R, K, dq1, dq2, q1, q2, z, dv1, dv2, zero, V, E
    weight: 1
    allow-blank: false
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
part6:
  type: symbolic-input
  pl-customizations:
    label: $E_{z} = $
    variables: R, K, dq1, dq2, q1, q2, z, dv1, dv2, zero, V, E
    weight: 1
    allow-blank: false
part7:
  type: number-input
  pl-customizations:
    label: $V = $
    weight: 1
    allow-blank: true
part8:
  type: number-input
  pl-customizations:
    label: $E_{z} = $
    weight: 1
    allow-blank: true
myst:
  substitutions:
    params:
      vars:
        title: Continuous Charge Distributions
      part3:
        ans1:
          value: No you would get the same result, as the charge $dq_1$ would be at
            a different distance from the point of interest at ($x$, $y$, $z$) = (0,
            0, $z$)
        ans2:
          value: Yes you would get the same result, as the charge $dq_1$ would be
            at the same distance from the point of interest at ($x$, $y$, $z$) = (0,
            0, $z$)
        ans3:
          value: Yes you would get the same result, as the charge $dq_1$ would be
            at the same distance from the point of interest at ($x$, $y$, $z$) = ($x$,
            0, 0)
        ans4:
          value: No you would get the same result, as the charge $dq_1$ would be at
            a different distance from the point of interest at ($x$, $y$, $z$) = ($x$,
            0, 0)
      part5:
        ans1:
          value: The equal charges are uniformly distributed on the opposite sides
            of the x-axis, so any components parallel to the x-axis will add to zero.
            The electric field must be perpendicular to the x-axis
        ans2:
          value: The equal charges are uniformly distributed on the opposite sides
            of the z-axis, so any components parallel to the z-axis will add to zero.
            The electric field must be perpendicular to the z-axis
        ans3:
          value: The equal charges are uniformly distributed on the opposite sides
            of the x-axis, so any components perpendicular to the x-axis will add
            to zero. The electric field must be parallel (or antiparallel) to the
            x-axis
        ans4:
          value: The equal charges are uniformly distributed on the opposite sides
            of the z-axis, so any components perpendicular to the z-axis will add
            to zero. The electric field must be parallel (or antiparallel) to the
            z-axis
      b: -2
      c: 4
      d: 4
      e: 6
---
# {{ params.vars.title }}
A thin ring of radius $R$ lies in the $xy$ plane, centred on the $z$-axis. The ring has four uncharged insulating pieces. (dark patches of figure below) and four metallic ars. Two of these metallic arcs have charge $q_1$ and two have charge $q_2$, symmetrically placed about ($x$, $y$, $z$) = (0,0,0) as shown in the figure below.

<img src="piecemeal.png" width=400 alt>

## Part 1

Write the small element of the electric potential $dV_1$ at heigh $z$ along the $z$-axis due to a small element of charge $dq_1$ as shown in the figure above.
Hint: assume the small element of charge is small enough to treat as a point charge.

Use the following table as a reference for each variable:

| For    | Use |
|--------|-----|
| $R$    | R   |
| $K$    | K   |
| $dq_1$ | dq1 |
| $dq_2$ | dq2 |
| $q_1$  | q1  |
| $q_2$  | q2  |
| $z$    | z   |

**If the answer is 0, enter "zero"**.

### Answer Section

## Part 2

Write the small element of the electric potential $dV_2$ at heigh $z$ along the $z$-axis due to a small element of charge $dq_2$ as shown in the figure above.

Use the following table as a reference for each variable:

| For    | Use |
|--------|-----|
| $R$    | R   |
| $K$    | K   |
| $dq_1$ | dq1 |
| $dq_2$ | dq2 |
| $q_1$  | q1  |
| $q_2$  | q2  |
| $z$    | z   |

**If the answer is 0, enter "zero"**.

### Answer Section

## Part 3

For $any$ small element of charge $dq_1$ on either patch of charge $q_1$, would you get the result found in (a)?

### Answer Section

- {{ params.part3.ans1.value }}
- {{ params.part3.ans2.value }}
- {{ params.part3.ans3.value }}
- {{ params.part3.ans4.value }}

## Part 4

Integrate your expressions from parts (a) and (b) to find the total electric potential due to this ring along the $z$-axis at $z$ = 3m.

Use the following table as a reference for each variable:

| For    | Use |
|--------|-----|
| $R$    | R   |
| $K$    | K   |
| $dq_1$ | dq1 |
| $dq_2$ | dq2 |
| $q_1$  | q1  |
| $q_2$  | q2  |
| $z$    | z   |

**If the answer is 0, enter "zero"**.

### Answer Section

## Part 5

Assuming that the charged patches are of equal sizes and on opposite sides of the ring, as shown in Fig. 1, explain what direction the electric field of this ring would have to point in and why.

### Answer Section

- {{ params.part5.ans1.value }}
- {{ params.part5.ans2.value }}
- {{ params.part5.ans3.value }}
- {{ params.part5.ans4.value }}

## Part 6

Find the $z$-component of the electric field due to this ring at height $z$.

Use the following table as a reference for each variable:

| For    | Use |
|--------|-----|
| $R$    | R   |
| $K$    | K   |
| $dq_1$ | dq1 |
| $dq_2$ | dq2 |
| $q_1$  | q1  |
| $q_2$  | q2  |
| $z$    | z   |

**If the answer is 0, enter "zero".**

### Answer Section

## Part 7

If $q_1$ = {{ params.b}}$\mu C$ and $q_2$ = {{ params.c}}$\mu C$, $R$ = {{ params.d}}m and $z$ = {{ params.e}}m, find $V$.

Note: $\mu = 10^{-6}$ and $K$ = 9.0 $\times 10^9 \frac{\text{N m}^2}{\text{C}^2}$

### Answer Section

## Part 8

If $q_1$ = {{ params.b}}$\mu C$ and $q_2$ = {{ params.c}}$\mu C$, $R$ = {{ params.d}}m and $z$ = {{ params.e}}m, find $E_z$.

Note: $\mu = 10^{-6}$ and $K$ = 9.0 $\times 10^9 \frac{\text{N m}^2}{\text{C}^2}$

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)