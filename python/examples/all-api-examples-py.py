#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2018-2019 SumUp Analytics, Inc. All Rights Reserved.
# 
# NOTICE: All information contained herein is, and remains the property of SumUp Analytics Inc. and its suppliers, if any. The intellectual and technical concepts contained herein are proprietary to SumUp Analytics Inc. and its suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.
# 
# Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from SumUp Analytics Inc.

# # Initialization, configure API host and key, and create new API instance

# In[1]:


import os
import csv
import json
import datetime
import time
import nucleus_api
from nucleus_api.rest import ApiException
import nucleus_api.api.nucleus_api as nucleus_helper
from pprint import pprint
import numpy as np
from pathlib import Path

# Determine if in Jupyter notebook or not
try:
    ip = get_ipython()
    running_notebook = True
except NameError:
    running_notebook = False

if running_notebook:
    print('Running example in Jupyter Notebook')
else:
    print('Running example in script mode')
    
configuration = nucleus_api.Configuration()
configuration.host = 'UPDATE-WITH-API-SERVER-HOSTNAME'
configuration.api_key['x-api-key'] = 'UPDATE-WITH-API-KEY'

# Create API instance
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))


# # Dataset APIs

# ## Append file from local drive to dataset

# In[2]:


print('--------- Append file from local drive to dataset -----------')
file = 'quarles20181109a.pdf'         # file | 
dataset = 'dataset_test'              # str | Destination dataset where the file will be inserted.
metadata = {"time": "1/2/2018", 
            "author": "Test Author"}  # Optional json containing additional document metadata

try:
    api_response = api_instance.post_upload_file(file, dataset)
    print(api_response.result, 'has been added to dataset', dataset)
    #print('api_response=', api_response)   # raw API response    
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_file: %s\n" % e)

print('-------------------------------------------------------------')


# # Append all PDFs from a folder to dataset in parallel

# In[3]:


print('--------- Append all files from local folder to dataset -----------')
folder = 'fomc-minutes'         

dataset = 'dataset_test'              # str | Destination dataset where the file will be inserted.

for root, dirs, files in os.walk(folder):
    file_iters = []
    for file in files:
        if Path(file).suffix == '.pdf':
            file_iters.append(os.path.join(root, file))
        
    nucleus_helper.import_files(api_instance, dataset, file_iters, processes=4)

print('-------------------------------------------------------------')


# ## Append file from URL to dataset

# In[4]:


print('------------ Append file from URL to dataset ---------------')

dataset = 'dataset_test'
file_url = 'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109a.docx'
# Optional filename saved on the server for the URL. If not specified, Nucleus will make
# an intelligent guess from the file URL
filename = 'quarles20181109a-newname.pdf'  
payload = nucleus_api.UploadURLModel(
                dataset=dataset,
                file_url=file_url,
                filename=filename  
            ) # UploadURLModel | 

try:
    api_response = api_instance.post_upload_url(payload)
    #print('api_response=', api_response)   # raw API response
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_url: %s\n" % e)
    
print(api_response.result, 'has been added to dataset', dataset)
print('-------------------------------------------------------------')


# ## Append files from URLs to dataset in parallel

# In[5]:


print('------------ Append file from URL to dataset ---------------')

dataset = 'dataset_test'
file_urls = [
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109a.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109b.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109c.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109d.docx'
]

nucleus_helper.import_urls(api_instance, dataset, file_urls, processes=4)
    

print('-------------------------------------------------------------')


# ## Append jsons from csv to dataset in parallel

# In[6]:


# This dataset will be used to test all topics and documents APIs
print('----------- Append json from CSV to dataset -----------------')
csv_file = 'trump-tweets-100.csv'
dataset = 'trump_tweets'

with open(csv_file, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    #print(list(reader))
    nucleus_helper.import_jsons(api_instance, dataset, reader, processes=1)

print('-------------------------------------------------------------')


# ## List available datasets

# In[7]:


print('---------------- List available datasets ---------------------')
try:
    api_response = api_instance.get_list_datasets()
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)

