---
title: Bat Doppler
topic: Waves
author: John Hopkinson
source: Phys122 2022S T8 Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 16.8.1.0
- 16.8.1.1
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
- HZ
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Bat Doppler
    params_part1_ans1_value: We don't know if the bat is moving closer to or moving
      farther away from the mosquito.
    params_part1_ans1_feedback: A frequency increase is not consistent with both the
      bat and mosquito approaching each other and moving farther away from each other.
    params_part1_ans2_value: The bat is moving farther away from the mosquito.
    params_part1_ans2_feedback: When the bat moves farther from the mosquito the reflected
      frequency will decrease.
    params_part1_ans3_value: The mosquito has evolved to mimic the sound waves produced
      by the bat to confuse it.
    params_part1_ans3_feedback: While there are moths that have been reported to mimic
      the sound wave to confuse their predators, mosquitos are not believed to.
    params_part1_ans4_value: Both the bat and mosquito are flying at the same rate
      in the same direction.
    params_part1_ans4_feedback: If the distance between bat and mosquito is not changing
      the frequency of sound between them should not be changing because of the Doppler
      effect.
    params_part1_ans5_value: The bat is moving closer to the mosquito.
    params_part1_ans5_feedback: Yes! You got it. Frequency increases when sources
      or receivers approach due to the Doppler effect.
---
# {{ params_vars_title }}
Bats have poor eyesight, so they use echolocation to orient themselves and to hunt prey (insects). They emit ultrasonic sound waves as chirps and listen to hear if the reflected waves are Doppler shifted to higher or lower frequencies as they fly.

## Useful Info

The Doppler effect for sound waves tells us when a sound source and a sound observer move relative to each other at speeds $v\_{source}$ and $v\_{observer}$ respectively, the frequency observed by the observer is given by $f\_{observer} = \frac{(1\pm \frac{v\_{observer}}{v\_{sound}})}{(1 - \mp \frac{v\_{source}}{v\_{sound}})} f_0$ where $f_0$ is the frequency of emitted sound, and $v\_{sound}$ is the speed of sound. In the numerator of this expression a plus (minus) sign indicates that the observer is moving toward (away from) the source. In the denominator of this expression a plus (minus) sign indicates that the source is moving away from (toward) the observer. In both cases this means that the frequency increases when the objects are approaching, and decreases when they are receding from each other. (In this problem involving a reflection picked up by the original source there would actually be two Doppler shifts, with the frequency of sound reflected by the mosquito acting as the source of sound for the bat, and the bat acting as the observer of that sound.)

## Part 1

If the reflected waves from a mosquito have slightly increased in frequency:

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)