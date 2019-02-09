# NucleusApi.NucleusApi

All URIs are relative to *https://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](NucleusApi.md#getJob) | **GET** /jobs | 
[**getListDatasets**](NucleusApi.md#getListDatasets) | **GET** /datasets | 
[**getUser**](NucleusApi.md#getUser) | **GET** /users | 
[**postAppendJsonToDataset**](NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
[**postAuthorConnectivityApi**](NucleusApi.md#postAuthorConnectivityApi) | **POST** /topics/author_connectivity | 
[**postDatasetInfo**](NucleusApi.md#postDatasetInfo) | **POST** /datasets/dataset_info | 
[**postDeleteDataset**](NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
[**postDeleteDocument**](NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
[**postDocDisplay**](NucleusApi.md#postDocDisplay) | **POST** /documents/document_display | 
[**postDocInfo**](NucleusApi.md#postDocInfo) | **POST** /documents/document_info | 
[**postDocRecommendApi**](NucleusApi.md#postDocRecommendApi) | **POST** /documents/document_recommend | 
[**postDocSummaryApi**](NucleusApi.md#postDocSummaryApi) | **POST** /documents/document_summary | 
[**postExampleJob**](NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
[**postLegacy**](NucleusApi.md#postLegacy) | **POST** /legacy | 
[**postTopicApi**](NucleusApi.md#postTopicApi) | **POST** /topics/topics | 
[**postTopicConsensusApi**](NucleusApi.md#postTopicConsensusApi) | **POST** /topics/topic_consensus | 
[**postTopicDeltaApi**](NucleusApi.md#postTopicDeltaApi) | **POST** /topics/topic_delta | 
[**postTopicHistoricalAnalysisApi**](NucleusApi.md#postTopicHistoricalAnalysisApi) | **POST** /topics/topic_historical | 
[**postTopicSentimentApi**](NucleusApi.md#postTopicSentimentApi) | **POST** /topics/topic_sentiment | 
[**postTopicSummaryApi**](NucleusApi.md#postTopicSummaryApi) | **POST** /topics/topic_summary | 
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



Document metadata retrieval.

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

var payload = new NucleusApi.RecommendDocs(); // RecommendDocs | 


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
 **payload** | [**RecommendDocs**](RecommendDocs.md)|  | 

### Return type

[**DocumentRecommendRespModel**](DocumentRecommendRespModel.md)

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

var payload = new NucleusApi.SummarizeDocs(); // SummarizeDocs | 


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
 **payload** | [**SummarizeDocs**](SummarizeDocs.md)|  | 

### Return type

[**DocumentSummaryRespModel**](DocumentSummaryRespModel.md)

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

var payload = new NucleusApi.Consensus(); // Consensus | 


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
 **payload** | [**Consensus**](Consensus.md)|  | 

### Return type

[**TopicConsensusRespModel**](TopicConsensusRespModel.md)

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

var payload = new NucleusApi.TopicDelta(); // TopicDelta | 


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
 **payload** | [**TopicDelta**](TopicDelta.md)|  | 

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

var payload = new NucleusApi.Sentiment(); // Sentiment | 


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
 **payload** | [**Sentiment**](Sentiment.md)|  | 

### Return type

[**TopicSentimentRespModel**](TopicSentimentRespModel.md)

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

var payload = new NucleusApi.Summary(); // Summary | 


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
 **payload** | [**Summary**](Summary.md)|  | 

### Return type

[**TopicSummaryRespModel**](TopicSummaryRespModel.md)

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
  'metadata': "metadata_example" // String | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"}
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

