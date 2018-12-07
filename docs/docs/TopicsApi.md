# swagger_client.TopicsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_topic_api**](TopicsApi.md#get_topic_api) | **GET** /topics/topics | 
[**get_topic_sentiment_api**](TopicsApi.md#get_topic_sentiment_api) | **GET** /topics/topic_sentiment | 
[**get_topic_summary_api**](TopicsApi.md#get_topic_summary_api) | **GET** /topics/topic_summary | 


# **get_topic_api**
> TopicModel get_topic_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, metadata_selection=metadata_selection, time_period=time_period)



Get key topics from a given dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopicsApi()
dataset = 'dataset_example' # str | Dataset name.
x_api_key = 'x_api_key_example' # str | API key for authentication.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)

try:
    api_response = api_instance.get_topic_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, metadata_selection=metadata_selection, time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **x_api_key** | **str**| API key for authentication. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words. | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 

### Return type

[**TopicModel**](TopicModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_sentiment_api**
> TopicSentimentModel get_topic_sentiment_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, docids=docids)



Get topic sentiment for topics extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopicsApi()
dataset = 'dataset_example' # str | Dataset name.
x_api_key = 'x_api_key_example' # str | API key for authentication.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
docids = 56 # int | The document ids to be used for topic extractions. (optional)

try:
    api_response = api_instance.get_topic_sentiment_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, docids=docids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_sentiment_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **x_api_key** | **str**| API key for authentication. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **docids** | **int**| The document ids to be used for topic extractions. | [optional] 

### Return type

[**TopicSentimentModel**](TopicSentimentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_summary_api**
> TopicSummaryModel get_topic_summary_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, summary_length=summary_length, context_amount=context_amount, reduce_rate_docs=reduce_rate_docs, reduce_rate_dict=reduce_rate_dict, num_docs=num_docs)



Get summarization of topics that have been extracted from a dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopicsApi()
dataset = 'dataset_example' # str | Dataset name.
x_api_key = 'x_api_key_example' # str | API key for authentication.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. (optional) (default to 0)
reduce_rate_docs = 0.25 # float | The percentage of the total dataset that the user targets in terms of recommended content from which summaries are derived. Range 0.0 to 1.0. (optional) (default to 0.25)
reduce_rate_dict = 0.25 # float | The number of keywords per topic that the user wants to see, expressed as a percentage of the full dataset dictionary. Range 0.0 to 1.0. (optional) (default to 0.25)
num_docs = 20 # int | The maximum number of documents to use for summarization. (optional) (default to 20)

try:
    api_response = api_instance.get_topic_summary_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, summary_length=summary_length, context_amount=context_amount, reduce_rate_docs=reduce_rate_docs, reduce_rate_dict=reduce_rate_dict, num_docs=num_docs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_topic_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **x_api_key** | **str**| API key for authentication. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **summary_length** | **int**| The maximum number of bullet points a user wants to see in the document summary. | [optional] [default to 6]
 **context_amount** | **int**| The number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. | [optional] [default to 0]
 **reduce_rate_docs** | **float**| The percentage of the total dataset that the user targets in terms of recommended content from which summaries are derived. Range 0.0 to 1.0. | [optional] [default to 0.25]
 **reduce_rate_dict** | **float**| The number of keywords per topic that the user wants to see, expressed as a percentage of the full dataset dictionary. Range 0.0 to 1.0. | [optional] [default to 0.25]
 **num_docs** | **int**| The maximum number of documents to use for summarization. | [optional] [default to 20]

### Return type

[**TopicSummaryModel**](TopicSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

