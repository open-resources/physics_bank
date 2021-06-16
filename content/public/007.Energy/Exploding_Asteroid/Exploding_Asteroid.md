---
title: Exploding Asteroid
topic: Energy
author: Jake Bobowski
source: Final 2016 Q6
template_version: 1.0
attribution: standard
outcomes:
- 8.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# define or load names/items/objects\n\
    names = pd.read_csv(\"data/names.csv\")[\"Names\"].tolist()\n\n# store phrases\
    \ etc\ndata2[\"params\"][\"vars\"][\"title\"] = 'Exploding Asteroid'\ndata2[\"\
    params\"][\"vars\"][\"name\"] = random.choice(names)\ndata2[\"params\"][\"vars\"\
    ][\"name2\"] = random.choice(names)\n\n# define useful variables/lists\n\n# create\
    \ list of answers and shuffle\nanswers = [\n\"The momentum vectors they use to\
    \ describe each of the two asteroid pieces will be the same.\", \n\"The total\
    \ momentum vectors they use to describe the asteroid system (both pieces) will\
    \ be the same.\", \n\"The CHANGE in the momentum vector they determine for each\
    \ piece of the asteroid before and after the explosion will be the same.\", \n\
    \"The FORCE vector they determine that each piece of the asteroid felt during\
    \ the explosion will be the same.\", \n\"The final velocity vectors they use to\
    \ describe the two asteroid pieces will be the same.\", \n\"The final speeds they\
    \ measure for the two asteroid pieces will be the same.\", \n\"They will both\
    \ agree on how much kinetic energy each of the asteroid pieces has.\", \n\"They\
    \ will both agree on how the kinetic energy of each of the pieces has changed.\"\
    , \n\"They will both agree on how the TOTAL kinetic energy of the system has changed.\"\
    , \n\"They will both agree on how the internal energy of the system has changed.\"\
    \n]\n\ncorrect_answers = [\n    \"The momentum vectors they use to describe each\
    \ of the two asteroid pieces will be the same.\", \n    \"The total momentum vectors\
    \ they use to describe the asteroid system (both pieces) will be the same.\",\n\
    \    \"The final velocity vectors they use to describe the two asteroid pieces\
    \ will be the same.\",\n    \"The final speeds they measure for the two asteroid\
    \ pieces will be the same.\", \n    \"They will both agree on how much kinetic\
    \ energy each of the asteroid pieces has.\", \n]\n\nrandom.shuffle(answers)\n\n\
    # Create ans_choices\nnum_choices = 6\n\nfor i,this_answer in enumerate(random.sample(answers,num_choices)):\n\
    \    \n    choice = f\"ans{i+1}\"\n    \n    data2[\"params\"][\"part1\"][choice][\"\
    value\"] = this_answer\n\n    if this_answer in correct_answers:\n        data2[\"\
    params\"][\"part1\"][choice][\"correct\"] = False\n    else:\n        data2[\"\
    params\"][\"part1\"][choice][\"correct\"] = True\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: "pass    \n"
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
substitutions:
  params:
    vars:
      title: Exploding Asteroid
      name: Ahmed
      name2: Maya
    part1:
      ans1:
        value: The final speeds they measure for the two asteroid pieces will be the
          same.
        correct: false
      ans2:
        value: They will both agree on how the internal energy of the system has changed.
        correct: true
      ans3:
        value: The FORCE vector they determine that each piece of the asteroid felt
          during the explosion will be the same.
        correct: true
      ans4:
        value: They will both agree on how the TOTAL kinetic energy of the system
          has changed.
        correct: true
      ans5:
        value: The CHANGE in the momentum vector they determine for each piece of
          the asteroid before and after the explosion will be the same.
        correct: true
      ans6:
        value: The final velocity vectors they use to describe the two asteroid pieces
          will be the same.
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)