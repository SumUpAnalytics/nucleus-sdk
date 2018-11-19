#!/usr/bin/env python
# coding: utf-8

# In[22]:


from __future__ import print_function
import csv, json, datetime
import time
import nucleus_client
from nucleus_client.rest import ApiException
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

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


# # Helper functions

# In[2]:


# Plot topic historical analysis
def topic_charts_historical(historical_metrics, selected_topics, show_sentiment_consensus):

    # Charts of Strength, Sentiment, Consensus for each of the topics
    current_max_strength = 0
    current_max_sent = 0
    current_max_cons = 0
    for i in selected_topics:
        if np.nanmax(np.abs(historical_metrics[i]['strength'])) > current_max_strength:
            current_max_strength = np.nanmax(np.abs(historical_metrics[i]['strength']))
        if np.nanmax(np.abs(historical_metrics[i]['sentiment'])) > current_max_sent:
            current_max_sent = np.nanmax(np.abs(historical_metrics[i]['sentiment']))
        if np.nanmax(np.abs(historical_metrics[i]['consensus'])) > current_max_cons:
            current_max_cons = np.nanmax(np.abs(historical_metrics[i]['consensus']))

    if show_sentiment_consensus == True:
        plt.rcParams['figure.figsize'] = [12, 18*len(selected_topics)]
        fig = plt.figure() 
        for i in selected_topics:
            current_ax = 'ax' + str(selected_topics.index(i) + 1)
            if current_ax == 'ax1':
                current_ax = plt.subplot(3*len(selected_topics), 1, 1 + 3*selected_topics.index(i))
                ax1 = plt.subplot(3*len(selected_topics), 1, 1 + 3*selected_topics.index(i))
            else:
                current_ax = plt.subplot(3*len(selected_topics), 1, 1 + 3*selected_topics.index(i), sharex=ax1)

            # 3 subplots, one per strength, sentiment, consensus
            current_ax.set_ylim([0, 1.05*current_max_strength])
            current_ax.plot('time_stamps', 'strength', data=historical_metrics[i], color='blue')
            plt.ylabel('Prevalence', fontsize=14, fontweight="bold")
            plt.title(historical_metrics[i]['topic'], fontsize=14, fontweight="bold")

            current_axSent = plt.subplot(3*len(selected_topics), 1, 1 + 3*selected_topics.index(i) + 1, sharex=ax1)
            current_axSent.set_ylim([-1.05*current_max_sent, 1.05*current_max_sent])
            current_axSent.plot('time_stamps', 'sentiment', data=historical_metrics[i], color='green')
            plt.ylabel('Sentiment', fontsize=14, fontweight="bold")

            current_axCons = plt.subplot(3*len(selected_topics), 1, 1 + 3*selected_topics.index(i) + 2, sharex=ax1)
            current_axCons.set_ylim([0, 1.05*current_max_cons])
            current_axCons.plot('time_stamps', 'consensus', data=historical_metrics[i], color='red')
            plt.ylabel('Consensus', fontsize=14, fontweight="bold")

        fig.autofmt_xdate(rotation=90)
    else:
        plt.rcParams['figure.figsize'] = [12, 6*len(selected_topics)]
        fig = plt.figure()
        for i in selected_topics:
            current_ax = 'ax' + str(selected_topics.index(i) + 1)
            if current_ax == 'ax1':
                current_ax = plt.subplot(len(selected_topics), 1, selected_topics.index(i) + 1)
                ax1 = plt.subplot(len(selected_topics), 1, selected_topics.index(i) + 1)
            else:
                current_ax = plt.subplot(len(selected_topics), 1, selected_topics.index(i) + 1, sharex=ax1)
            current_ax.set_ylim([0, 1.05*current_max_strength])
            current_ax.plot('time_stamps', 'strength', data=historical_metrics[i], color='blue')
            plt.ylabel('Prevalence', fontsize=14, fontweight="bold")        
            plt.title(historical_metrics[i]['topic'], fontsize=14, fontweight="bold")
        fig.autofmt_xdate(rotation=90)
        
    return 0