list_datasets = api_response.result

print(len(list_datasets), 'datasets in the database:')
for ds in list_datasets:
    print('    ', ds)

    
print('-------------------------------------------------------------')


# ## Get dataset information

# In[8]:


print('--------------- Get dataset information -------------------')
dataset = 'dataset_test' # str | Dataset name.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. (optional)
metadata_selection = '' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = '' # str | Time period selection (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"

try:
    payload = nucleus_api.DatasetInfo(dataset=dataset, 
                                    query=query, 
                                    metadata_selection=metadata_selection, 
                                    time_period=time_period)
    api_response = api_instance.post_dataset_info(payload)
    #print('api_response=', api_response) # raw API response
except ApiException as e:
    print("Exception when calling DatasetsApi->post_dataset_info: %s\n" % e)

print('Information about dataset', dataset)
print('    Language:', api_response.result.detected_language)
print('    Number of documents:', api_response.result.num_documents)
print('    Time range:', datetime.datetime.fromtimestamp(float(api_response.result.time_range[0])),
             'to', datetime.datetime.fromtimestamp(float(api_response.result.time_range[1])))


print('-------------------------------------------------------------')


# ## Delete document

# In[9]:


print('--------------------- Delete document -----------------------')
dataset = 'dataset_test'

docid = '1'
payload = nucleus_api.Deletedocumentmodel(dataset=dataset,
                                             docid=docid) # Deletedocumentmodel | 

try:
    api_response = api_instance.post_delete_document(payload)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_delete_document: %s\n" % e)


print('Document', docid, 'from dataset', dataset, 'has been deleted.')
# print(api_response)     # raw API response
print('-------------------------------------------------------------')


# ## Delete dataset

# In[10]:


print('--------------------- Delete dataset ------------------------')

dataset = 'dataset_test'  
payload = nucleus_api.Deletedatasetmodel(dataset=dataset) # Deletedatasetmodel | 


try:
    api_response = api_instance.post_delete_dataset(payload)
    #print(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_delete_dataset: %s\n" % e)
    
# List datasets again to check if the specified dataset has been deleted
try:
    api_response = api_instance.get_list_datasets()
    print('api_response=', api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)
    
print('-------------------------------------------------------------')


# # Topic APIs

# ## Get list of topics from dataset

# In[11]:


print('------------- Get list of topics from dataset --------------')
dataset = 'trump_tweets'
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = ""     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)

try:
    payload = nucleus_api.Topics(dataset=dataset,                                
                                query=query,                   
                                custom_stop_words=custom_stop_words,     
                                num_topics=num_topics,
                                metadata_selection=metadata_selection,
                                time_period=time_period)
    api_response = api_instance.post_topic_api(payload)        
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_api: %s\n" % e)
    
