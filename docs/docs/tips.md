# Tips for authoring questions

Below is a list of suggestions and recommendataions when authoring questions.

## Shuffling choices

Let's imagine an MCQ that has 3 distractors and 1 correct choice (total of 4).

1. PL will automatically shuffle Multiple Choice / Dropdown / checkbox choices so each variant produces a uniquely ordered list. 
2. The reason we used `random.shuffle()`, is because we had a "bank" of choices (say 10 distractors) and 3 correct choices, and we wanted to construct a series of questions where each variant would get DIFFERENT distractors and DIFFERENT correct answers

So, in short, here's the guideline: 

- If your question is one where the distractors are always the same (whether they are calculated or fixed), you don't need to shuffle and draw from the list. PL will randomize the order. 
- If your question has a bank of correct and a bank of incorrect choices, then you should shuffle the list so that each variant has different choices.
