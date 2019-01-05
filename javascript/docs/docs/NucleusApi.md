# NucleusApi.NucleusApi

All URIs are relative to *https://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthorConnectivityApi**](NucleusApi.md#getAuthorConnectivityApi) | **GET** /topics/author_connectivity | 
[**getDatasetInfo**](NucleusApi.md#getDatasetInfo) | **GET** /datasets/dataset_info | 
[**getDocDisplay**](NucleusApi.md#getDocDisplay) | **GET** /documents/document_display | 
[**getDocInfo**](NucleusApi.md#getDocInfo) | **GET** /documents/document_info | 
[**getDocRecommendApi**](NucleusApi.md#getDocRecommendApi) | **GET** /documents/document_recommend | 
[**getDocSummaryApi**](NucleusApi.md#getDocSummaryApi) | **GET** /documents/document_summary | 
[**getJob**](NucleusApi.md#getJob) | **GET** /jobs | 
[**getListDatasets**](NucleusApi.md#getListDatasets) | **GET** /datasets | 
[**getTopicApi**](NucleusApi.md#getTopicApi) | **GET** /topics/topics | 
[**getTopicDeltaApi**](NucleusApi.md#getTopicDeltaApi) | **GET** /topics/topic_delta | 
[**getTopicSummaryApi**](NucleusApi.md#getTopicSummaryApi) | **GET** /topics/topic_summary | 
[**getUser**](NucleusApi.md#getUser) | **GET** /users | 
[**postAppendJsonToDataset**](NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
[**postDeleteDataset**](NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
[**postDeleteDocument**](NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
[**postExampleJob**](NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
[**postLegacy**](NucleusApi.md#postLegacy) | **POST** /legacy | 
[**postTopicConsensusApi**](NucleusApi.md#postTopicConsensusApi) | **POST** /topics/topic_consensus | 
[**postTopicHistoricalAnalysisApi**](NucleusApi.md#postTopicHistoricalAnalysisApi) | **POST** /topics/topic_historical | 
[**postTopicSentimentApi**](NucleusApi.md#postTopicSentimentApi) | **POST** /topics/topic_sentiment | 
[**postUploadFile**](NucleusApi.md#postUploadFile) | **POST** /datasets/upload_file | 
[**postUploadUrl**](NucleusApi.md#postUploadUrl) | **POST** /datasets/import_file_from_url | 
[**postUser**](NucleusApi.md#postUser) | **POST** /users | 


<a name="getAuthorConnectivityApi"></a>
# **getAuthorConnectivityApi**
> AuthorConnectRespModel getAuthorConnectivityApi(dataset, targetAuthor, timePeriod, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var targetAuthor = "targetAuthor_example"; // String | Name of the author to be analyzed.

var timePeriod = "timePeriod_example"; // String | Time period selection

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of words possibly used by the target author that are considered not information-bearing.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getAuthorConnectivityApi(dataset, targetAuthor, timePeriod, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **targetAuthor** | **String**| Name of the author to be analyzed. | 
 **timePeriod** | **String**| Time period selection | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of words possibly used by the target author that are considered not information-bearing. | [optional] 
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**AuthorConnectRespModel**](AuthorConnectRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getDatasetInfo"></a>
# **getDatasetInfo**
> DatasetInfoRespModel getDatasetInfo(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example" // String | Time period selection
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDatasetInfo(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. | [optional] 
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 

### Return type

[**DatasetInfoRespModel**](DatasetInfoRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getDocDisplay"></a>
# **getDocDisplay**
> DocDisplayRespModel getDocDisplay(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'docTitles': "docTitles_example", // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
  'docIds': "docIds_example" // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDocDisplay(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **docTitles** | **String**| The title of the documents on which info is requested. Example: [ \&quot;title 1\&quot;, \&quot;title 2\&quot; ]  | [optional] 
 **docIds** | **String**| The docid of the documents on which info is requested. Example:[ \&quot;docid1, docid2\&quot; ] | [optional] 

### Return type

[**DocDisplayRespModel**](DocDisplayRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getDocInfo"></a>
# **getDocInfo**
> DocInfoRespModel getDocInfo(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'docTitles': "docTitles_example", // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
  'docIds': "docIds_example" // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDocInfo(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **docTitles** | **String**| The title of the documents on which info is requested. Example: [ \&quot;title 1\&quot;, \&quot;title 2\&quot; ]  | [optional] 
 **docIds** | **String**| The docid of the documents on which info is requested. Example:[ \&quot;docid1, docid2\&quot; ] | [optional] 

### Return type

[**DocInfoRespModel**](DocInfoRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getDocRecommendApi"></a>
# **getDocRecommendApi**
> DocumentRecommendRespModel getDocRecommendApi(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words.
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'numDocs': 20, // Number | Number of desired recommended docs per topic.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example", // String | Time period selection
  'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDocRecommendApi(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words. | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **numDocs** | **Number**| Number of desired recommended docs per topic. | [optional] [default to 20]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**DocumentRecommendRespModel**](DocumentRecommendRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getDocSummaryApi"></a>
# **getDocSummaryApi**
> DocumentSummaryRespModel getDocSummaryApi(dataset, docTitle, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var docTitle = "docTitle_example"; // String | The title of the document to be summarized.

var opts = { 
  'customStopWords': "customStopWords_example", // String | List of stop words
  'summaryLength': 6, // Number | The maximum number of bullet points a user wants to see in the document summary.
  'contextAmount': 0 // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDocSummaryApi(dataset, docTitle, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **docTitle** | **String**| The title of the document to be summarized. | 
 **customStopWords** | **String**| List of stop words | [optional] 
 **summaryLength** | **Number**| The maximum number of bullet points a user wants to see in the document summary. | [optional] [default to 6]
 **contextAmount** | **Number**| The number of sentences surrounding key summary sentences in the documents that they come from. | [optional] [default to 0]

### Return type

[**DocumentSummaryRespModel**](DocumentSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

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

<a name="getTopicApi"></a>
# **getTopicApi**
> TopicRespModel getTopicApi(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words.
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example", // String | Time period selection
  'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getTopicApi(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words. | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicRespModel**](TopicRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getTopicDeltaApi"></a>
# **getTopicDeltaApi**
> TopicDeltaRespModel getTopicDeltaApi(dataset, timeStartT0, timeEndT0, timeStartT1, timeEndT1, opts)



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

var dataset = "dataset_example"; // String | Dataset with a time series component. These docs should reference a universe of entities that overlaps through time.

var timeStartT0 = "timeStartT0_example"; // String | Start date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 

var timeEndT0 = "timeEndT0_example"; // String | End date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 

var timeStartT1 = "timeStartT1_example"; // String | Start date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 

var timeEndT1 = "timeEndT1_example"; // String | End date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words.
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getTopicDeltaApi(dataset, timeStartT0, timeEndT0, timeStartT1, timeEndT1, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset with a time series component. These docs should reference a universe of entities that overlaps through time. | 
 **timeStartT0** | **String**| Start date for the start-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **timeEndT0** | **String**| End date for the start-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **timeStartT1** | **String**| Start date for the end-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **timeEndT1** | **String**| End date for the end-of-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words. | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicDeltaRespModel**](TopicDeltaRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getTopicSummaryApi"></a>
# **getTopicSummaryApi**
> TopicSummaryRespModel getTopicSummaryApi(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset and summarized.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example", // String | Time period selection
  'summaryLength': 6, // Number | The maximum number of bullet points a user wants to see in each topic summary.
  'contextAmount': 0, // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
  'numDocs': 20, // Number | The maximum number of key documents to use for summarization.
  'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getTopicSummaryApi(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset and summarized. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 
 **summaryLength** | **Number**| The maximum number of bullet points a user wants to see in each topic summary. | [optional] [default to 6]
 **contextAmount** | **Number**| The number of sentences surrounding key summary sentences in the documents that they come from. | [optional] [default to 0]
 **numDocs** | **Number**| The maximum number of key documents to use for summarization. | [optional] [default to 20]
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 

### Return type

[**TopicSummaryRespModel**](TopicSummaryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

<a name="getUser"></a>
# **getUser**
> UserModel getUser(userEmail, password)



Use this API to authenticate. If the password is correct, returns the user details, including the user&#39;s api key.

### Example
```javascript
var NucleusApi = require('nucleus_api');

var apiInstance = new NucleusApi.NucleusApi();

var userEmail = "userEmail_example"; // String | Email of the user to authenticate. 

var password = "password_example"; // String | Plaintext password of the user to authenticate. 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getUser(userEmail, password, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userEmail** | **String**| Email of the user to authenticate.  | 
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

<a name="postExampleJob"></a>
# **postExampleJob**
> ExampleJobResponse postExampleJob(color, waitTime)



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

var waitTime = 0; // Number | Seconds to wait before returning the result


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postExampleJob(color, waitTime, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **String**| A color | 
 **waitTime** | **Number**| Seconds to wait before returning the result | [default to 0]

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

<a name="postTopicConsensusApi"></a>
# **postTopicConsensusApi**
> TopicConsensusRespModel postTopicConsensusApi(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example", // String | Time period selection
  'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
  'customDictFile': "/path/to/file.txt" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicConsensusApi(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **customDictFile** | **File**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicConsensusRespModel**](TopicConsensusRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="postTopicHistoricalAnalysisApi"></a>
# **postTopicHistoricalAnalysisApi**
> TopicHistoryRespModel postTopicHistoricalAnalysisApi(dataset, timePeriod, updatePeriod, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var timePeriod = "1M"; // String | Time period selection

var updatePeriod = "d"; // String | Frequency at which the historical anlaysis is performed

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'incStep': 1, // Number | Number of increments of the udpate period in between two historical computations.
  'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
  'customDictFile': "/path/to/file.txt" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicHistoricalAnalysisApi(dataset, timePeriod, updatePeriod, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **timePeriod** | **String**| Time period selection | [default to 1M]
 **updatePeriod** | **String**| Frequency at which the historical anlaysis is performed | [default to d]
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **incStep** | **Number**| Number of increments of the udpate period in between two historical computations. | [optional] [default to 1]
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **customDictFile** | **File**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicHistoryRespModel**](TopicHistoryRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="postTopicSentimentApi"></a>
# **postTopicSentimentApi**
> TopicSentimentRespModel postTopicSentimentApi(dataset, opts)



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

var dataset = "dataset_example"; // String | Dataset name.

var opts = { 
  'query': "query_example", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  'customStopWords': "customStopWords_example", // String | List of stop words
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "timePeriod_example", // String | Time period selection
  'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
  'customDictFile': "/path/to/file.txt" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postTopicSentimentApi(dataset, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Dataset name. | 
 **query** | **String**| Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
 **customStopWords** | **String**| List of stop words | [optional] 
 **numTopics** | **Number**| Number of topics to be extracted from the dataset. | [optional] [default to 8]
 **numKeywords** | **Number**| Number of keywords per topic that is extracted from the dataset. | [optional] [default to 8]
 **metadataSelection** | **String**| json object of {\&quot;metadata_field\&quot;:[\&quot;selected_values\&quot;]} | [optional] 
 **timePeriod** | **String**| Time period selection | [optional] 
 **excludedDocs** | **String**| List of document IDs that should be excluded from the analysis. Example, \&quot;docid1, docid2, ..., docidN\&quot;  | [optional] 
 **customDictFile** | **File**| Custom sentiment dictionary JSON file. | [optional] 

### Return type

[**TopicSentimentRespModel**](TopicSentimentRespModel.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