#print(api_response)
i = 1
for res in api_response.result:
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.topic)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposure
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposure)):
        doc_topic_exp = float(res.doc_topic_exposure[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(res.doc_id[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')
    i = i + 1
    
print('-------------------------------------------------------------')


# ## Get list of topics from dataset with a time range selection

# In[12]:


print('------------- Get list of topics from dataset --------------')
dataset = 'trump_tweets'
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_start = "2016-10-15 04:30:00" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "2019-01-01 12:00:05" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"

try:
    payload = nucleus_api.Topics(dataset=dataset,                                
                                query=query,                   
                                custom_stop_words=custom_stop_words,     
                                num_topics=num_topics,
                                metadata_selection=metadata_selection,
                                period_start=period_start,
                                period_end=period_end)
    api_response = api_instance.post_topic_api(payload)        
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_api: %s\n" % e)
    
#print(api_response)
i = 1
for res in api_response.result:
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.topic)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposure
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposure)):
        doc_topic_exp = float(res.doc_topic_exposure[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(res.doc_id[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')
    i = i + 1
    
print('-------------------------------------------------------------')


# ## Get list of topics from dataset with a metadata selection

# In[13]:


print('------------- Get list of topics from dataset --------------')
dataset = 'trump_tweets'
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection = {"author": "D_Trump16"} # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)

try:
    payload = nucleus_api.Topics(dataset=dataset,                                
                                query=query,                   
                                custom_stop_words=custom_stop_words,     
                                num_topics=num_topics,
                                metadata_selection=metadata_selection)
    api_response = api_instance.post_topic_api(payload)        
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_api: %s\n" % e)
    
#print(api_response)
i = 1
for res in api_response.result:
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.topic)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposure
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposure)):
        doc_topic_exp = float(res.doc_topic_exposure[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(res.doc_id[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')
    i = i + 1
    
print('-------------------------------------------------------------')


# ## Get topic summary

# In[14]:


print('------------------- Get topic summary -----------------------')
dataset = 'trump_tweets' # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in each topic summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
num_docs = 20 # int | The maximum number of key documents to use for summarization. (optional) (default to 20)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = ""     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""]  (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
api_response = None

try:
    payload = nucleus_api.TopicSummaryModel	(
        dataset=dataset, 
        query=query,
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        metadata_selection=metadata_selection,
        summary_length=summary_length, 
        context_amount=context_amount, 
        num_docs=num_docs)
    api_response = api_instance.post_topic_summary_api(payload)        
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_summary_api: %s\n" % e)

#pprint(api_response)  # raw API response
if api_response != None:
    i = 1
    for res in api_response.result:
        print('Topic', i, 'summary:')
        print('    Keywords:', res.topic)
        for j in range(len(res.summary)):
            print(res.summary[j])
            print('    Document ID:', res.summary[j].sourceid)
            print('        Title:', res.summary[j].title)
            print('        Sentences:', res.summary[j].sentences)
            print('        Author:', res.summary[j].attribute['author'])
            print('        Time:', datetime.datetime.fromtimestamp(float(res.summary[j].attribute['time'])))
        
        print('---------------')
        i = i + 1
    
print('-------------------------------------------------------------')


# ## Get topic sentiment

# In[15]:


print('---------------- Get topic sentiment ------------------------')
dataset = 'trump_tweets' # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {"great": 1.0, "awful": -1.0, "clinton":-1.0, "trump":1.0} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = ""     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"

try:
    payload = nucleus_api.TopicSentimentModel(
        dataset=dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        custom_dict_file=custom_dict_file)
    api_response = api_instance.post_topic_sentiment_api(payload)
    
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_sentiment_api: %s\n" % e)

i = 1
for res in api_response.result:
    print('Topic', i, 'sentiment:')
    print('    Keywords:', res.topic)
    print('    Sentiment:', res.sentiment)
    print('    Strength:', res.strength)
    
    doc_id_str = ' '.join(str(x) for x in res.doc_id)
    doc_sentiment_str = ' '.join(str(x) for x in res.doc_sentiment)
    doc_score_str = ' '.join(str(x) for x in res.doc_score)
    print('    Document IDs:', doc_id_str)
    print('    Document Sentiments:', doc_sentiment_str)
    print('    Document Scores:', doc_score_str)
    
    print('---------------')
    i = i + 1
    
#pprint(api_response)
print('-------------------------------------------------------------')


# ## Get topic consensus

# In[16]:


print('---------------- Get topic consensus ------------------------')
dataset = 'trump_tweets' # str | Dataset name.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {"great": 1.0, "awful": -1.0, "clinton":-1.0, "trump":1.0} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = ""     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"

try:
    payload = nucleus_api.TopicConsensusModel(
        dataset=dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        custom_dict_file=custom_dict_file)
    api_response = api_instance.post_topic_consensus_api(payload)
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_consensus_api: %s\n" % e)
    
i = 1
for res in api_response.result:
    print('Topic', i, 'consensus:')
    print('    Keywords:', res.topic)
    print('    Consensus:', res.consensus)
    print('    Strength:', res.strength)
    
    print('---------------')
    i = i + 1
    
#pprint(api_response) # raw API response
print('-------------------------------------------------------------')


# ## Get topic historical analysis

# In[17]:


print('------------ Get topic historical analysis ----------------')

dataset = 'trump_tweets'   # str | Dataset name.
update_period = 'd' # str | Frequency at which the historical anlaysis is performed. choices=["d","m","H","M"] (default to d)
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
inc_step = 1 # int | Number of increments of the udpate period in between two historical computations. (optional) (default to 1)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = "6M"     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
api_response = None
try:
    payload = nucleus_api.TopicHistoryModel(
        dataset=dataset, 
        time_period=time_period, 
        update_period=update_period, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords, 
        metadata_selection=metadata_selection, 
        inc_step=inc_step, 
        excluded_docs=excluded_docs,
        custom_dict_file=custom_dict_file)
    api_response = api_instance.post_topic_historical_analysis_api(payload)
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_historical_analysis_api: %s\n" % e)

if api_response != None:
    #print('api_response=', api_response)
    results = api_response.result

    # chart the historical metrics when running in Jupyter Notebook
    if running_notebook:
        print('Plotting historical metrics data...')
        historical_metrics = []
        for res in results:
            # conctruct a list of historical metrics dictionaries for charting
            historical_metrics.append({
                'topic'    : res.topic,
                'time_stamps' : np.array(res.time_stamps),
                'strength' : np.array(res.strength, dtype=np.float32),
                'consensus': np.array(res.consensus, dtype=np.float32), 
                'sentiment': np.array(res.sentiment, dtype=np.float32)})

        selected_topics = range(len(historical_metrics)) 
        topic_charts_historical(historical_metrics, selected_topics, True)
    else:
        print('Printing historical metrics data...')
        print('NOTE: historical metrics data can be plotted when running the example in Jupyter Notebook')
        i = 1
        for res in results:
            print('Topic', i, res.topic)
            print('    Timestamps:', res.time_stamps)
            print('    Strength:', res.strength)
            print('    Consensus:', res.consensus)
            print('    Sentiment:', res.sentiment)
            print('----------------')
            i = i + 1

print('-------------------------------------------------------------')


# ## Get author connectivity

# In[18]:


print('----------------- Get author connectivity -------------------')
dataset = dataset # str | Dataset name.
target_author = 'D_Trump16' # str | Name of the author to be analyzed.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of words possibly used by the target author that are considered not information-bearing. (optional)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = "12M"     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)
period_start = "" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"
period_end = "" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD HH:MM:SS"

try:
    payload = nucleus_api.AuthorConnection(dataset=dataset, 
                                            target_author=target_author, 
                                            query=query, 
                                            custom_stop_words=custom_stop_words, 
                                            time_period=time_period, 
                                            metadata_selection=metadata_selection, 
                                            excluded_docs=excluded_docs)
    api_response = api_instance.post_author_connectivity_api(payload)    
except ApiException as e:
    print("Exception when calling TopicsApi->post_author_connectivity_api: %s\n" % e)

res = api_response.result
print('Mainstream connections:')
for mc in res.mainstream_connection:
    print('    Topic:', mc.topic)
    print('    Authors:', " ".join(str(x) for x in mc.authors))
    
print('Niche connections:')
for nc in res.niche_connection:
    print('    Topic:', nc.topic)
    print('    Authors:', " ".join(str(x) for x in nc.authors))  
    
#pprint(api_response)   # raw API response
print('-------------------------------------------------------------')


# # Get topic delta

# In[19]:


print('------------------- Get topic deltas -----------------------')
dataset = 'trump_tweets' 
#dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = [""] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_0_start = '2018-08-12 00:00:00'
period_0_end = '2018-08-15 13:00:00'
period_1_start = '2018-08-16 00:00:00'
period_1_end = '2018-08-19 00:00:00'
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.TopicDeltaModel(
        dataset=dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        period_0_start=period_0_start,
        period_0_end=period_0_end,
        period_1_start=period_1_start,
        period_1_end=period_1_end,
        metadata_selection=metadata_selection)
    api_response = api_instance.post_topic_delta_api(payload)        
except ApiException as e:
    print("Exception when calling TopicsApi->post_topic_delta_api: %s\n" % e)

i = 1
for res in api_response.result:
    print('Topic', i, 'changes in exposure:')
    print('    Keywords:', res.topic)
    print('    Document ID:', res.doc_id_t0, res.doc_id_t1)
    print('    Per Source Change in Exposure:', res.doc_topic_exposure_delta)
    print('---------------')
    i = i + 1
    
    
#pprint(api_response)  # raw API response
print('-------------------------------------------------------------')


# # Document APIs

# ## Get document information without content

# In[20]:


dataset = 'trump_tweets' # str | Dataset name.
doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the documents to retrieve. Example: ["title1", "title2", ..., "titleN"]  (optional)
doc_ids = ['3397215194896514820', '776902852041351634']      # str | The docid of the documents to retrieve. Example: ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.DocInfo(
        dataset=dataset, 
        doc_titles=doc_titles, 
        doc_ids=doc_ids,
        metadata_selection='')
    api_response = api_instance.post_doc_info(payload)
except ApiException as e:
    print("Exception when calling post_doc_info: %s\n" % e)
    
for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))

    print('---------------')
    
    
#pprint(api_response)  # raw response from API server
print('-------------------------------------------------------------')


# ## Display document info with a metadata selection

# In[21]:


dataset = 'trump_tweets' # str | Dataset name.
metadata_selection = {"author": "D_Trump16"}      # dict | A selector off metadata. Example: {"field": "value"}  (optional)

try:
    payload = nucleus_api.DocInfo(dataset=dataset, metadata_selection=metadata_selection)
    api_response = api_instance.post_doc_info(payload)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_info_api: %s\n" % e)

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))

    print('---------------')


#pprint(api_response) # raw response from API server
print('-------------------------------------------------------------')


# ## Display document details

# In[22]:


dataset = 'trump_tweets' # str | Dataset name.
#doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the documents to retrieve. Example: ["title1", "title2", ..., "titleN"]  (optional)
doc_ids = ['776902852041351634']      # str | The docid of the documents to retrieve. Example: ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.DocDisplay(dataset, doc_ids=doc_ids)
    api_response = api_instance.post_doc_display(payload)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_display_api: %s\n" % e)

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))
    print('    Content', res.content)

    print('---------------')


