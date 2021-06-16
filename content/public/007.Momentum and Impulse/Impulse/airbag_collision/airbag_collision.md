---
title: Airbags
topic: Momentum and Impulse
author: Jake Bobowski
source: 2013 Final Q2
template_version: 1.0
attribution: standard
outcomes:
- 6.3.1.2
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
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

     # store phrases etc
    data2["params"]["vars"]["title"] = 'Airbags'

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = "Increase the time of impact, increasing the average acceleration of the person they are protecting"
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = "Increase the time of impact, decreasing the average acceleration of the person they are protecting"
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = "Increase the time of impact, decreasing the impulse on the person"
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = "Increase the time of impact, increasing the impulse on the person"
    data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = "Explode to give you more oxygen to breathe"
    data2["params"]["part1"]["ans5"]["correct"] = False

    # Update the data object with a new dict
    data.update(data2)
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
      title: Airbags
    part1:
      ans1:
        value: Increase the time of impact, increasing the average acceleration of
          the person they are protecting
        correct: false
      ans2:
        value: Increase the time of impact, decreasing the average acceleration of
          the person they are protecting
        correct: true
      ans3:
        value: Increase the time of impact, decreasing the impulse on the person
        correct: false
      ans4:
        value: Increase the time of impact, increasing the impulse on the person
        correct: false
      ans5:
        value: Explode to give you more oxygen to breathe
        correct: false
---
# {{ params.vars.title }}
Modern cars are outfitted with air bags that quickly inflate with air if the car experiences too large an acceleration.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)