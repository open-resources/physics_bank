---
title: Perfect Elastic Collision of a Mass Attached to a Spring
topic: Simple Harmonic Motion
author: Jake Bobowski
source: 2012 Final Q13
template_version: 1.0
attribution: standard
outcomes:
- 7.5.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q13_2012Final.png
server:
  imports: |
    import sympy as sp
    import prairielearn as pl
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Perfect Elastic Collision of a Mass Attached to a Spring'

    # Declare math symbols to be used by sympy
    m1, m2, k, x0, v1, t, A, w = sp.symbols('m1 m2 k x0 v1 t A w')

    ## Part 1

    # Describe the solution equation. A1 is used for the amplitude so that A can be used in Part 3.
    A1 = sp.sqrt(m2/k)*((2*m1)/(m1+m2))*v1

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(A1)

    ## Part 2

    # Describe the solution equation
    T = 2*sp.pi*sp.sqrt(m2/k)

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part2_ans'] = pl.to_json(T)

    ## Part 3

    # Describe the solution equation
    x = A*sp.cos(w*t+(3*sp.pi/2))

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part3_ans'] = pl.to_json(x)

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: symbolic-input
  label: $A = $
  pl-customizations:
    variables: m1, m2, k, x0, v1
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  label: $T = $
  pl-customizations:
    variables: m1, m2, k, x0, v1
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  label: $x = $
  pl-customizations:
    variables: t, A, w
    weight: 1
    allow-blank: false
substitutions:
  params:
    vars:
      title: Perfect Elastic Collision of a Mass Attached to a Spring
  correct_answers:
    part1_ans:
      _type: sympy
      _value: 2*m1*v1*sqrt(m2/k)/(m1 + m2)
      _variables:
      - k
      - v1
      - m1
      - m2
    part2_ans:
      _type: sympy
      _value: 2*pi*sqrt(m2/k)
      _variables:
      - k
      - m2
    part3_ans:
      _type: sympy
      _value: A*sin(t*w)
      _variables:
      - t
      - w
      - A
---
# {{ params.vars.title }}
A block of mass $m_1$ slides across a frictionless surface with speed $v_1$ and collides perfectly elastically with a block $m_2$ (initially at rest).
Block $m_2$ is attached to a spring with spring constant $k$ and equilibrium length $x_0$.
Assume $m_2 > m_1$.

![A block of mass m one slides across a frictionless surface with speed v one and collides perfectly elastically with a block m two attached to a spring with spring constant k and equilibrium length x naught.](q13_2012Final.png)

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)