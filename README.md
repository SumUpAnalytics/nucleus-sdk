# Nucleus SDK
Nucleus SDK with instructions and examples on how to use Nucleus APIs

## Overview
Nucleus SDK is a suite of high-performance text-analytics APIs developed by SumUp Analytics, Inc and subject to Terms of Services available at www.sumup.ai. Copyright SumUp Analytics Inc, 2018.

Those APIs enable end-users to perform the following tasks:
1. Analytics
* Topic modeling
* Summarization at the Topic and Document level
* Sentiment analysis at the Topic level
* Consensus analysis at the Topic level
* Content recommendation at the Topic level
* Historical analysis of prevalence, sentiment and consensus at the Topic level
* Author connectivity analysis
* Topic exposure variation, as building block for time-series predictive modeling

2. Dataset Management
* Dataset creation (whole pre-processing pipeline)
* Retrieval of documents metadata
* Document display
* Selective documents deletion
* Dataset deletion

10 languages are currently supported by those APIs: English, Mandarin, Japanese, Portuguese, Spanish, German, Russian, Italian, French, Farsi.

The core task, topic modeling, has been benchmarked against Scikit-Learn, Gensim and AWS Comprehend topic models and delivers 100x speed-up with 2x accuracy. More details can be found at www.sumup.ai in Nucleus Solution Brief (https://www.sumup.ai/SumUp%20Real-Time%20Text%20Analytics%20Solution%20Brief.pdf)

## Prerequisites
1. Python 3.5 or 3.6 is set up in a virtual environment. More details: https://docs.python.org/3/tutorial/venv.html
2. Java 7 or 8 is installed. More details: https://www.oracle.com/technetwork/java/index.html 

## Python SDK Generation
The starting point of all command sequence is the root of the repository.  
1. Install Swagger Generator  
   Below are quick-start instructions for the operations systems that we have tested. For more details or OS not listed below please refer to https://github.com/swagger-api/swagger-codegen .
  * MacOS:   
    `brew install swagger-codegen`
  
  * Ubuntu:   
    ```
    cd swagger
    wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
    cd ..
    ```

2. Run Swagger Code Generator to generate Nucleus client Python module
  * MacOS:  
    ```
    cd swagger
    swagger-codegen generate -i nucleus-api-swagger.json -l python -c config.json -o sdk
    cd ..
    ```

  * Ubuntu:  
    ```
    cd swagger
    java -jar swagger-codegen-cli.jar generate -i nucleus-api-swagger.json -l python -c config.json -o sdk
    cd ..
    ```

3. Install Nucleus client Python module. This step assumes that you are running python from a Python3 virtual environment
```
cd swagger/sdk
python3 setup.py install
cd ../..
```

## Python SDK Documentation
The documentation on all available APIs can be found in swagger/sdk/README.md and swagger/sdk/docs after Swagger
Code Generator has been run.

A Guideline for Calibration is available in examples/ directory: [a relative link](examples/Guidelines%20for%20Calibrating%20Nucleus%20APIs.pdf) 

## Example using Nucleus APIs
1. Go to the examples directory `cd examples`
2. Open all-api-examples.py in a text editor and update the lines below with provided host name and API key  
    ```
    configuration.host = 'API_HOST_HERE'
    configuration.api_key['x-api-key'] = 'API_KEY_HERE'
    ```
3. Execute the example: 'python3 all-api-examples.py'

4. For Jupyter Notebook users, please use all-api-examples.ipynb in your notebook. 
