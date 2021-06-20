---
title: Perfectly Inelastic Collision of Raindrops
topic: Momentum
author: Jake Bobowski
source: 2012 Final Q2
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 7.5.1.3
- 7.5.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
server:
  imports: |
    import random as rd
    import sympy as sp
    import numpy as np
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = 'Perfectly Inelastic Collision of Raindrops'\n\
    data2[\"params\"][\"vars\"][\"units\"] = \"m/s\"\n\n# Randomize Variables\nm1\
    \ = pbh.roundp(rd.uniform(0.10, 1.00), decimals = 2)\nm2 = pbh.roundp(rd.uniform(0.10,\
    \ 1.00), decimals = 2)\n\nv1_i = pbh.roundp(rd.uniform(-20.0, 20.0), sigfigs =\
    \ 3)     # separate the terms to do the math \nv1_j = pbh.roundp(rd.uniform(-20,\
    \ 20.0), sigfigs = 3)\n\nv2_i = pbh.roundp(rd.uniform(-20.0, 20.0), sigfigs =\
    \ 3)\nv2_j = pbh.roundp(rd.uniform(-20.0, 20.0), sigfigs = 3)\n\n# store the variables\
    \ in the dictionary \"params\"\ndata2[\"params\"][\"m1\"] = m1\ndata2[\"params\"\
    ][\"m2\"] = m2\ndata2[\"params\"][\"v1_i\"] = v1_i\ndata2[\"params\"][\"v2_i\"\
    ] = v2_i\ndata2[\"params\"][\"v1_j_abs\"] = np.abs(v1_j)\ndata2[\"params\"][\"\
    v2_j_abs\"] = np.abs(v2_j)\ndata2[\"params\"][\"v1_j_sign\"] = pbh.sign_str(v1_j)\n\
    data2[\"params\"][\"v2_j_sign\"] = pbh.sign_str(v2_j)\n\n# define possible answers\n\
    \n## ans1\nvf_i = pbh.roundp((m1*v1_i + m2*v2_i)/m1, sigfigs = 2)\nvf_j = pbh.roundp((m1*v1_j\
    \ + m2*v2_j)/m1, sigfigs = 2)\n\ndata2[\"params\"][\"part1\"][\"ans1\"][\"value\"\
    ] = str(vf_i) + \"$\\hat{\\imath}$\" + pbh.sign_str(vf_j) + str(np.abs(vf_j))\
    \ + \"$\\hat{\\jmath}$\"\ndata2[\"params\"][\"part1\"][\"ans1\"][\"correct\"]\
    \ = False\n\n## ans2\n\nvf_i = pbh.roundp((m1*v1_i + m2*v2_i)/(m1+m2), sigfigs\
    \ = 2)\nvf_j = pbh.roundp((m1*v1_j + m2*v2_j)/(m1+m2), sigfigs = 2)\n\ndata2[\"\
    params\"][\"part1\"][\"ans2\"][\"value\"] = str(vf_i) + \"$\\hat{\\imath}$\" +\
    \ pbh.sign_str(vf_j) + str(np.abs(vf_j)) + \"$\\hat{\\jmath}$\"\ndata2[\"params\"\
    ][\"part1\"][\"ans2\"][\"correct\"] = True\n\n## ans3\n\nvf_i = pbh.roundp((m1*v1_i\
    \ + m2*v2_i)/m2, sigfigs = 2)\nvf_j = pbh.roundp((m1*v1_j + m2*v2_j)/m2, sigfigs\
    \ = 2)\n\ndata2[\"params\"][\"part1\"][\"ans3\"][\"value\"] = str(vf_i) + \"$\\\
    hat{\\imath}$\" + pbh.sign_str(vf_j) + str(np.abs(vf_j)) + \"$\\hat{\\jmath}$\"\
    \ndata2[\"params\"][\"part1\"][\"ans3\"][\"correct\"] = False\n\n## ans4\n\nvf_i\
    \ = pbh.roundp((m1*v1_i + m2*v2_i)/2*(m1+m2), sigfigs = 2)\nvf_j = pbh.roundp((m1*v1_j\
    \ + m2*v2_j)/2*(m1+m2), sigfigs = 2)\n\ndata2[\"params\"][\"part1\"][\"ans4\"\
    ][\"value\"] = str(vf_i) + \"$\\hat{\\imath}$\" + pbh.sign_str(vf_j) + str(np.abs(vf_j))\
    \ + \"$\\hat{\\jmath}$\"\ndata2[\"params\"][\"part1\"][\"ans4\"][\"correct\"]\
    \ = False\n\n## ans5\n\nvf_i = pbh.roundp((m1*v1_i - m2*v2_i)/0.5*(m1+m2), sigfigs\
    \ = 2)\nvf_j = pbh.roundp((m1*v1_j - m2*v2_j)/0.5*(m1+m2), sigfigs = 2)\n\ndata2[\"\
    params\"][\"part1\"][\"ans5\"][\"value\"] = str(vf_i) + \"$\\hat{\\imath}$\" +\
    \ pbh.sign_str(vf_j) + str(np.abs(vf_j)) + \"$\\hat{\\jmath}$\"\ndata2[\"params\"\
    ][\"part1\"][\"ans5\"][\"correct\"] = False\n\n## ans6\n\nvf_i = pbh.roundp((m1*v1_i\
    \ - m2*v2_i)/(m1+m2), sigfigs = 2)\nvf_j = pbh.roundp((m1*v1_j - m2*v2_j)/(m1+m2),\
    \ sigfigs = 2)\n\ndata2[\"params\"][\"part1\"][\"ans6\"][\"value\"] = str(vf_i)\
    \ + \"$\\hat{\\imath}$\" + pbh.sign_str(vf_j) + str(np.abs(vf_j)) + \"$\\hat{\\\
    jmath}$\"\ndata2[\"params\"][\"part1\"][\"ans6\"][\"correct\"] = False\n\n# Update\
    \ the data object with a new dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Perfectly Inelastic Collision of Raindrops
      units: m/s
    m1: 0.32
    m2: 0.31
    v1_i: -11.4
    v2_i: 2.02
    v1_j_abs: !!python/object/apply:numpy.core.multiarray.scalar
    - &id001 !!python/object/apply:numpy.dtype
      args:
      - f8
      - false
      - true
      state: !!python/tuple
      - 3
      - <
      - null
      - null
      - null
      - -1
      - -1
      - 0
    - !!binary |
      7FG4HoXrB0A=
    v2_j_abs: !!python/object/apply:numpy.core.multiarray.scalar
    - *id001
    - !!binary |
      pHA9Ctej9D8=
    v1_j_sign: ' - '
    v2_j_sign: ' + '
    part1:
      ans1:
        value: -9.4$\hat{\imath}$ - 1.7$\hat{\jmath}$
        correct: false
      ans2:
        value: -4.8$\hat{\imath}$ - 0.88$\hat{\jmath}$
        correct: true
      ans3:
        value: -9.7$\hat{\imath}$ - 1.8$\hat{\jmath}$
        correct: false
      ans4:
        value: -0.95$\hat{\imath}$ - 0.18$\hat{\jmath}$
        correct: false
      ans5:
        value: -5.4$\hat{\imath}$ - 1.7$\hat{\jmath}$
        correct: false
      ans6:
        value: -6.8$\hat{\imath}$ - 2.2$\hat{\jmath}$
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)