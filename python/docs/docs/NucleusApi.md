# nucleus_api.NucleusApi

All URIs are relative to *https://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_author_connectivity_api**](NucleusApi.md#get_author_connectivity_api) | **GET** /topics/author_connectivity | 
[**get_dataset_info**](NucleusApi.md#get_dataset_info) | **GET** /datasets/dataset_info | 
[**get_doc_display**](NucleusApi.md#get_doc_display) | **GET** /documents/document_display | 
[**get_doc_info**](NucleusApi.md#get_doc_info) | **GET** /documents/document_info | 
[**get_doc_recommend_api**](NucleusApi.md#get_doc_recommend_api) | **GET** /documents/document_recommend | 
[**get_doc_summary_api**](NucleusApi.md#get_doc_summary_api) | **GET** /documents/document_summary | 
[**get_job**](NucleusApi.md#get_job) | **GET** /jobs | 
[**get_list_datasets**](NucleusApi.md#get_list_datasets) | **GET** /datasets | 
[**get_topic_api**](NucleusApi.md#get_topic_api) | **GET** /topics/topics | 
[**get_topic_delta_api**](NucleusApi.md#get_topic_delta_api) | **GET** /topics/topic_delta | 
[**get_topic_summary_api**](NucleusApi.md#get_topic_summary_api) | **GET** /topics/topic_summary | 
[**get_user**](NucleusApi.md#get_user) | **GET** /users | 
[**post_append_json_to_dataset**](NucleusApi.md#post_append_json_to_dataset) | **POST** /datasets/append_json_to_dataset | 
[**post_delete_dataset**](NucleusApi.md#post_delete_dataset) | **POST** /datasets/delete_dataset | 
[**post_delete_document**](NucleusApi.md#post_delete_document) | **POST** /datasets/delete_document | 
[**post_example_job**](NucleusApi.md#post_example_job) | **POST** /jobs/start_example_job | 
[**post_legacy**](NucleusApi.md#post_legacy) | **POST** /legacy | 
[**post_topic_consensus_api**](NucleusApi.md#post_topic_consensus_api) | **POST** /topics/topic_consensus | 
[**post_topic_historical_analysis_api**](NucleusApi.md#post_topic_historical_analysis_api) | **POST** /topics/topic_historical | 
[**post_topic_sentiment_api**](NucleusApi.md#post_topic_sentiment_api) | **POST** /topics/topic_sentiment | 
[**post_upload_file**](NucleusApi.md#post_upload_file) | **POST** /datasets/upload_file | 
[**post_upload_url**](NucleusApi.md#post_upload_url) | **POST** /datasets/import_file_from_url | 
[**post_user**](NucleusApi.md#post_user) | **POST** /users | 


# **get_author_connectivity_api**
> AuthorConnectRespModel get_author_connectivity_api(dataset, target_author, time_period, query=query, custom_stop_words=custom_stop_words, metadata_selection=metadata_selection, excluded_docs=excluded_docs)



Get the network of similar authors to a reference author.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
target_author = 'target_author_example' # str | Name of the author to be analyzed.
time_period = 'time_period_example' # str | Time period selection
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of words possibly used by the target author that are considered not information-bearing. (optional)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance.get_author_connectivity_api(dataset, target_author, time_period, query=query, custom_stop_words=custom_stop_words, metadata_selection=metadata_selection, excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_author_connectivity_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **target_author** | **str**| Name of the author to be analyzed. | 
 **time_period** | **str**| Time period selection | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of words possibly used by the target author that are considered not information-bearing. | [optional] 
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**AuthorConnectRespModel**](AuthorConnectRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_info**
> DatasetInfoRespModel get_dataset_info(dataset, query=query, metadata_selection=metadata_selection, time_period=time_period)



Get information about a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. (optional)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)

try:
    api_response = api_instance.get_dataset_info(dataset, query=query, metadata_selection=metadata_selection, time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_dataset_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. | [optional] 
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 

### Return type

[**DatasetInfoRespModel**](DatasetInfoRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_display**
> DocDisplayRespModel get_doc_display(dataset, doc_titles=doc_titles, doc_ids=doc_ids)



Document display.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
doc_titles = 'doc_titles_example' # str | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ]  (optional)
doc_ids = 'doc_ids_example' # str | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ] (optional)

try:
    api_response = api_instance.get_doc_display(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_doc_display: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **doc_titles** | **str**| The title of the documents on which info is requested. Example: [ \&quot;title 1\&quot;, \&quot;title 2\&quot; ]  | [optional] 
 **doc_ids** | **str**| The docid of the documents on which info is requested. Example:[ \&quot;docid1, docid2\&quot; ] | [optional] 

### Return type

[**DocDisplayRespModel**](DocDisplayRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_info**
> DocInfoRespModel get_doc_info(dataset, doc_titles=doc_titles, doc_ids=doc_ids)



Document metadata retrieval.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
doc_titles = 'doc_titles_example' # str | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ]  (optional)
doc_ids = 'doc_ids_example' # str | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ] (optional)

try:
    api_response = api_instance.get_doc_info(dataset, doc_titles=doc_titles, doc_ids=doc_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_doc_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **doc_titles** | **str**| The title of the documents on which info is requested. Example: [ \&quot;title 1\&quot;, \&quot;title 2\&quot; ]  | [optional] 
 **doc_ids** | **str**| The docid of the documents on which info is requested. Example:[ \&quot;docid1, docid2\&quot; ] | [optional] 

### Return type

[**DocInfoRespModel**](DocInfoRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_recommend_api**
> DocumentRecommendRespModel get_doc_recommend_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, num_docs=num_docs, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
num_docs = 20 # int | Number of desired recommended docs per topic. (optional) (default to 20)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance.get_doc_recommend_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, num_docs=num_docs, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_doc_recommend_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words. | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **num_docs** | **int**| Number of desired recommended docs per topic. | [optional] [default to 20]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**DocumentRecommendRespModel**](DocumentRecommendRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_summary_api**
> DocumentSummaryRespModel get_doc_summary_api(dataset, doc_title, custom_stop_words=custom_stop_words, summary_length=summary_length, context_amount=context_amount, short_sentence_length=short_sentence_length, long_sentence_length=long_sentence_length)



Document summarization.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
doc_title = 'doc_title_example' # str | The title of the document to be summarized.
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
short_sentence_length = 4 # int | The sentence length below which a sentence is excluded from summarization (optional) (default to 4)
long_sentence_length = 40 # int | The sentence length beyond which a sentence is excluded from summarization (optional) (default to 40)

try:
    api_response = api_instance.get_doc_summary_api(dataset, doc_title, custom_stop_words=custom_stop_words, summary_length=summary_length, context_amount=context_amount, short_sentence_length=short_sentence_length, long_sentence_length=long_sentence_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_doc_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **doc_title** | **str**| The title of the document to be summarized. | 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **summary_length** | **int**| The maximum number of bullet points a user wants to see in the document summary. | [optional] [default to 6]
 **context_amount** | **int**| The number of sentences surrounding key summary sentences in the documents that they come from. | [optional] [default to 0]
 **short_sentence_length** | **int**| The sentence length below which a sentence is excluded from summarization | [optional] [default to 4]
 **long_sentence_length** | **int**| The sentence length beyond which a sentence is excluded from summarization | [optional] [default to 40]

### Return type

[**DocumentSummaryRespModel**](DocumentSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobRespModel get_job(id)



Use this API to check the progress and retrieve results of a job. Poll this endpoint repeatedly until result is not null.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
id = 'id_example' # str | ID of the job

try:
    api_response = api_instance.get_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job | 

### Return type

[**JobRespModel**](JobRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_datasets**
> ListDatasetsModel get_list_datasets()



List the datasets owned by the user.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))

try:
    api_response = api_instance.get_list_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_list_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDatasetsModel**](ListDatasetsModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_api**
> TopicRespModel get_topic_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs)



Get key topics from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance.get_topic_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_topic_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words. | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicRespModel**](TopicRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_delta_api**
> TopicDeltaRespModel get_topic_delta_api(dataset, time_start_t0, time_end_t0, time_start_t1, time_end_t1, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, excluded_docs=excluded_docs)



Get changes in exposure to key topics from documents in a dataset in between two dates.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset with a time series component. These docs should reference a universe of entities that overlaps through time.
time_start_t0 = 'time_start_t0_example' # str | Start date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
time_end_t0 = 'time_end_t0_example' # str | End date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
time_start_t1 = 'time_start_t1_example' # str | Start date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
time_end_t1 = 'time_end_t1_example' # str | End date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance.get_topic_delta_api(dataset, time_start_t0, time_end_t0, time_start_t1, time_end_t1, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_topic_delta_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset with a time series component. These docs should reference a universe of entities that overlaps through time. | 
 **time_start_t0** | **str**| Start date for the start-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **time_end_t0** | **str**| End date for the start-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **time_start_t1** | **str**| Start date for the end-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **time_end_t1** | **str**| End date for the end-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words. | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicDeltaRespModel**](TopicDeltaRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_summary_api**
> TopicSummaryRespModel get_topic_summary_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, summary_length=summary_length, context_amount=context_amount, num_docs=num_docs, excluded_docs=excluded_docs)



Get summaries of topics that have been extracted from a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset and summarized. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in each topic summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the documents that they come from. (optional) (default to 0)
num_docs = 20 # int | The maximum number of key documents to use for summarization. (optional) (default to 20)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)

try:
    api_response = api_instance.get_topic_summary_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, summary_length=summary_length, context_amount=context_amount, num_docs=num_docs, excluded_docs=excluded_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_topic_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset and summarized. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 
 **summary_length** | **int**| The maximum number of bullet points a user wants to see in each topic summary. | [optional] [default to 6]
 **context_amount** | **int**| The number of sentences surrounding key summary sentences in the documents that they come from. | [optional] [default to 0]
 **num_docs** | **int**| The maximum number of key documents to use for summarization. | [optional] [default to 20]
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicSummaryRespModel**](TopicSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserModel get_user(user_email, password)



Use this API to authenticate. If the password is correct, returns the user details, including the user's api key.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nucleus_api.NucleusApi()
user_email = 'user_email_example' # str | Email of the user to authenticate. 
password = 'password_example' # str | Plaintext password of the user to authenticate. 

try:
    api_response = api_instance.get_user(user_email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| Email of the user to authenticate.  | 
 **password** | **str**| Plaintext password of the user to authenticate.  | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_append_json_to_dataset**
> AppendJsonRespModel post_append_json_to_dataset(payload)



Add a document to a dataset, in JSON form.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.Appendjsonparams() # Appendjsonparams | 

try:
    api_response = api_instance.post_append_json_to_dataset(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_append_json_to_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Appendjsonparams**](Appendjsonparams.md)|  | 

### Return type

[**AppendJsonRespModel**](AppendJsonRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_dataset**
> DeleteDatasetRespModel post_delete_dataset(payload)



Delete an existing dataset from the user storage.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.Deletedatasetmodel() # Deletedatasetmodel | 

try:
    api_response = api_instance.post_delete_dataset(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_delete_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Deletedatasetmodel**](Deletedatasetmodel.md)|  | 

### Return type

[**DeleteDatasetRespModel**](DeleteDatasetRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_document**
> DeleteDocumentRespModel post_delete_document(payload)



Delete a document from a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.Deletedocumentmodel() # Deletedocumentmodel | 

try:
    api_response = api_instance.post_delete_document(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Deletedocumentmodel**](Deletedocumentmodel.md)|  | 

### Return type

[**DeleteDocumentRespModel**](DeleteDocumentRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_example_job**
> ExampleJobResponse post_example_job(color, wait_time)



Start an example background job

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
color = 'color_example' # str | A color
wait_time = 0 # int | Seconds to wait before returning the result (default to 0)

try:
    api_response = api_instance.post_example_job(color, wait_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_example_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **str**| A color | 
 **wait_time** | **int**| Seconds to wait before returning the result | [default to 0]

### Return type

[**ExampleJobResponse**](ExampleJobResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_legacy**
> LegacyResponseModel post_legacy(payload)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.ApiCall() # ApiCall | 

try:
    api_response = api_instance.post_legacy(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_legacy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ApiCall**](ApiCall.md)|  | 

### Return type

[**LegacyResponseModel**](LegacyResponseModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_consensus_api**
> TopicConsensusRespModel post_topic_consensus_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)



Get topic consensus for topics extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)
custom_dict_file = '/path/to/file.txt' # file | Custom sentiment dictionary JSON file. (optional)

try:
    api_response = api_instance.post_topic_consensus_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_consensus_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **custom_dict_file** | **file**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicConsensusRespModel**](TopicConsensusRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_historical_analysis_api**
> TopicHistoryRespModel post_topic_historical_analysis_api(dataset, time_period, update_period, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, inc_step=inc_step, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)



Get a historical analysis of topics extracted from a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
time_period = '1M' # str | Time period selection (default to 1M)
update_period = 'd' # str | Frequency at which the historical anlaysis is performed (default to d)
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
inc_step = 1 # int | Number of increments of the udpate period in between two historical computations. (optional) (default to 1)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)
custom_dict_file = '/path/to/file.txt' # file | Custom sentiment dictionary JSON file. (optional)

try:
    api_response = api_instance.post_topic_historical_analysis_api(dataset, time_period, update_period, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, inc_step=inc_step, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_historical_analysis_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **time_period** | **str**| Time period selection | [default to 1M]
 **update_period** | **str**| Frequency at which the historical anlaysis is performed | [default to d]
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **inc_step** | **int**| Number of increments of the udpate period in between two historical computations. | [optional] [default to 1]
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **custom_dict_file** | **file**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicHistoryRespModel**](TopicHistoryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_sentiment_api**
> TopicSentimentRespModel post_topic_sentiment_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)



Get topic sentiment for topics extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
dataset = 'dataset_example' # str | Dataset name.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
num_keywords = 8 # int | Number of keywords per topic that is extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)
excluded_docs = 'excluded_docs_example' # str | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\"  (optional)
custom_dict_file = '/path/to/file.txt' # file | Custom sentiment dictionary JSON file. (optional)

try:
    api_response = api_instance.post_topic_sentiment_api(dataset, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, num_keywords=num_keywords, metadata_selection=metadata_selection, time_period=time_period, excluded_docs=excluded_docs, custom_dict_file=custom_dict_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_sentiment_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **num_keywords** | **int**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 
 **excluded_docs** | **str**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **custom_dict_file** | **file**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicSentimentRespModel**](TopicSentimentRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_upload_file**
> UploadFileRespModel post_upload_file(file, dataset, metadata=metadata)



### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
file = '/path/to/file.txt' # file | 
dataset = 'dataset_example' # str | Destination dataset where the file will be inserted.
metadata = 'metadata_example' # str | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"} (optional)

try:
    api_response = api_instance.post_upload_file(file, dataset, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 
 **dataset** | **str**| Destination dataset where the file will be inserted. | 
 **metadata** | **str**| Optional json containing additional document metadata. Eg: {\&quot;time\&quot;:\&quot;01/01/2001\&quot;,\&quot;author\&quot;:\&quot;me\&quot;} | [optional] 

### Return type

[**UploadFileRespModel**](UploadFileRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_upload_url**
> UploadUrlRespModel post_upload_url(payload)



### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.UploadURLModel() # UploadURLModel | 

try:
    api_response = api_instance.post_upload_url(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UploadURLModel**](UploadURLModel.md)|  | 

### Return type

[**UploadUrlRespModel**](UploadUrlRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> PostUserRespModel post_user(payload)



Use this API to register a new user. Email and password are required, all other fields optional.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.User() # User | 

try:
    api_response = api_instance.post_user(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**User**](User.md)|  | 

### Return type

[**PostUserRespModel**](PostUserRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