# # Configure API host and key

# In[3]:


configuration = nucleus_client.Configuration()
configuration.host = 'UPDATE-WITH-API-HOST'
configuration.api_key['x-api-key'] = 'UPDATE-WITH-API-KEY'
configuration.host = 'https://7h4tcw9nej.execute-api.us-west-2.amazonaws.com/beta'
configuration.api_key['x-api-key'] = 'hmsVTKr57l8LZPAZ_iEOYg'
configuration.host = 'http://localhost:5000'
configuration.api_key['x-api-key'] = 'p2Hbhk1J2cTnO6VFrNUP1Q'


# # Dataset APIs

# ## Create API instance

# In[4]:


print('-------------------------------------------------------------')
print('--                Dataset API Examples                     --')
print('-------------------------------------------------------------')
api_instance_dataset = nucleus_client.DatasetsApi(nucleus_client.ApiClient(configuration))


# ## Append file from local drive to dataset

# In[5]:


print('--------- Append file from local drive to dataset -----------')
print('')
file = 'quarles20181109a.pdf' # file | 
dataset = 'dataset_test' # str | Destination dataset where the file will be inserted.

try:
    api_instance_dataset.post_upload_file(file, dataset)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_file: %s\n" % e)

print(file, 'has been added to dataset', dataset)
print('-------------------------------------------------------------')


# ## Append file from URL to dataset

# In[6]:


print('------------ Append file from URL to dataset ---------------')

dataset = dataset
file_url = 'https://www.federalreserve.gov/newsevents/speech/files/quarles20181109a.pdf'
payload = nucleus_client.UploadURLModel(
                dataset=dataset,
                file_url=file_url
            ) # UploadURLModel | 

try:
    api_response = api_instance_dataset.post_upload_url(payload)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_upload_url: %s\n" % e)
    
#pprint(api_response)   # raw API response
print(file_url, 'has been added to dataset', dataset)
print('-------------------------------------------------------------')


# ## Append json from csv to dataset

# In[7]:


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
                api_response = api_instance_dataset.post_append_json_to_dataset(payload)
            except ApiException as e:
                print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
        
        doc_cnt = doc_cnt + 1
        
print('Dataset', dataset, 'now has', api_response.num_documents, 'documents.')
print('-------------------------------------------------------------')


# ## List available datasets

# In[8]:


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

# In[9]:


print('--------------- Get dataset information -------------------')
dataset = dataset # str | Dataset name.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. (optional)
metadata_selection = '' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = '' # str | Time period selection (optional)

try:
    api_response = api_instance_dataset.get_dataset_info(
        dataset, 
        query=query, 
        metadata_selection=metadata_selection, 
        time_period=time_period)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_info: %s\n" % e)

print('Information about dataset', dataset)
print('    Language:', api_response.detected_language)
print('    Number of documents:', api_response.num_documents)
print('    Time range:', datetime.datetime.fromtimestamp(float(api_response.time_range[0])),
             'to', datetime.datetime.fromtimestamp(float(api_response.time_range[1])))

#pprint(api_response) # raw API response
print('-------------------------------------------------------------')


# ## Delete document

# In[10]:


print('--------------------- Delete document -----------------------')
dataset = dataset
docid = '1'
payload = nucleus_client.Deletedocumentmodel(dataset=dataset,
                                             docid=docid) # Deletedocumentmodel | 

try:
    api_response = api_instance_dataset.post_delete_document(payload)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_delete_document: %s\n" % e)


print('Document', docid, 'from dataset', dataset, 'has been deleted.')
# print(api_response)     # raw API response
print('-------------------------------------------------------------')


# ## Delete dataset

# In[11]:


print('--------------------- Delete dataset ------------------------')

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
    
print('-------------------------------------------------------------')


# ## Create a full dataset for testing other APIs

# In[12]:


print('--------- Create a full dataset for testing other APIs ---------')
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
            
print('Dataset', dataset, 'now has', response.num_documents, 'documents.')
print('-------------------------------------------------------------')


# # Topic APIs

# ## Create API Instance

