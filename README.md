## Introduction

This package provides data augmentation techniques for text data using back translation and synonym replacement. Data augmentation is a technique to increase the size of the training data by generating new samples from the existing ones. This can be helpful in improving the performance of machine learning models by making them more robust and generalizable.

## Installation

You can install the package using `pip`:

```python
pip install TextBooster
```

## Usage
The package provides two functions for data augmentation: back_Translation() and synonym_Replacement().

## Back Translation:
This function performs back translation of the given text to a randomly chosen target language and then back to the source language. This can be useful in generating new samples with different sentence structures and word choices.

This function performs back translation of the given text to a randomly chosen target language and then back to the source language. This can be useful in generating new samples with different sentence structures and word choices.

```python
from TextBooster import back_Translation

text = "The quick brown fox jumps over the lazy dog."
augmented_texts = back_Translation(text, nbre_samples=3)

print(augmented_texts)
```
Output:
```vbnet
['The quick brown fox jumps over the indolent dog.',
 'The quick brown fox jumped over the lazy dog.',
 'The quick brown fox jumps over the torpid dog.']
```

## Synonym Replacement:
This function replaces each word in the given text with one of its synonyms, chosen randomly. This can be useful in generating new samples with different word choices.
```python
from textaugment import synonym_Replacement

text = "The quick brown fox jumps over the lazy dog."
augmented_texts = synonym_Replacement(text)

print(augmented_texts)
```
