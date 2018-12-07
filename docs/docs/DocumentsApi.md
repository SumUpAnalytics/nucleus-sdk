# swagger_client.DocumentsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_doc_recommend_api**](DocumentsApi.md#get_doc_recommend_api) | **GET** /documents/document_recommend | 
[**get_doc_summary_api**](DocumentsApi.md#get_doc_summary_api) | **GET** /documents/document_summary | 


# **get_doc_recommend_api**
> DocumentRecommendModel get_doc_recommend_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, reduce_rate_docs=reduce_rate_docs, reduce_rate_dict=reduce_rate_dict)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentsApi()
dataset = 'dataset_example' # str | Dataset name.
x_api_key = 'x_api_key_example' # str | API key for authentication.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = 'custom_stop_words_example' # str | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
reduce_rate_docs = 0.1 # float | The max number of recommended documents the user wants to see per topic, expressed as a percentage of the total dataset. (optional) (default to 0.1)
reduce_rate_dict = 0.01 # float | The number of keywords per topic that the user wants to get content recommendations on, expressed as a percentage of the full dataset dictionary. (optional) (default to 0.01)

try:
    api_response = api_instance.get_doc_recommend_api(dataset, x_api_key, query=query, custom_stop_words=custom_stop_words, num_topics=num_topics, reduce_rate_docs=reduce_rate_docs, reduce_rate_dict=reduce_rate_dict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_recommend_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **x_api_key** | **str**| API key for authentication. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **custom_stop_words** | **str**| List of stop words. | [optional] 
 **num_topics** | **int**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **reduce_rate_docs** | **float**| The max number of recommended documents the user wants to see per topic, expressed as a percentage of the total dataset. | [optional] [default to 0.1]
 **reduce_rate_dict** | **float**| The number of keywords per topic that the user wants to get content recommendations on, expressed as a percentage of the full dataset dictionary. | [optional] [default to 0.01]

### Return type

[**DocumentRecommendModel**](DocumentRecommendModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_summary_api**
> DocumentSummaryModel get_doc_summary_api(dataset, doc_title, x_api_key, custom_stop_words=custom_stop_words, summary_length=summary_length, context_amount=context_amount)



Document summarization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentsApi()
dataset = 'dataset_example' # str | Dataset name.
doc_title = 'doc_title_example' # str | The title of the document to be summarized.
x_api_key = 'x_api_key_example' # str | API key for authentication.
custom_stop_words = 'custom_stop_words_example' # str | List of stop words (optional)
summary_length = 6 # int | The maximum number of bullet points a user wants to see in the document summary. (optional) (default to 6)
context_amount = 0 # int | The number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. (optional) (default to 0)

try:
    api_response = api_instance.get_doc_summary_api(dataset, doc_title, x_api_key, custom_stop_words=custom_stop_words, summary_length=summary_length, context_amount=context_amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_doc_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **doc_title** | **str**| The title of the document to be summarized. | 
 **x_api_key** | **str**| API key for authentication. | 
 **custom_stop_words** | **str**| List of stop words | [optional] 
 **summary_length** | **int**| The maximum number of bullet points a user wants to see in the document summary. | [optional] [default to 6]
 **context_amount** | **int**| The number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. | [optional] [default to 0]

### Return type

[**DocumentSummaryModel**](DocumentSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

