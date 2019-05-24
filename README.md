# Nucleus SDK
Nucleus SDK with instructions and examples on how to use Nucleus APIs

## Overview
Nucleus SDK is a suite of high-performance text-analytics APIs developed by 
SumUp Analytics, Inc and subject to Terms of Services available at www.sumup.ai. 
Copyright SumUp Analytics Inc, 2019.

Those APIs enable end-users to perform the following tasks:
## 1. Analytics
### a. Document-level
* Sentiment analysis
* Per-document Summarization
* Per-document Contrasted Summarization
* Document classification in user-controlled sub-categories

### b. Topic-level
* Topic modeling
* Topic transfer learning for propagation analysis of prevalence, sentiment and consensus
* Sentiment analysis
* Consensus analysis
* Named Entity tagging (strict match)
* Cross-documents Topic Summarization
* Historical analysis of prevalence, sentiment and consensus
* Author connectivity analysis
* Contrasted topic modeling: topic best separating two sub-categories of documents in a corpus
* Content recommendation
* Topic exposure variation, as building block for time-series predictive modeling

## 2. Dataset Management
* Dataset creation (whole pre-processing pipeline)
* Metadata-based documents' selection
* Document rendering
* Dataset management


13 languages are currently supported by those APIs: English, Chinese (Simplified and Traditional), Japanese, 
Portuguese, Spanish, German, Russian, Italian, French, Arabic, Farsi, Hindi.

The core task, topic modeling, has been benchmarked against Scikit-Learn, Gensim 
and AWS Comprehend topic models and delivers 100x speed-up with 2x accuracy on a 
wide range of dataset sizes, complexity and languages. More details can be found 
at www.sumup.ai in Nucleus Solution Brief (https://www.sumup.ai/SumUp%20Real-Time%20Text%20Analytics%20Solution%20Brief.pdf)

## Python SDK
Python SDK is available in [*python*](python) directory.

## Javascript SDK
Javascript SDK is available in [*javascript*](javascript) directory.

## Note to Jupyter Notebook users
We strongly recommend that rapid testing done in Jupyter Notebook be limited to 
1,000 documents being uploaded through our APIs from within the notebook.

Jupyter Notebooks suffer from file descriptor leakage and this will cause your 
tests on large datasets being uploaded from within these notebooks to error out 
with a message such as 'Too many open files'.

Once your rapid testing is done in notebook, best is to move to scripts to perform 
testing and exploration on much larger corpuses.
