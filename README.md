# Nucleus SDK
Instructions and examples on how to use the Nucleus SDK. This GitHub repository is meant to complement the official Nucleus SDK Documentation available at www.sumup.ai/apis/#nucleus-documentation

## Overview
Nucleus is the Intelligent Text Data Platform developed and commercialized by SumUp Analytics.
The Nucleus SDK is one of Nucleus' end-points, aiming at users needing a flexible and high-performance access to integrate into existing workflows and applications.

It is subject to Terms of Services available at www.sumup.ai. 

Copyright SumUp Analytics Inc, 2018 - present.

## Capabilities
Nucleus currently natively supports 13 languages: English, Chinese (Simplified and Traditional), Japanese, 
Portuguese, Spanish, German, Russian, Italian, French, Arabic, Farsi, Hindi.

Nucleus currently supports the following document formats: JSON, PDF, TXT/RTF, DOCX, HTML, XML, CSV.

The SDK enables users to perform the following tasks:
### 1. Processing
* Data transformation & representation
* Metadata filtering
* Search
* Local repositories synchronization
* Resources management

### 2. Core Analytics
* Topic extraction
* Summarization
* Sentiment & consensus
* Topic importance
* Historical analysis
* Content recommendation
* Assisted data labeling

### 3. Advanced Analytics
* Contrast analysis
* Novelty analysis
* Key contributors' analysis
* Transfer learning
* Content classification
* Authors network analysis
* Streaming analytics

## Available SDKs
### 1. Python SDK
A Python SDK is available in [*python*](python) directory.

### 2. Javascript SDK
A Javascript SDK is available in [*javascript*](javascript) directory.

## Note to Jupyter Notebook users
We strongly recommend that rapid testing done in Jupyter Notebook be limited to 
1,000 documents being uploaded through our APIs from within the notebook.

Jupyter Notebooks suffer from file descriptor leakage and this will cause your 
tests on large datasets being uploaded from within these notebooks to error out 
with a message such as 'Too many open files'.

Once your rapid testing is done in notebook, best is to move to scripts to perform 
testing and exploration on much larger corpora.

## Benchmarks
The core task, topic modeling, has been benchmarked against Scikit-Learn, Gensim 
and AWS Comprehend topic models and delivers 100x speed-up with 2x accuracy on a 
wide range of dataset sizes, complexity and languages. More details can be found 
at www.sumup.ai in Nucleus Solution Brief (https://app.hubspot.com/documents/5812509/view/44612668?accessId=9bf45e)

Other benchmarks and performance studies are available on SumUp Analytics' blog: www.sumup.ai/blog