# In[13]:


print('-------------------------------------------------------------')
print('--                Topic API Examples                     --')
print('-------------------------------------------------------------')
api_instance_topic = nucleus_client.TopicsApi(nucleus_client.ApiClient(configuration))


# ## Get list of topics from dataset

# In[14]:


print('------------- Get list of topics from dataset --------------')
dataset = dataset
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
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
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_api: %s\n" % e)
    
#print(api_response)
i = 1
for res in api_response.results:
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

# In[15]:


print('------------------- Get topic summary -----------------------')
dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection ="" # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in each topic summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
num_docs = 20 # int | The maximum number of key documents to use for summarization. (optional) (default to 20)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_summary_api(
        dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords,
        metadata_selection=metadata_selection,
        summary_length=summary_length, 
        context_amount=context_amount, 
        num_docs=num_docs)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_summary_api: %s\n" % e)

i = 1
for res in api_response.results:
    print('Topic', i, 'summary:')
    print('    Keywords:', res.topic)
    for j in range(len(res.summary)):
        print('    Document ID:', res.summary[j].sourceid)
        print('        Title:', res.summary[j].title)
        print('        Sentences:', res.summary[j].sentences)
        print('        Author:', res.summary[j].attribute.author)
        print('        Source:', res.summary[j].attribute.source)
        print('        Time:', datetime.datetime.fromtimestamp(float(res.summary[j].attribute.time)))

        #print(type(res.summary[j].attribute))
        
    print('---------------')
    i = i + 1
    
    
#pprint(api_response)  # raw API response
print('-------------------------------------------------------------')


# ## Get topic sentiment

# In[16]:


print('---------------- Get topic sentiment ------------------------')
dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_sentiment_api(
        dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords)
    
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_sentiment_api: %s\n" % e)

i = 1
for res in api_response.results:
    print('Topic', i, 'sentiment:')
    print('    Keywords:', res.topic)
    print('    Sentiment:', res.sentiment)
    print('    Strength:', res.strength)
    
    doc_id_str = ' '.join(str(x) for x in res.doc_id)
    doc_sentiment_str = ' '.join(str(x) for x in res.doc_sentiment)
    doc_score_str = ' '.join(str(x) for x in res.doc_score)
    print('    Doucment IDs:', doc_id_str)
    print('    Doucment Sentiments:', doc_sentiment_str)
    print('    Doucment Scores:', doc_score_str)
    
    print('---------------')
    i = i + 1
    
#pprint(api_response)
print('-------------------------------------------------------------')


# ## Get topic consensus

# In[17]:


print('---------------- Get topic consensus ------------------------')
dataset = dataset # str | Dataset name.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_consensus_api(
        dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_consensus_api: %s\n" % e)
    
i = 1
for res in api_response.results:
    print('Topic', i, 'consensus:')
    print('    Keywords:', res.topic)
    print('    Consensus:', res.consensus)
    print('    Strength:', res.strength)
    
    print('---------------')
    i = i + 1
    
#pprint(api_response) # raw API response
print('-------------------------------------------------------------')


# ## Get topic historical analysis

# In[24]:


print('------------ Get topic historical analysis ----------------')

dataset = dataset   # str | Dataset name.
time_period = '6M'  # str | Time period selection (default to 1M)
update_period = 'd' # str | Frequency at which the historical anlaysis is performed (default to d)
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = '' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
inc_step = 1 # int | Number of increments of the udpate period in between two historical computations. (optional) (default to 1)
excluded_docs = [''] # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_topic.get_topic_historical_analysis_api(
        dataset, 
        time_period, 
        update_period, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords, 
        metadata_selection=metadata_selection, 
        inc_step=inc_step, 
        excluded_docs=excluded_docs)
    
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_historical_analysis_api: %s\n" % e)

results = api_response.results

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
#pprint(api_response)
print('-------------------------------------------------------------')


# ## Get author connectivity

# In[ ]:


print('----------------- Get author connectivity -------------------')
dataset = dataset # str | Dataset name.
target_author = 'D_Trump16' # str | Name of the author to be analyzed.
query = '' # str | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # str | List of words possibly used by the target author that are considered not information-bearing. (optional)
time_period = '12M' # str | Time period selection. Required. Valid values: "1M","3M","6M","12M","3Y","5Y"
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
    
except ApiException as e:
    print("Exception when calling TopicsApi->get_author_connectivity_api: %s\n" % e)

res = api_response.results
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


# # Document APIs

# ## Create API instance

# In[ ]:


print('-------------------------------------------------------------')
print('--                Document API examples                    --')
print('-------------------------------------------------------------')

api_instance_doc = nucleus_client.DocumentsApi(nucleus_client.ApiClient(configuration))


# ## Get document information without content

# In[ ]:


dataset = dataset # str | Dataset name.
doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the document to retrieve. Example: \" \"title 1\" \"  (optional)
doc_ids = ['11', '12', '20']      # int | The docid of the document to retrieve. Example: \"docid1\"  (optional)

try:
    api_response = api_instance_doc.get_doc_info(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_info: %s\n" % e)
    
for res in api_response.results:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute.author)
    print('    Source:', res.attribute.source)
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute.time)))

    print('---------------')
    
    
#pprint(api_response)  # raw response from API server
print('-------------------------------------------------------------')


# ## Display document details

# In[ ]:


print('-------------------------------------------------------------')

dataset = dataset # str | Dataset name.
doc_titles = ['D_Trump2018_8_18_1_47']   # str | The title of the document to retrieve. Example: \" \"title 1\" \"  (optional)
doc_ids = ['11']      # int | The docid of the document to retrieve. Example: \"docid1\"  (optional)

try:
    api_response = api_instance_doc.get_doc_display(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_display_api: %s\n" % e)

for res in api_response.results:
    print('Document ID:', res.sourceid)
    print('    Title:', res.title)
    print('    Author:', res.attribute.author)
    print('    Source:', res.attribute.source)
    print('    Time:', datetime.datetime.fromtimestamp(float(res.attribute.time)))
    print('    Content', res.content)

    print('---------------')


#pprint(api_response) # raw response from API server
print('-------------------------------------------------------------')


# ## Get document recommendations

# In[ ]:


print('------------- Get document recommendations -----------------')

dataset = dataset # str | Dataset name.
#query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
query = ''
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
excluded_docs = '' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance_doc.get_doc_recommend_api(
        dataset, 
        query=query, 
        custom_stop_words=custom_stop_words, 
        num_topics=num_topics, 
        num_keywords=num_keywords)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_recommend_api: %s\n" % e)
    
i = 1
for res in api_response.results:
    print('Document recommendations for topic', i, ':')
    print('    Keywords:', res.topic)

    j = 1
    for doc in res.recommendations:
        print('    Recommendation', j, ':')
        print('        Document ID:', doc.sourceid)
        print('        Title:', doc.title)
        print('        Attribute:', doc.attribute)
        print('        Author:', doc.attribute.author)
        print('        Source:', doc.attribute.source)
        print('        Time:', datetime.datetime.fromtimestamp(float(doc.attribute.time)))
        j = j + 1
    
    print('---------------')
    i = i + 1
    
#pprint(api_response)   # raw API response
print('-------------------------------------------------------------')


# ## Get document summary

# In[ ]:


print('------------------ Get document summary  --------------------')

dataset = dataset # str | Dataset name.
doc_title = 'D_Trump2018_8_15_15_4' # str | The title of the document to be summarized.
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)

try:
    api_response = api_instance_doc.get_doc_summary_api(
        dataset, 
        doc_title, 
        custom_stop_words=custom_stop_words, 
        summary_length=summary_length, 
        context_amount=context_amount)
    
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_summary_api: %s\n" % e)
 
print('Document Summary')
print('    ID:', api_response.summary.sourceid)
print('    Title:', api_response.doc_title)
print('    Summary:', api_response.summary.sentences)

#pprint(api_response)   # raw API response
print('-------------------------------------------------------------')


# In[ ]:





# In[ ]:




