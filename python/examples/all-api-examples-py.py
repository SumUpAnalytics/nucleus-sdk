#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2018-2019 SumUp Analytics, Inc. All Rights Reserved.
# 
# NOTICE: All information contained herein is, and remains the property of SumUp Analytics Inc. and its suppliers, if any. The intellectual and technical concepts contained herein are proprietary to SumUp Analytics Inc. and its suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.
# 
# Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from SumUp Analytics Inc.

# # Initialization, configure API host and key, and create new API instance

# In[ ]:


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

# In[ ]:


print('--------- Append file from local drive to dataset -----------')
dataset = "dataset_test"
file = 'quarles20181109a.pdf'         # file | 
metadata = {"time": "1/2/2018", 
            "author": "Test Author"}  # Optional json containing additional document metadata

try:
    api_response = api_instance.post_upload_file(file, dataset, metadata=metadata)
    fp = api_response.result
    print(fp.filename, '(', fp.size, 'bytes) has been added to dataset', dataset,)    
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

print('-------------------------------------------------------------')


# # Append all PDFs from a folder to dataset in parallel

# In[ ]:


folder = 'fomc-minutes'         
dataset = 'dataset_test'# str | Destination dataset where the file will be inserted.
print('--------- Append all files from local folder {} to dataset {} in parallel -----------'.format(folder, dataset))

# build file iterable. Each item in the iterable is in the format below:
# {'filename': filename,   # filename to be uploaded. REQUIRED
#  'metadata': {           # metadata for the file. Optional
#      'key1': val1,       # keys can have arbiturary names as long as the names only
#      'key2': val2        # contain alphanumeric (0-9|a-z|A-Z) and underscore (_)
#   } 
# }
file_iter = []
for root, dirs, files in os.walk(folder):
    for file in files:
        if Path(file).suffix == '.pdf':
            file_dict = {'filename': os.path.join(root, file),
                         'metadata': {'field1': 'financial'}}
            file_iter.append(file_dict)

file_props = nucleus_helper.upload_files(api_instance, dataset, file_iter, processes=1)
for fp in file_props:
    print(fp.filename, '(', fp.size, 'bytes) has been added to dataset', dataset)
    
print('-------------------------------------------------------------')


# ## Append file from URL to dataset

# In[ ]:


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
    url_prop = api_response.result
    print(url_prop.file_url, '(', url_prop.size, ' bytes) has been added to dataset', dataset)

except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
print('-------------------------------------------------------------')


# ## Append files from URLs to dataset in parallel

# In[ ]:


print('------------ Append file from URL to dataset ---------------')

dataset = 'dataset_test'
file_urls = [
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109a.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109b.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109c.docx',
    'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109d.docx'
]

url_props = nucleus_helper.upload_urls(api_instance, dataset, file_urls, processes=1)

for up in url_props:
    print(up.file_url, '(', up.size, ' bytes) has been added to dataset', dataset)
    
print('-------------------------------------------------------------')


# ## Append JSON to dataset

# In[ ]:


dataset = 'dataset_test'
print('----------- Append json from to dataset {}-----------------'.format(dataset))

document = {
    "title": "This a test json title field",
    "time": "2019-01-01",
    "content": "This is a test json content field"
}

payload = nucleus_api.Appendjsonparams(dataset=dataset,
                                       document=document)

try:
    api_response = api_instance.post_append_json_to_dataset(payload)
    print(api_response.result)
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])


# ## Append jsons from csv to dataset in parallel

# In[ ]:


# This dataset will be used to test all topics and documents APIs
csv_file = 'trump-tweets-100.csv'
dataset = 'trump_tweets1'
print('----------- Append json from CSV {} to dataset {}-----------------'.format(csv_file, dataset))

with open(csv_file, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    json_props = nucleus_helper.upload_jsons(api_instance, dataset, reader, processes=1)
    
    total_size = 0
    total_jsons = 0
    for jp in json_props:
        total_size += jp.size
        total_jsons += 1
        
    print(total_jsons, 'JSON records (', total_size, 'bytes) appended to', dataset)

print('-------------------------------------------------------------')


# ## List available datasets

# In[ ]:


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

# In[ ]:


dataset = 'dataset_test' # str | Dataset name.
print('--------------- Get dataset information from {}-------------------'.format(dataset))

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
    print('Information about dataset', dataset)
    print('    Language:', api_response.result.detected_language)
    print('    Number of documents:', api_response.result.num_documents)
    print('    Time range:', datetime.datetime.fromtimestamp(float(api_response.result.time_range[0])),
             'to', datetime.datetime.fromtimestamp(float(api_response.result.time_range[1])))
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

print('-------------------------------------------------------------')


# ## Delete document

# In[ ]:


#print('--------------------- Delete document -----------------------')
#dataset = 'dataset_test'

#docid = '1'
#payload = nucleus_api.Deletedocumentmodel(dataset=dataset,
#                                          docid=docid) # Deletedocumentmodel | 

#try:
#    api_response = api_instance.post_delete_document(payload)
#except ApiException as e:
#    print("Exception when calling DatasetsApi->post_delete_document: %s\n" % e)


#print('Document', docid, 'from dataset', dataset, 'has been deleted.')
## print(api_response)     # raw API response
#print('-------------------------------------------------------------')


# ## Delete dataset

# In[ ]:


print('--------------------- Delete dataset ------------------------')

dataset = 'dataset_test'
payload = nucleus_api.Deletedatasetmodel(dataset=dataset) # Deletedatasetmodel | 

try:
    api_response = api_instance.post_delete_dataset(payload)
    print(api_response.result['result'])
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
# List datasets again to check if the specified dataset has been deleted
try:
    api_response = api_instance.get_list_datasets()
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
print('-------------------------------------------------------------')


# # Topic APIs

# ## Get list of topics from dataset

# In[ ]:


dataset = 'trump_tweets'
print('------------- Get list of topics from dataset {}--------------'.format(dataset))

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

doc_ids = api_response.result.doc_ids
topics = api_response.result.topics
for i, res in enumerate(topics):
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.keywords)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposures
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposures)):
        doc_topic_exp = float(res.doc_topic_exposures[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(doc_ids[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')
    
print('-------------------------------------------------------------')


# ## Get list of topics from dataset with a time range selection

# In[ ]:


dataset = 'trump_tweets'
print('------------- Get list of topics from dataset {}--------------'.format(dataset))

#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_start = "2016-10-15" # str | Start date for the period to analyze within the dataset. Format: "YYYY-MM-DD"
period_end = "2019-01-01" # str | End date for the period to analyze within the dataset. Format: "YYYY-MM-DD"

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
doc_ids = api_response.result.doc_ids
topics = api_response.result.topics
for i, res in enumerate(topics):
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.keywords)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposure
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposures)):
        doc_topic_exp = float(res.doc_topic_exposures[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(doc_ids[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')

print('-------------------------------------------------------------')


# ## Get list of topics from dataset with a metadata selection

# In[ ]:


dataset = 'trump_tweets'
print('------------- Get list of topics from dataset {}--------------'.format(dataset))

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
doc_ids = api_response.result.doc_ids
topics = api_response.result.topics
for i, res in enumerate(topics):
    print('Topic', i, 'keywords:')
    print('    Keywords:', res.keywords)
    keywords_weight_str = ";".join(str(x) for x in res.keywords_weight)
    print('    Keyword weights:', keywords_weight_str)
    print('    Strength:', res.strength)
    doc_topic_exposure_sel = []  # list of non-zero doc_topic_exposure
    doc_id_sel = []        # list of doc ids matching doc_topic_exposure_sel
    for j in range(len(res.doc_topic_exposures)):
        doc_topic_exp = float(res.doc_topic_exposures[j])
        if doc_topic_exp != 0:
            doc_topic_exposure_sel.append(doc_topic_exp)
            doc_id_sel.append(doc_ids[j])
    
    doc_id_sel_str = ' '.join(str(x) for x in doc_id_sel)
    doc_topic_exposure_sel_str = ' '.join(str(x) for x in doc_topic_exposure_sel)
    print('    Document IDs:', doc_id_sel_str)
    print('    Document exposures:', doc_topic_exposure_sel_str)

    print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic summary

# In[ ]:


dataset = 'trump_tweets'
print('------------------- Get topic summary for {} -----------------------'.format(dataset))
 # str | Dataset name.
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
    api_ok = True
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    api_ok = False

if api_ok:
    for i,res in enumerate(api_response.result):
        print('Topic', i, 'summary:')
        print('    Keywords:', res.keywords)
        for j in range(len(res.summary)):
            print(res.summary[j])
            print('    Document ID:', res.summary[j].sourceid)
            print('        Title:', res.summary[j].title)
            print('        Sentences:', res.summary[j].sentences)
            print('        Author:', res.summary[j].attribute['author'])
            print('        Time:', datetime.datetime.fromtimestamp(float(res.summary[j].attribute['time'])))

        print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic sentiment

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name
print('---------------- Get topic sentiment for {} ------------------------'.format(dataset))

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

for i,res in enumerate(api_response.result):
    print('Topic', i, 'sentiment:')
    print('    Keywords:', res.keywords)
    print('    Sentiment:', res.sentiment)
    print('    Strength:', res.strength)
    
    doc_id_str = ' '.join(str(x) for x in res.doc_ids)
    doc_sentiment_str = ' '.join(str(x) for x in res.doc_sentiments)
    doc_score_str = ' '.join(str(x) for x in res.doc_topic_exposures)
    print('    Document IDs:', doc_id_str)
    print('    Document Sentiments:', doc_sentiment_str)
    print('    Document Exposures:', doc_score_str)
    
    print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic consensus

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('---------------- Get topic consensus for {} ------------------------'.format(dataset))

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
for i, res in enumerate(api_response.result):
    print('Topic', i, 'consensus:')
    print('    Keywords:', res.keywords)
    print('    Consensus:', res.consensus)
    print('    Strength:', res.strength)
    
    print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic historical analysis

# In[ ]:


dataset = 'trump_tweets'   # str | Dataset name.
print('------------ Get topic historical analysis for {} ----------------'.format(dataset))

update_period = 'm' # str | Frequency at which the historical anlaysis is performed. choices=["d","m","H","M"] (default to d)
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
inc_step = 1 # int | Number of increments of the udpate period in between two historical computations. (optional) (default to 1)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
time_period = "12M"     # str | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""] (optional)
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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    print(e)

print('Printing historical metrics data...')
print('NOTE: historical metrics data can be plotted when running the example in Jupyter Notebook')

for i,res in enumerate(api_response.result):
    print('Topic', i, res.keywords)
    print('    Timestamps:', res.time_stamps)
    print('    Strengths:', res.strengths)
    print('    Consensuses:', res.consensuses)
    print('    Sentiments:', res.sentiments)
    print('----------------')
            

# chart the historical metrics when running in Jupyter Notebook
if running_notebook:
    print('Plotting historical metrics data...')
    historical_metrics = []
    for res in api_response.result:
        # construct a list of historical metrics dictionaries for charting
        historical_metrics.append({
            'topic'    : res.keywords,
            'time_stamps' : np.array(res.time_stamps),
            'strength' : np.array(res.strengths, dtype=np.float32),
            'consensus': np.array(res.consensuses, dtype=np.float32), 
            'sentiment': np.array(res.sentiments, dtype=np.float32)})

    selected_topics = range(len(historical_metrics)) 
    #nucleus_helper.topic_charts_historical(historical_metrics, selected_topics, True)

print('-------------------------------------------------------------')


# ## Get author connectivity

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('----------------- Get author connectivity for {} -------------------'.format(dataset))

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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

res = api_response.result
print('Mainstream connections:')
for mc in res.mainstream_connections:
    print('    Keywords:', mc.keywords)
    print('    Authors:', " ".join(str(x) for x in mc.authors))
    
print('Niche connections:')
for nc in res.niche_connections:
    print('    Keywords:', nc.keywords)
    print('    Authors:', " ".join(str(x) for x in nc.authors))  
    
print('-------------------------------------------------------------')


# ## Get topic transfer

# In[ ]:


dataset0 = 'trump_tweets'
print('------------------- Get topic transfer for {} -----------------------'.format(dataset))

dataset1 = None # str | Validation dataset (optional if period_0 and period_1 dates provided)
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = [""] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_0_start = '2018-08-12' # Not needed if you provide a validation dataset in the "dataset1" variable 
period_0_end = '2018-08-16' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_start = '2018-08-14' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_end = '2018-08-18' # Not needed if you provide a validation dataset in the "dataset1" variable
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.TopicTransferModel(dataset0=dataset0,
                                             dataset1=dataset1,
                                             query=query, 
                                             custom_stop_words=custom_stop_words, 
                                             num_topics=num_topics, 
                                             num_keywords=num_keywords,
                                             period_0_start=period_0_start,
                                             period_0_end=period_0_end,
                                             period_1_start=period_1_start,
                                             period_1_end=period_1_end,
                                             metadata_selection=metadata_selection)
    api_response = api_instance.post_topic_transfer_api(payload)
    api_ok = True
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    api_ok = False

if api_ok:
    doc_ids_t1 = api_response.result.doc_ids_t1
    topics = api_response.result.topics
    for i,res in enumerate(topics):
        print('Topic', i, 'exposure within validation dataset:')
        print('    Keywords:', res.keywords)
        print('    Strength:', res.strength)
        print('    Document IDs:', doc_ids_t1)
        print('    Exposure per Doc in Validation Dataset:', res.doc_topic_exposures_t1)
        print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic sentiment transfer

# In[ ]:


dataset0 = 'trump_tweets'
dataset1 = None
print('------------------- Get topic sentiment transfer for {} -----------------------'.format(dataset))

#dataset1 = dataset # str | Validation dataset (optional if period_0 and period_1 dates provided)
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = [""] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_0_start = '2018-08-12' # Not needed if you provide a validation dataset in the "dataset1" variable 
period_0_end = '2018-08-16' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_start = '2018-08-14' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_end = '2018-08-18' # Not needed if you provide a validation dataset in the "dataset1" variable
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {"great": 1.0, "awful": -1.0, "clinton":-1.0, "trump":1.0} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

try:
    payload = nucleus_api.TopicSentimentTransferModel(
        dataset0=dataset0, 
        dataset1=dataset1,
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        period_0_start=period_0_start,
        period_0_end=period_0_end,
        period_1_start=period_1_start,
        period_1_end=period_1_end,
        metadata_selection=metadata_selection,
        custom_dict_file=custom_dict_file)
    api_response = api_instance.post_topic_sentiment_transfer_api(payload)
    api_ok = True
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    api_ok = False

if api_ok:
    topics = api_response.result
    for i,res in enumerate(topics):
        print('Topic', i, 'exposure within validation dataset:')
        print('    Keywords:', res.keywords)
        print('    Strength:', res.strength)
        print('    Sentiment:', res.sentiment)
        print('    Document IDs:', res.doc_ids_t1)
        print('    Sentiment per Doc in Validation Dataset:', res.doc_sentiments_t1)
        print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic consensus transfer

# In[ ]:


dataset0 = 'trump_tweets'
print('------------------- Get topic consensus transfer for {} -----------------------'.format(dataset))

dataset1 = None # str | Validation dataset (optional if period_0 and period_1 dates provided)
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = [""] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = "" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_0_start = '2018-08-12' # Not needed if you provide a validation dataset in the "dataset1" variable 
period_0_end = '2018-08-16' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_start = '2018-08-14' # Not needed if you provide a validation dataset in the "dataset1" variable
period_1_end = '2019-08-18' # Not needed if you provide a validation dataset in the "dataset1" variable
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)
custom_dict_file = {"great": 1.0, "awful": -1.0, "clinton":-1.0, "trump":1.0} # file | Custom sentiment dictionary JSON file. Example, {"field1": value1, ..., "fieldN": valueN} (optional)

try:
    payload = nucleus_api.TopicConsensusTransferModel(
        dataset0=dataset0,
        dataset1=dataset1,
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        period_0_start=period_0_start,
        period_0_end=period_0_end,
        period_1_start=period_1_start,
        period_1_end=period_1_end,
        metadata_selection=metadata_selection,
        custom_dict_file=custom_dict_file)
    api_response = api_instance.post_topic_consensus_transfer_api(payload)
    api_ok = True
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    api_ok = False

if api_ok:
    topics = api_response.result
    for i,res in enumerate(topics):
        print('Topic', i, 'exposure within validation dataset:')
        print('    Keywords:', res.keywords)
        print('    Consensus:', res.consensus)
        print('---------------')
    
print('-------------------------------------------------------------')


# ## Get topic delta

# In[ ]:


dataset = 'trump_tweets'
print('------------------- Get topic deltas for {} -----------------------'.format(dataset))
 
#dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = [""] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection ="" # dict | JSON object specifying metadata-based queries on the dataset, of type {"metadata_field": "selected_values"} (optional)
period_0_start = '2018-08-12'
period_0_end = '2018-08-15'
period_1_start = '2018-08-16'
period_1_end = '2018-08-19'
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
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

doc_ids_t0 = api_response.result.doc_ids_t0
doc_ids_t1 = api_response.result.doc_ids_t1
topics = api_response.result.topics
for i,res in enumerate(topics):
    print('Topic', i, 'changes in exposure:')
    print('    Keywords:', res.keywords)
    print('    Document ID:', doc_ids_t0, doc_ids_t1)
    print('    Per Source Change in Exposure:', res.doc_topic_exposure_deltas)
    print('---------------')
    
print('-------------------------------------------------------------')


# # Document APIs

# ## Get document information without content

# In[ ]:


dataset = 'trump_tweets'
print('------------------- Get document information for {} -----------------------'.format(dataset))
# doc_titles, doc_ids, and metadata_selection below are filters to narrow down 
# documents to be retrieved.
# The information of all documents will be retrived when no filters are provided.

# doc_titles: list of strings
# The titles of the documents to retrieve. Example: ["title1", "title2", ..., "titleN"]  (optional)
# doc_titles = ['D_Trump2018_8_18_1_47']   
doc_titles = []
# doc_ids: list of strings
# The docid of the documents to retrieve. Example: ["docid1", "docid2", ..., "docidN"]  (optional)
# doc_ids = ['3397215194896514820', '776902852041351634']
doc_ids = []

# metadata_selection = {"author": "D_Trump16"} # dict | A selector off metadata. Example: {"field": "value"}  (optional)
metadata_selection = ''

try:
    payload = nucleus_api.DocInfo(dataset=dataset, 
                                doc_titles=doc_titles, 
                                doc_ids=doc_ids,
                                metadata_selection=metadata_selection)
    api_response = api_instance.post_doc_info(payload)
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    title:', res.title)
    for attr in res.attribute.keys():
        if attr == 'time':
            print('   ', attr, ':', datetime.datetime.fromtimestamp(float(res.attribute[attr])))
        else:
            print('   ', attr, ':', res.attribute[attr])

    print('---------------')

print('-------------------------------------------------------------')


# ## Display document info with a metadata selection

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('------------------- Get document information for {} -----------------------'.format(dataset))

metadata_selection = {"author": "D_Trump16"}      # dict | A selector off metadata. Example: {"field": "value"}  (optional)

try:
    payload = nucleus_api.DocInfo(dataset=dataset, metadata_selection=metadata_selection)
    api_response = api_instance.post_doc_info(payload)
    
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    title:', res.title)
    for attr in res.attribute.keys():
        if attr == 'time':
            print('   ', attr, ':', datetime.datetime.fromtimestamp(float(res.attribute[attr])))
        else:
            print('   ', attr, ':', res.attribute[attr])

    print('---------------')

print('-------------------------------------------------------------')


# ## Display document details

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('------------------- Get document details for {} -----------------------'.format(dataset))

#doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the documents to retrieve. Example: ["title1", "title2", ..., "titleN"]  (optional)
doc_ids = ['776902852041351634']      # str | The docid of the documents to retrieve. Example: ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.DocDisplay(dataset, doc_ids=doc_ids)
    api_response = api_instance.post_doc_display(payload)
    
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))
    print('    Content', res.content)

    print('---------------')

print('-------------------------------------------------------------')


# ## Display document details with a metadata selection

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('------------------- Get document details for {} -----------------------'.format(dataset))
metadata_selection = {"author": "D_Trump16"}      # dict | A selector off metadata. Example: {"field": "value"}  (optional)

try:
    payload = nucleus_api.DocDisplay(dataset=dataset, metadata_selection=metadata_selection)
    api_response = api_instance.post_doc_display(payload)
    
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

for res in api_response.result:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute['author'])
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute['time'])))
    print('    Content', res.content)

    print('---------------')

print('-------------------------------------------------------------')


# ## Get document recommendations

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('------------- Get document recommendations for {} -----------------'.format(dataset))

#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, ["docid1", "docid2", ..., "docidN"]  (optional)

try:
    payload = nucleus_api.DocumentRecommendModel(dataset=dataset, 
                                                query=query, 
                                                custom_stop_words=custom_stop_words, 
                                                num_topics=num_topics, 
                                                num_keywords=num_keywords)
    api_response = api_instance.post_doc_recommend_api(payload)
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])
    
for i, res in enumerate(api_response.result):
    print('Document recommendations for topic', i, ':')
    print('    Keywords:', res.keywords)

    for j, doc in enumerate(res.recommendations):
        print('    Recommendation', j, ':')
        print('        Document ID:', doc.sourceid)
        print('        Title:', doc.title)
        print('        Attribute:', doc.attribute)
        print('        Author:', doc.attribute['author'])
        print('        Time:', datetime.datetime.fromtimestamp(float(doc.attribute['time'])))
    
    print('---------------')
    
print('-------------------------------------------------------------')


# ## Get document summary

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
doc_title = 'D_Trump2018_8_17_14_10' # str | The title of the document to be summarized.
print('------------------ Get document summary for {} in {}  --------------------'.format(doc_title, dataset))

custom_stop_words = ["real","hillary"] # List of stop words. (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
short_sentence_length = 0 # int | The sentence length below which a sentence is excluded from summarization (optional) (default to 4)
long_sentence_length = 40 # int | The sentence length beyond which a sentence is excluded from summarization (optional) (default to 40)

try:
    payload = nucleus_api.DocumentSummaryModel(dataset=dataset, 
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
    
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

print('-------------------------------------------------------------')


# ## Get document sentiment

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
doc_title = 'D_Trump2018_8_17_14_10' # str | The title of the document to be analyzed.
print('------------------ Get document sentiment  for {} in {}  --------------------'.format(doc_title, dataset))

custom_stop_words = ["real","hillary"] # List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the document. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the document. (optional) (default to 8)

try:
    payload = nucleus_api.DocumentSentimentModel(dataset=dataset, 
                                                doc_title=doc_title, 
                                                custom_stop_words=custom_stop_words, 
                                                num_topics=num_topics, 
                                                num_keywords=num_keywords)
    api_response = api_instance.post_doc_sentiment_api(payload)
    
    print('Sentiment for', api_response.result.doc_title)
    print(api_response.result.sentiment)

except ValueError as e:
    print('ERROR:', e)
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])

print('-------------------------------------------------------------')


# ## Tag documents

# In[ ]:


dataset = 'trump_tweets' # str | Dataset name.
print('---------------- Tag dataset ------------------------')

try:
    payload = nucleus_api.DatasetTagging(dataset=dataset, 
                                        query='new york city OR big apple OR NYC OR New York', 
                                        metadata_selection='', 
                                        time_period='',
                                        period_start='2010-01-01',
                                        period_end='2019-04-30')
    api_response = api_instance.post_dataset_tagging(payload)
    print(api_response)
    print('    Entities tagged:', api_response.result.entities_tagged)
    print('    Docids tagged with the entities:', api_response.result.doc_ids)
    print('    Entities count:', api_response.result.entities_count)
except ApiException as e:
    api_error = json.loads(e.body)
    print('ERROR:', api_error['message'])


# ## Summarize file from URL 

# In[ ]:


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
  
print('Summary for', result.doc_title, ':')
for sent in result.summary.sentences:
    print('    *', sent)

print('-------------------------------------------------------------')


# In[ ]:




