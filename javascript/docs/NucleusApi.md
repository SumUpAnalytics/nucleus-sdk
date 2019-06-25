# NucleusApi.NucleusApi

All URIs are relative to *https://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](NucleusApi.md#getJob) | **GET** /jobs | 
[**getListDatasets**](NucleusApi.md#getListDatasets) | **GET** /datasets | 
[**getListFilters**](NucleusApi.md#getListFilters) | **GET** /filters | 
[**getUser**](NucleusApi.md#getUser) | **GET** /users | 
[**postAppendJsonToDataset**](NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
[**postAuthorConnectivityApi**](NucleusApi.md#postAuthorConnectivityApi) | **POST** /topics/author_connectivity | 
[**postAvailableSecFilings**](NucleusApi.md#postAvailableSecFilings) | **POST** /feeds/available_sec_filings | 
[**postBulkInsertJson**](NucleusApi.md#postBulkInsertJson) | **POST** /datasets/bulk_insert_json | 
[**postCreateDatasetFromSecFilings**](NucleusApi.md#postCreateDatasetFromSecFilings) | **POST** /feeds/create_dataset_from_sec_filings | 
[**postDatasetInfo**](NucleusApi.md#postDatasetInfo) | **POST** /datasets/dataset_info | 
[**postDatasetTagging**](NucleusApi.md#postDatasetTagging) | **POST** /datasets/dataset_tagging | 
[**postDeleteDataset**](NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
[**postDeleteDocument**](NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
[**postDeleteFilter**](NucleusApi.md#postDeleteFilter) | **POST** /filters/delete_filter | 
[**postDocClassifyApi**](NucleusApi.md#postDocClassifyApi) | **POST** /documents/document_classify | 
[**postDocDisplay**](NucleusApi.md#postDocDisplay) | **POST** /documents/document_display | 
[**postDocInfo**](NucleusApi.md#postDocInfo) | **POST** /documents/document_info | 
[**postDocRecommendApi**](NucleusApi.md#postDocRecommendApi) | **POST** /documents/document_recommend | 
[**postDocSentimentApi**](NucleusApi.md#postDocSentimentApi) | **POST** /documents/document_sentiment | 
[**postDocSummaryApi**](NucleusApi.md#postDocSummaryApi) | **POST** /documents/document_summary | 
[**postDocumentContrastSummaryApi**](NucleusApi.md#postDocumentContrastSummaryApi) | **POST** /documents/document_contrasted_summary | 
[**postExampleJob**](NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
[**postLegacy**](NucleusApi.md#postLegacy) | **POST** /legacy | 
[**postRenameDataset**](NucleusApi.md#postRenameDataset) | **POST** /datasets/rename_dataset | 
[**postSaveFilter**](NucleusApi.md#postSaveFilter) | **POST** /filters/save_filter | 
[**postTopicApi**](NucleusApi.md#postTopicApi) | **POST** /topics/topics | 
[**postTopicConsensusApi**](NucleusApi.md#postTopicConsensusApi) | **POST** /topics/topic_consensus | 
[**postTopicConsensusTransferApi**](NucleusApi.md#postTopicConsensusTransferApi) | **POST** /topics/topic_consensus_transfer | 
[**postTopicContrastApi**](NucleusApi.md#postTopicContrastApi) | **POST** /topics/topic_contrast | 
[**postTopicDeltaApi**](NucleusApi.md#postTopicDeltaApi) | **POST** /topics/topic_delta | 
[**postTopicHistoricalAnalysisApi**](NucleusApi.md#postTopicHistoricalAnalysisApi) | **POST** /topics/topic_historical | 
[**postTopicSentimentApi**](NucleusApi.md#postTopicSentimentApi) | **POST** /topics/topic_sentiment | 
[**postTopicSentimentTransferApi**](NucleusApi.md#postTopicSentimentTransferApi) | **POST** /topics/topic_sentiment_transfer | 
[**postTopicSummaryApi**](NucleusApi.md#postTopicSummaryApi) | **POST** /topics/topic_summary | 
[**postTopicTransferApi**](NucleusApi.md#postTopicTransferApi) | **POST** /topics/topic_transfer | 
[**postUploadFile**](NucleusApi.md#postUploadFile) | **POST** /datasets/upload_file | 
[**postUploadUrl**](NucleusApi.md#postUploadUrl) | **POST** /datasets/import_file_from_url | 
[**postUser**](NucleusApi.md#postUser) | **POST** /users | 


<a name="getJob"></a>
# **getJob**
> JobRespModel getJob(id)



Use this API to check the progress and retrieve results of a job. Poll this endpoint repeatedly until result is not null.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var id = "id_example"; // String | ID of the job


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getJob(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the job | 

### Return type

[**JobRespModel**](JobRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getListDatasets"></a>
# **getListDatasets**
> ListDatasetsModel getListDatasets()



List the datasets owned by the user.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getListDatasets(callback);
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

<a name="getListFilters"></a>
# **getListFilters**
> ListFiltersModel getListFilters()



List the filters owned by the user.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getListFilters(callback);
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

<a name="getUser"></a>
# **getUser**
> UserModel getUser(user_email, password)



Use this API to authenticate. If the password is correct, returns the user details, including the user&#39;s api key.

### Example
```javascript
var NucleusApi = require('nucleus_api');

var apiInstance = new NucleusApi.NucleusApi();

var user_email = "user_email_example"; // String | Email of the user to authenticate. 

var password = "password_example"; // String | Plaintext password of the user to authenticate. 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getUser(user_email, password, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **String**| Email of the user to authenticate.  | 
 **password** | **String**| Plaintext password of the user to authenticate.  | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="postAppendJsonToDataset"></a>
# **postAppendJsonToDataset**
> AppendJsonRespModel postAppendJsonToDataset(payload)



Add a document to a dataset, in JSON form.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.Appendjsonparams(); // Appendjsonparams | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postAppendJsonToDataset(payload, callback);
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

<a name="postAuthorConnectivityApi"></a>
# **postAuthorConnectivityApi**
> AuthorConnectRespModel postAuthorConnectivityApi(payload)



Get the network of similar authors to a reference author.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.AuthorConnection(); // AuthorConnection | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postAuthorConnectivityApi(payload, callback);
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

<a name="postAvailableSecFilings"></a>
# **postAvailableSecFilings**
> AvailableFilingsResponseModel postAvailableSecFilings(payload)



Get information about the available sec filings. If no input is passed, returns the list of all available tickers. If tickers are passed, returns the list of available document types for these tickers. If documt types are also passed, returns the list of available secions for the selected tickers/filing types

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.EdgarFields(); // EdgarFields | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postAvailableSecFilings(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**EdgarFields**](EdgarFields.md)|  | 

### Return type

[**AvailableFilingsResponseModel**](AvailableFilingsResponseModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postBulkInsertJson"></a>
# **postBulkInsertJson**
> BulkInsertRespModel postBulkInsertJson(payload)



Add many document to a dataset, in JSON form. Bulk insertion is much faster than making one api call for each document.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.BulkInsertParams(); // BulkInsertParams | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postBulkInsertJson(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**BulkInsertParams**](BulkInsertParams.md)|  | 

### Return type

[**BulkInsertRespModel**](BulkInsertRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postCreateDatasetFromSecFilings"></a>
# **postCreateDatasetFromSecFilings**
> CreateSecDatasetResponseModel postCreateDatasetFromSecFilings(payload)



Creates a new dataset and populates it with sec filings matching the specified tickers/form types.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.EdgarQuery(); // EdgarQuery | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postCreateDatasetFromSecFilings(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**EdgarQuery**](EdgarQuery.md)|  | 

### Return type

[**CreateSecDatasetResponseModel**](CreateSecDatasetResponseModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postDatasetInfo"></a>
# **postDatasetInfo**
> DatasetInfoRespModel postDatasetInfo(payload)



Get information about a dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DatasetInfo(); // DatasetInfo | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDatasetInfo(payload, callback);
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

<a name="postDatasetTagging"></a>
# **postDatasetTagging**
> DatasetTaggingRespModel postDatasetTagging(payload)



Tag documents containig specified entities within a dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DatasetTagging(); // DatasetTagging | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDatasetTagging(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DatasetTagging**](DatasetTagging.md)|  | 

### Return type

[**DatasetTaggingRespModel**](DatasetTaggingRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postDeleteDataset"></a>
# **postDeleteDataset**
> DeleteDatasetRespModel postDeleteDataset(payload)



Delete an existing dataset from the user storage.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.Deletedatasetmodel(); // Deletedatasetmodel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDeleteDataset(payload, callback);
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

<a name="postDeleteDocument"></a>
# **postDeleteDocument**
> DeleteDocumentRespModel postDeleteDocument(payload)



Delete a document from a dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.Deletedocumentmodel(); // Deletedocumentmodel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDeleteDocument(payload, callback);
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

<a name="postDeleteFilter"></a>
# **postDeleteFilter**
> DeleteFilterRespModel postDeleteFilter(payload)



Delete a filter.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DeleteFilterModel(); // DeleteFilterModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDeleteFilter(payload, callback);
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

<a name="postDocClassifyApi"></a>
# **postDocClassifyApi**
> DocClassifyRespModel postDocClassifyApi(payload)



Document one-layer classifier on a chosen dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocClassifyModel(); // DocClassifyModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocClassifyApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocClassifyModel**](DocClassifyModel.md)|  | 

### Return type

[**DocClassifyRespModel**](DocClassifyRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postDocDisplay"></a>
# **postDocDisplay**
> DocDisplayRespModel postDocDisplay(payload)



Document display.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocDisplay(); // DocDisplay | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocDisplay(payload, callback);
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

<a name="postDocInfo"></a>
# **postDocInfo**
> DocInfoRespModel postDocInfo(payload)



Retrieve metadata of documents matching the provided filter (limited to 10000 documents).

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocInfo(); // DocInfo | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocInfo(payload, callback);
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

<a name="postDocRecommendApi"></a>
# **postDocRecommendApi**
> DocumentRecommendRespModel postDocRecommendApi(payload)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocumentRecommendModel(); // DocumentRecommendModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocRecommendApi(payload, callback);
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

<a name="postDocSentimentApi"></a>
# **postDocSentimentApi**
> DocumentSentimentRespModel postDocSentimentApi(payload)



Document sentiment.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocumentSentimentModel(); // DocumentSentimentModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocSentimentApi(payload, callback);
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

<a name="postDocSummaryApi"></a>
# **postDocSummaryApi**
> DocumentSummaryRespModel postDocSummaryApi(payload)



Document summarization.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocumentSummaryModel(); // DocumentSummaryModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocSummaryApi(payload, callback);
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

<a name="postDocumentContrastSummaryApi"></a>
# **postDocumentContrastSummaryApi**
> DocumentContrastSummaryRespModel postDocumentContrastSummaryApi(payload)



Document contrasted summarization.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.DocumentContrastSummaryModel(); // DocumentContrastSummaryModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postDocumentContrastSummaryApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DocumentContrastSummaryModel**](DocumentContrastSummaryModel.md)|  | 

### Return type

[**DocumentContrastSummaryRespModel**](DocumentContrastSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postExampleJob"></a>
# **postExampleJob**
> ExampleJobResponse postExampleJob(color, wait_time)



Start an example background job

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var color = "color_example"; // String | A color

var wait_time = 0; // Number | Seconds to wait before returning the result


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postExampleJob(color, wait_time, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **String**| A color | 
 **wait_time** | **Number**| Seconds to wait before returning the result | [default to 0]

### Return type

[**ExampleJobResponse**](ExampleJobResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="postLegacy"></a>
# **postLegacy**
> LegacyResponseModel postLegacy(payload)



Recommendation of documents on given topics that have been extracted from a given dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.ApiCall(); // ApiCall | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postLegacy(payload, callback);
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

<a name="postRenameDataset"></a>
# **postRenameDataset**
> RenameDatasetRespModel postRenameDataset(payload)



Rename an existing dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.Renamedatasetmodel(); // Renamedatasetmodel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postRenameDataset(payload, callback);
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

<a name="postSaveFilter"></a>
# **postSaveFilter**
> SaveFilterRespModel postSaveFilter(payload)



Save a filter representing a subsect of a dataset (time range, query, metadata..).

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.SaveFilterModel(); // SaveFilterModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postSaveFilter(payload, callback);
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

<a name="postTopicApi"></a>
# **postTopicApi**
> TopicRespModel postTopicApi(payload)



Get key topics from a given dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.Topics(); // Topics | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicApi(payload, callback);
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

<a name="postTopicConsensusApi"></a>
# **postTopicConsensusApi**
> TopicConsensusRespModel postTopicConsensusApi(payload)



Get topic consensus for topics extracted from a given dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicConsensusModel(); // TopicConsensusModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicConsensusApi(payload, callback);
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

<a name="postTopicConsensusTransferApi"></a>
# **postTopicConsensusTransferApi**
> TopicConsensusTransferRespModel postTopicConsensusTransferApi(payload)



Get exposures of documents in a validation dataset to topics extracted from a reference dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicConsensusTransferModel(); // TopicConsensusTransferModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicConsensusTransferApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicConsensusTransferModel**](TopicConsensusTransferModel.md)|  | 

### Return type

[**TopicConsensusTransferRespModel**](TopicConsensusTransferRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postTopicContrastApi"></a>
# **postTopicContrastApi**
> TopicContrastRespModel postTopicContrastApi(payload)



Contrasting topic extraction on a chosen dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicContrastModel(); // TopicContrastModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicContrastApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicContrastModel**](TopicContrastModel.md)|  | 

### Return type

[**TopicContrastRespModel**](TopicContrastRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postTopicDeltaApi"></a>
# **postTopicDeltaApi**
> TopicDeltaRespModel postTopicDeltaApi(payload)



Get changes in exposure to key topics from documents in a dataset in between two dates.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicDeltaModel(); // TopicDeltaModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicDeltaApi(payload, callback);
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

<a name="postTopicHistoricalAnalysisApi"></a>
# **postTopicHistoricalAnalysisApi**
> TopicHistoryRespModel postTopicHistoricalAnalysisApi(payload)



Get a historical analysis of topics extracted from a dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicHistoryModel(); // TopicHistoryModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicHistoricalAnalysisApi(payload, callback);
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

<a name="postTopicSentimentApi"></a>
# **postTopicSentimentApi**
> TopicSentimentRespModel postTopicSentimentApi(payload)



Get topic sentiment for topics extracted from a given dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicSentimentModel(); // TopicSentimentModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicSentimentApi(payload, callback);
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

<a name="postTopicSentimentTransferApi"></a>
# **postTopicSentimentTransferApi**
> TopicSentimentTransferRespModel postTopicSentimentTransferApi(payload)



Get sentiment exposures of documents in a validation dataset to topics extracted from a reference dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicSentimentTransferModel(); // TopicSentimentTransferModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicSentimentTransferApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicSentimentTransferModel**](TopicSentimentTransferModel.md)|  | 

### Return type

[**TopicSentimentTransferRespModel**](TopicSentimentTransferRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postTopicSummaryApi"></a>
# **postTopicSummaryApi**
> TopicSummaryRespModel postTopicSummaryApi(payload)



Get summaries of topics that have been extracted from a dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicSummaryModel(); // TopicSummaryModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicSummaryApi(payload, callback);
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

<a name="postTopicTransferApi"></a>
# **postTopicTransferApi**
> TopicTransferRespModel postTopicTransferApi(payload)



Get exposures of documents in a validation dataset to topics extracted from a reference dataset.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.TopicTransferModel(); // TopicTransferModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicTransferApi(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TopicTransferModel**](TopicTransferModel.md)|  | 

### Return type

[**TopicTransferRespModel**](TopicTransferRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postUploadFile"></a>
# **postUploadFile**
> UploadFileRespModel postUploadFile(file, dataset, opts)



### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var file = "/path/to/file.txt"; // File | 

var dataset = "dataset_example"; // String | Destination dataset where the file will be inserted.

var opts = { 
  'metadata': "metadata_example", // String | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"}
  'filename': "filename_example" // String | Specify the filename if you want to override the original filename (Nucleus guesses the file type from the file name extension)
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postUploadFile(file, dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **File**|  | 
 **dataset** | **String**| Destination dataset where the file will be inserted. | 
 **metadata** | **String**| Optional json containing additional document metadata. Eg: {\&quot;time\&quot;:\&quot;01/01/2001\&quot;,\&quot;author\&quot;:\&quot;me\&quot;} | [optional] 
 **filename** | **String**| Specify the filename if you want to override the original filename (Nucleus guesses the file type from the file name extension) | [optional] 

### Return type

[**UploadFileRespModel**](UploadFileRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="postUploadUrl"></a>
# **postUploadUrl**
> UploadUrlRespModel postUploadUrl(payload)



### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.UploadURLModel(); // UploadURLModel | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postUploadUrl(payload, callback);
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

<a name="postUser"></a>
# **postUser**
> PostUserRespModel postUser(payload)



Use this API to register a new user. Email and password are required, all other fields optional.

### Example
```javascript
var NucleusApi = require('nucleus_api');
var defaultClient = NucleusApi.ApiClient.instance;

// Configure API key authorization: apikey
var apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

var apiInstance = new NucleusApi.NucleusApi();

var payload = new NucleusApi.User(); // User | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postUser(payload, callback);
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

