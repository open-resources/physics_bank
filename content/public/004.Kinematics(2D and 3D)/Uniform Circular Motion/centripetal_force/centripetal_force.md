---
title: Centripetal Motion
topic: centripetal motion
author: Michael Kudla
source: original
template_version: 1.0
attribution: standard
outcomes:
- undefined
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
server:
  imports: |
    import random
    import prairielearn as pl
    import sympy
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    data2["params"]["vars"]["title"] = "Centripetal Motion"

    # Declare math symbols to be used by sympy
    m, v, r = sympy.symbols('m v r')

    # Describe the solution equation
    F = m*v**2/r

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']["part1_ans"] = pl.to_json(F)

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: "pass    \n"
part1:
  type: symbolic-input
  label: $F_r = $
  pl-customizations:
    variables: m, v, r
    weight: 1
    allow-blank: false
substitutions:
  params:
    vars:
      title: Centripetal Motion
  correct_answers:
    part1_ans:
      _type: sympy
      _value: m*v**2/r
      _variables:
      - v
      - r
      - m
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).