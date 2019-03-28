# nucleus_api.NucleusApi

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# **get_list_filters**
> ListFiltersModel get_list_filters()



List the filters owned by the user.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))

try:
    api_response = api_instance.get_list_filters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_list_filters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListFiltersModel**](ListFiltersModel.md)

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# **post_author_connectivity_api**
> AuthorConnectRespModel post_author_connectivity_api(payload)



Get the network of similar authors to a reference author.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.AuthorConnection() # AuthorConnection | 

try:
    api_response = api_instance.post_author_connectivity_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_author_connectivity_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**AuthorConnection**](AuthorConnection.md)|  | 

### Return type

[**AuthorConnectRespModel**](AuthorConnectRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dataset_info**
> DatasetInfoRespModel post_dataset_info(payload)



Get information about a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DatasetInfo() # DatasetInfo | 

try:
    api_response = api_instance.post_dataset_info(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_dataset_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DatasetInfo**](DatasetInfo.md)|  | 

### Return type

[**DatasetInfoRespModel**](DatasetInfoRespModel.md)

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# **post_delete_filter**
> DeleteFilterRespModel post_delete_filter(payload)



Delete a filter.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DeleteFilterModel() # DeleteFilterModel | 

try:
    api_response = api_instance.post_delete_filter(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteFilterModel**](DeleteFilterModel.md)|  | 

### Return type

[**DeleteFilterRespModel**](DeleteFilterRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_display**
> DocDisplayRespModel post_doc_display(payload)



Document display.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DocDisplay() # DocDisplay | 

try:
    api_response = api_instance.post_doc_display(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_doc_display: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocDisplay**](DocDisplay.md)|  | 

### Return type

[**DocDisplayRespModel**](DocDisplayRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_info**
> DocInfoRespModel post_doc_info(payload)



Document metadata retrieval.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DocInfo() # DocInfo | 

try:
    api_response = api_instance.post_doc_info(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_doc_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocInfo**](DocInfo.md)|  | 

### Return type

[**DocInfoRespModel**](DocInfoRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_recommend_api**
> DocumentRecommendRespModel post_doc_recommend_api(payload)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DocumentRecommendModel() # DocumentRecommendModel | 

try:
    api_response = api_instance.post_doc_recommend_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_doc_recommend_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocumentRecommendModel**](DocumentRecommendModel.md)|  | 

### Return type

[**DocumentRecommendRespModel**](DocumentRecommendRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_sentiment_api**
> DocumentSentimentRespModel post_doc_sentiment_api(payload)



Document sentiment.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DocumentSentimentModel() # DocumentSentimentModel | 

try:
    api_response = api_instance.post_doc_sentiment_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_doc_sentiment_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocumentSentimentModel**](DocumentSentimentModel.md)|  | 

### Return type

[**DocumentSentimentRespModel**](DocumentSentimentRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_summary_api**
> DocumentSummaryRespModel post_doc_summary_api(payload)



Document summarization.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.DocumentSummaryModel() # DocumentSummaryModel | 

try:
    api_response = api_instance.post_doc_summary_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_doc_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocumentSummaryModel**](DocumentSummaryModel.md)|  | 

### Return type

[**DocumentSummaryRespModel**](DocumentSummaryRespModel.md)

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# **post_rename_dataset**
> RenameDatasetRespModel post_rename_dataset(payload)



Rename an existing dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.Renamedatasetmodel() # Renamedatasetmodel | 

try:
    api_response = api_instance.post_rename_dataset(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_rename_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Renamedatasetmodel**](Renamedatasetmodel.md)|  | 

### Return type

[**RenameDatasetRespModel**](RenameDatasetRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_save_filter**
> SaveFilterRespModel post_save_filter(payload)



Save a filter representing a subsect of a dataset (time range, query, metadata..).

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.SaveFilterModel() # SaveFilterModel | 

try:
    api_response = api_instance.post_save_filter(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_save_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**SaveFilterModel**](SaveFilterModel.md)|  | 

### Return type

[**SaveFilterRespModel**](SaveFilterRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_api**
> TopicRespModel post_topic_api(payload)



Get key topics from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.Topics() # Topics | 

try:
    api_response = api_instance.post_topic_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Topics**](Topics.md)|  | 

### Return type

[**TopicRespModel**](TopicRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_consensus_api**
> TopicConsensusRespModel post_topic_consensus_api(payload)



Get topic consensus for topics extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.TopicConsensusModel() # TopicConsensusModel | 

try:
    api_response = api_instance.post_topic_consensus_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_consensus_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicConsensusModel**](TopicConsensusModel.md)|  | 

### Return type

[**TopicConsensusRespModel**](TopicConsensusRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_delta_api**
> TopicDeltaRespModel post_topic_delta_api(payload)



Get changes in exposure to key topics from documents in a dataset in between two dates.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.TopicDeltaModel() # TopicDeltaModel | 

try:
    api_response = api_instance.post_topic_delta_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_delta_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicDeltaModel**](TopicDeltaModel.md)|  | 

### Return type

[**TopicDeltaRespModel**](TopicDeltaRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_historical_analysis_api**
> TopicHistoryRespModel post_topic_historical_analysis_api(payload)



Get a historical analysis of topics extracted from a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.TopicHistoryModel() # TopicHistoryModel | 

try:
    api_response = api_instance.post_topic_historical_analysis_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_historical_analysis_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicHistoryModel**](TopicHistoryModel.md)|  | 

### Return type

[**TopicHistoryRespModel**](TopicHistoryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_sentiment_api**
> TopicSentimentRespModel post_topic_sentiment_api(payload)



Get topic sentiment for topics extracted from a given dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.TopicSentimentModel() # TopicSentimentModel | 

try:
    api_response = api_instance.post_topic_sentiment_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_sentiment_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicSentimentModel**](TopicSentimentModel.md)|  | 

### Return type

[**TopicSentimentRespModel**](TopicSentimentRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_topic_summary_api**
> TopicSummaryRespModel post_topic_summary_api(payload)



Get summaries of topics that have been extracted from a dataset.

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
payload = nucleus_api.TopicSummaryModel() # TopicSummaryModel | 

try:
    api_response = api_instance.post_topic_summary_api(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->post_topic_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicSummaryModel**](TopicSummaryModel.md)|  | 

### Return type

[**TopicSummaryRespModel**](TopicSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_upload_file**
> UploadFileRespModel post_upload_file(file, dataset, metadata=metadata, filename=filename)



### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))
file = '/path/to/file.txt' # file | 
dataset = 'dataset_example' # str | Destination dataset where the file will be inserted.
metadata = 'metadata_example' # str | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"} (optional)
filename = 'filename_example' # str | Specify the filename if you want to override the original filename (Nucleus guesses the file type from the file name extension) (optional)

try:
    api_response = api_instance.post_upload_file(file, dataset, metadata=metadata, filename=filename)
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
 **filename** | **str**| Specify the filename if you want to override the original filename (Nucleus guesses the file type from the file name extension) | [optional] 

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

# Configure API host and key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

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