#pprint(api_response) # raw response from API server
print('-------------------------------------------------------------')


# ## Display document details with a metadata selection

# In[23]:


dataset = 'trump_tweets' # str | Dataset name.
metadata_selection = {"author": "D_Trump16"}      # dict | A selector off metadata. Example: {"field": "value"}  (optional)

try:
    payload = nucleus_api.DocDisplay(dataset=dataset, metadata_selection=metadata_selection)
    api_response = api_instance.post_doc_display(payload)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_display_api: %s\n" % e)

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))
    print('    Content', res.content)

    print('---------------')


#pprint(api_response) # raw response from API server
print('-------------------------------------------------------------')


# ## Get document recommendations

# In[24]:


print('------------- Get document recommendations -----------------')

dataset = 'trump_tweets' # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.DocumentRecommendModel(
        dataset=dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords)
    api_response = api_instance.post_doc_recommend_api(payload)
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_recommend_api: %s\n" % e)
    
i = 1
for res in api_response.result:
    print('Document recommendations for topic', i, ':')
    print('    Keywords:', res.topic)

    j = 1
    for doc in res.recommendations:
        print('    Recommendation', j, ':')
        print('        Document ID:', doc.sourceid)
        print('        Title:', doc.title)
        print('        Attribute:', doc.attribute)
        print('        Author:', doc.attribute['author'])
        print('        Time:', datetime.datetime.fromtimestamp(float(doc.attribute['time'])))
        j = j + 1
    
    print('---------------')
    i = i + 1
    
#pprint(api_response)   # raw API response
print('-------------------------------------------------------------')


# ## Get document summary

# In[25]:


print('------------------ Get document summary  --------------------')

dataset = 'trump_tweets' # str | Dataset name.
doc_title = 'D_Trump2018_8_17_14_10' # str | The title of the document to be summarized.
custom_stop_words = ["real","hillary"] # List of stop words. (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
short_sentence_length = 0 # int | The sentence length below which a sentence is excluded from summarization (optional) (default to 4)
long_sentence_length = 40 # int | The sentence length beyond which a sentence is excluded from summarization (optional) (default to 40)

try:
    payload = nucleus_api.DocumentSummaryModel(
        dataset=dataset, 
        doc_title=doc_title, 
        custom_stop_words=custom_stop_words, 
        summary_length=summary_length, 
        context_amount=context_amount,
        short_sentence_length=short_sentence_length,
        long_sentence_length=long_sentence_length)
    api_response = api_instance.post_doc_summary_api(payload)
    
    print('Summary for', api_response.result.doc_title)
    for sent in api_response.result.summary.sentences:
        print('    *', sent)

    #pprint(api_response)   # raw API response
    
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_summary_api: %s\n" % e)


print('-------------------------------------------------------------')


# # Summarize file from URL 

# In[26]:


######################################################################################
# file_params fields descriptions:  
#   file_url              : string, the URL at which the file is stored (could be a S3 bucket address for instance)
#   filename              : OPTIONAL string, filename saved on the server. also serves as the doc_title for summarization
#   custom_stop_words     : OPTIONAL a string list, user-provided list of stopwords to be excluded from the content analysis leading to document summarization
#                            ["word1", "word2", ...]. DEFAULT: empty
#   summary_length        : OPTIONAL an integer, the maximum number of bullet points a user wants to see in the document summary. DEFAULT: 6
#   context_amount        : OPTIONAL an integer, the number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. DEFAULT: 0
#   short_sentence_length : OPTIONAL an integer, the sentence length below which a sentence is excluded from summarization. DEFAULT: 4 words
#   long_sentence_length  : OPTIONAL an integer, the sentence length beyond which a sentence is excluded from summarization. DEFAULT: 40 words
#
file_params = {
    'file_url': 'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109a.docx',
    'filename': 'quarles20181109a-newname.pdf',   
    'custom_stop_words': ["document", "sometimes"], 
    'summary_length': 6,
    'context_amount': 0, 
    'short_sentence_length': 4, 
    'long_sentence_length': 40}


result = nucleus_helper.summarize_file_url(api_instance, file_params)

#print(result)   
print('Summary for', result.doc_title, ':')
for sent in result.summary.sentences:
    print('    *', sent)

print('-------------------------------------------------------------')


# ## Get document sentiment

# In[27]:


print('------------------ Get document sentiment  --------------------')

dataset = 'trump_tweets' # str | Dataset name.
doc_title = 'D_Trump2018_8_17_14_10' # str | The title of the document to be analyzed.
custom_stop_words = ["real","hillary"] # List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the document. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the document. (optional) (default to 8)

try:
    payload = nucleus_api.DocumentSentimentModel(
        dataset=dataset, 
        doc_title=doc_title, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords)
    api_response = api_instance.post_doc_sentiment_api(payload)
    
    print('Sentiment for', api_response.result.doc_title)
    print(api_response.result.sentiment)

    #pprint(api_response)   # raw API response
    
except ApiException as e:
    print("Exception when calling DocumentsApi->post_doc_sentiment_api: %s\n" % e)


print('-------------------------------------------------------------')


# In[ ]:




