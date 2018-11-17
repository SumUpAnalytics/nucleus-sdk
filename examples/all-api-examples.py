#!/usr/bin/env python
# coding: utf-8

# In[37]:


from __future__ import print_function
import csv, json
import time
import nucleus_client
from nucleus_client.rest import ApiException
from pprint import pprint


# # Configure API host and key

# In[38]:


configuration = nucleus_client.Configuration()
configuration.host = 'UPDATE-WITH-API-HOST'
configuration.api_key['x-api-key'] = 'UPDATE-WITH-API-KEY'


# # Dataset APIs

# ## Create API instance

# In[39]:


print('-------------------------------------------------------------')
print('--                Dataset API Examples                     --')
print('-------------------------------------------------------------')
api_instance_dataset = nucleus_client.DatasetsApi(nucleus_client.ApiClient(configuration))


# ## Append file from local drive to dataset

# In[40]:


print('--------- Append file from local drive to dataset -----------')
print('')
file = 'quarles20181109a.pdf' # file | 
dataset = 'dataset_test' # str | Destination dataset where the file will be inserted.

try:
    api_instance_dataset.post_upload_file(file, dataset)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_file: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Append file from URL to dataset

# In[41]:


print('------------ Append frile from URL to dataset ---------------')

dataset = dataset
file_url = 'https://www.federalreserve.gov/newsevents/speech/files/quarles20181109a.pdf'
payload = nucleus_client.UploadURLModel(
                dataset=dataset,
                file_url=file_url
            ) # UploadURLModel | 

