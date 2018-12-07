# swagger_client.DatasetsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_info**](DatasetsApi.md#get_dataset_info) | **GET** /datasets/dataset_info | 
[**get_list_datasets**](DatasetsApi.md#get_list_datasets) | **GET** /datasets | 
[**post_append_json_to_dataset**](DatasetsApi.md#post_append_json_to_dataset) | **POST** /datasets/append_json_to_dataset | 


# **get_dataset_info**
> GetDatasetInfoModel get_dataset_info(dataset, x_api_key, query=query, metadata_selection=metadata_selection, time_period=time_period)



Get information about a dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetsApi()
dataset = 'dataset_example' # str | Dataset name.
x_api_key = 'x_api_key_example' # str | API key for authentication.
query = 'query_example' # str | Fulltext query, using mysql MATCH boolean query format. (optional)
metadata_selection = 'metadata_selection_example' # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period = 'time_period_example' # str | Time period selection (optional)

try:
    api_response = api_instance.get_dataset_info(dataset, x_api_key, query=query, metadata_selection=metadata_selection, time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset name. | 
 **x_api_key** | **str**| API key for authentication. | 
 **query** | **str**| Fulltext query, using mysql MATCH boolean query format. | [optional] 
 **metadata_selection** | **str**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **time_period** | **str**| Time period selection | [optional] 

### Return type

[**GetDatasetInfoModel**](GetDatasetInfoModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_datasets**
> UserDatasetModel get_list_datasets(x_api_key)



List the datasets owned by the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetsApi()
x_api_key = 'x_api_key_example' # str | API key for authentication.

try:
    api_response = api_instance.get_list_datasets(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| API key for authentication. | 

### Return type

[**UserDatasetModel**](UserDatasetModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_append_json_to_dataset**
> AppendjsonpostModel post_append_json_to_dataset(payload)



Add a document to a dataset, in JSON form.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetsApi()
payload = swagger_client.Appendjsonparams() # Appendjsonparams | 

try:
    api_response = api_instance.post_append_json_to_dataset(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Appendjsonparams**](Appendjsonparams.md)|  | 

### Return type

[**AppendjsonpostModel**](AppendjsonpostModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