try:
    api_response = api_instance_dataset.post_upload_url(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_url: %s\n" % e)
print('-------------------------------------------------------------')


# ## Append json from csv to dataset

# In[42]:


print('----------- Append json from CSV to dataset -----------------')
# add documents to dataset
csv_file = 'trump-tweets-100.csv'
dataset = dataset   

doc_cnt = 0
with open(csv_file, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if doc_cnt < 10:
            payload = nucleus_client.Appendjsonparams(dataset=dataset, 
                                                  language='english', 
                                                  document={'time'   : row['time'],
                                                            'title'  : row['title'],
                                                            'content': row['content'],
                                                            'author' : row['author']}
                                                 )

            try:
                response = api_instance_dataset.post_append_json_to_dataset(payload)
            except ApiException as e:
                print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
        
        doc_cnt = doc_cnt + 1
        
print('Dataset', dataset, 'now has', response.success, 'documents.')
print('-------------------------------------------------------------')


# ## List available datasets

# In[43]:


print('---------------- List available datasets ---------------------')
try:
    api_response = api_instance_dataset.get_list_datasets()
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)

list_datasets = api_response.to_dict()['list_datasets']

print(len(list_datasets), 'datasets in the database:')
for ds in list_datasets:
    print('    ', ds)

    
print('-------------------------------------------------------------')


# ## Get dataset information

# In[44]:


print('-------------------------------------------------------------')
dataset = dataset # str | Dataset name.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. (optional)
metadata_selection = '' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = '' # str | Time period selection (optional)

try:
    api_response = api_instance_dataset.get_dataset_info(dataset, 
                                                 query=query, 
                                                 metadata_selection=metadata_selection, 
                                                 time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_info: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Delete document

# In[45]:


print('-------------------------------------------------------------')
dataset = dataset
payload = nucleus_client.Deletedocumentmodel(dataset=dataset,
                                             docid='1') # Deletedocumentmodel | 

try:
    api_response = api_instance_dataset.post_delete_document(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_delete_document: %s\n" % e)

print('-------------------------------------------------------------')


# ## Delete dataset

# In[46]:


dataset = dataset     
payload = nucleus_client.Deletedatasetmodel(dataset=dataset) # Deletedatasetmodel | 

try:
    api_response = api_instance_dataset.post_delete_dataset(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_delete_dataset: %s\n" % e)
    
# List datasets again to check if the specified dataset has been deleted
try:
    api_response = api_instance_dataset.get_list_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)


# ## Create a full dataset for testing other APIs

# In[47]:


print('-------------------------------------------------------------')
# add documents to dataset
csv_file = 'trump-tweets-100.csv'
dataset = 'trump_tweets'   

with open(csv_file, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        payload = nucleus_client.Appendjsonparams(dataset=dataset, 
                                                  language='english', 
                                                  document={'time'   : row['time'],
                                                            'title'  : row['title'],
                                                            'content': row['content'],
                                                            'author' : row['author']}
                                                 )

        try:
            response = api_instance_dataset.post_append_json_to_dataset(payload)
        except ApiException as e:
            print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
            
print(response)
print('-------------------------------------------------------------')


# # Topic APIs

# ## Create API Instance

# In[48]:


print('-------------------------------------------------------------')
print('--                Topic API Examples                     --')
print('-------------------------------------------------------------')
api_instance_topic = nucleus_client.TopicsApi(nucleus_client.ApiClient(configuration))


# ## Get list of topics from dataset

# In[49]:


print('-------------------------------------------------------------')
dataset = dataset
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection ="" # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period =""# str | Time period selection (optional)

try:
    api_response = api_instance_topic.get_topic_api(
        dataset,                                
        query=query,                   
        custom_stop_words=custom_stop_words,     
        num_topics=num_topics,
        metadata_selection=metadata_selection,
        time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Get topic summary

# In[50]:


print('-------------------------------------------------------------')
dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in each topic summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
num_docs = 20 # int | The maximum number of key documents to use for summarization. (optional) (default to 20)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_summary_api(dataset, 
                                                      query=query, 
                                                      custom_stop_words=custom_stop_words, 
                                                      num_topics=num_topics, 
                                                      num_keywords=num_keywords, 
                                                      summary_length=summary_length, 
                                                      context_amount=context_amount, 
                                                      num_docs=num_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_summary_api: %s\n" % e)

print('-------------------------------------------------------------')


# ## Get topic sentiment

# In[51]:


print('-------------------------------------------------------------')
dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_sentiment_api(dataset, 
                                                        query=query, 
                                                        custom_stop_words=custom_stop_words, 
                                                        num_topics=num_topics, 
                                                        num_keywords=num_keywords)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_sentiment_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Get topic consensus

# In[52]:


print('-------------------------------------------------------------')
dataset = dataset # str | Dataset name.
query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_consensus_api(dataset, 
                                                        query=query, 
                                                        custom_stop_words=custom_stop_words, 
                                                        num_topics=num_topics, 
                                                        num_keywords=num_keywords)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_consensus_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Get author connectivity

# In[53]:


print('-------------------------------------------------------------')
dataset = dataset # str | Dataset name.
target_author = 'D_Trump16' # str | Name of the author to be analyzed.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of words possibly used by the target author that are considered not information-bearing. (optional)
time_period = '' # str | Time period selection (optional)
metadata_selection = '' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_author_connectivity_api(
        dataset, 
        target_author, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        time_period=time_period, 
        metadata_selection=metadata_selection, 
        excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_author_connectivity_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# # Document APIs

# ## Create API instance

# In[54]:


print('-------------------------------------------------------------')
print('--                Document API examples                    --')
print('-------------------------------------------------------------')

api_instance_doc = nucleus_client.DocumentsApi(nucleus_client.ApiClient(configuration))


# ## Get document information without content

# In[55]:


dataset = dataset # str | Dataset name.
doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the document to retrieve. Example: \" \"title 1\" \"  (optional)
doc_ids = ['11', '12', '20']      # int | The docid of the document to retrieve. Example: \"docid1\"  (optional)

try:
    api_response = api_instance_doc.get_doc_info(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_info: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Display document details

# In[56]:


print('-------------------------------------------------------------')

dataset = dataset # str | Dataset name.
doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the document to retrieve. Example: \" \"title 1\" \"  (optional)
doc_ids = ['11']      # int | The docid of the document to retrieve. Example: \"docid1\"  (optional)

try:
    api_response = api_instance_doc.get_doc_display(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_display_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Get document recommendation

# In[57]:


print('-------------------------------------------------------------')

dataset = dataset # str | Dataset name.
query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_doc.get_doc_recommend_api(dataset, 
                                                      query=query, 
                                                      custom_stop_words=custom_stop_words, 
                                                      num_topics=num_topics, 
                                                      num_keywords=num_keywords)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_recommend_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# ## Get document summary

# In[58]:


print('-------------------------------------------------------------')

dataset = dataset # str | Dataset name.
doc_title = 'D_Trump2018_8_15_15_4' # str | The title of the document to be summarized.
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)

try:
    api_response = api_instance_doc.get_doc_summary_api(dataset, doc_title, custom_stop_words=custom_stop_words, summary_length=summary_length, context_amount=context_amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_summary_api: %s\n" % e)
    
print('-------------------------------------------------------------')


# In[ ]:





# In[ ]:





# In[ ]:




