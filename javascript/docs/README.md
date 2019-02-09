# nucleus_api

NucleusApi - JavaScript client for nucleus_api
Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://github.com/SumUpAnalytics/nucleus-sdk

- API version: v0.1.7
- Package version: v0.1.7

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

Run the following command to install the latest version of the sdk:

```shell
npm install nucleus_api@latest --save --force
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var NucleusApi = require('nucleus_api');

var my_instance = new NucleusApi.ApiClient("http://localhost:5000", "YOUR_API_KEY")
var api = new NucleusApi.NucleusApi(my_instance)


api.postExampleJob("purple", 5, function (error, data, response) {
    if (error) {console.log(error);return;}
    console.log(data);
}, function(prog) {
    console.log("Progress:", prog);
})

```

The legacy api's can be called using `callLegacyApi`, as follows:

```javascript
api.callLegacyApi("topic_spot_metrics_api.topic_spot_metrics_api",{dataset:"my_dataset"}, function (error, data, response) {
    if (error) {console.log(error);return;}
    console.log(data);
}, function(prog) {
    console.log("Progress:", prog);
})
```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:5000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NucleusApi.NucleusApi* | [**getJob**](docs/NucleusApi.md#getJob) | **GET** /jobs | 
*NucleusApi.NucleusApi* | [**getListDatasets**](docs/NucleusApi.md#getListDatasets) | **GET** /datasets | 
*NucleusApi.NucleusApi* | [**getUser**](docs/NucleusApi.md#getUser) | **GET** /users | 
*NucleusApi.NucleusApi* | [**postAppendJsonToDataset**](docs/NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
*NucleusApi.NucleusApi* | [**postAuthorConnectivityApi**](docs/NucleusApi.md#postAuthorConnectivityApi) | **POST** /topics/author_connectivity | 
*NucleusApi.NucleusApi* | [**postDatasetInfo**](docs/NucleusApi.md#postDatasetInfo) | **POST** /datasets/dataset_info | 
*NucleusApi.NucleusApi* | [**postDeleteDataset**](docs/NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
*NucleusApi.NucleusApi* | [**postDeleteDocument**](docs/NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
*NucleusApi.NucleusApi* | [**postDocDisplay**](docs/NucleusApi.md#postDocDisplay) | **POST** /documents/document_display | 
*NucleusApi.NucleusApi* | [**postDocInfo**](docs/NucleusApi.md#postDocInfo) | **POST** /documents/document_info | 
*NucleusApi.NucleusApi* | [**postDocRecommendApi**](docs/NucleusApi.md#postDocRecommendApi) | **POST** /documents/document_recommend | 
*NucleusApi.NucleusApi* | [**postDocSummaryApi**](docs/NucleusApi.md#postDocSummaryApi) | **POST** /documents/document_summary | 
*NucleusApi.NucleusApi* | [**postExampleJob**](docs/NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
*NucleusApi.NucleusApi* | [**postLegacy**](docs/NucleusApi.md#postLegacy) | **POST** /legacy | 
*NucleusApi.NucleusApi* | [**postTopicApi**](docs/NucleusApi.md#postTopicApi) | **POST** /topics/topics | 
*NucleusApi.NucleusApi* | [**postTopicConsensusApi**](docs/NucleusApi.md#postTopicConsensusApi) | **POST** /topics/topic_consensus | 
*NucleusApi.NucleusApi* | [**postTopicDeltaApi**](docs/NucleusApi.md#postTopicDeltaApi) | **POST** /topics/topic_delta | 
*NucleusApi.NucleusApi* | [**postTopicHistoricalAnalysisApi**](docs/NucleusApi.md#postTopicHistoricalAnalysisApi) | **POST** /topics/topic_historical | 
*NucleusApi.NucleusApi* | [**postTopicSentimentApi**](docs/NucleusApi.md#postTopicSentimentApi) | **POST** /topics/topic_sentiment | 
*NucleusApi.NucleusApi* | [**postTopicSummaryApi**](docs/NucleusApi.md#postTopicSummaryApi) | **POST** /topics/topic_summary | 
*NucleusApi.NucleusApi* | [**postUploadFile**](docs/NucleusApi.md#postUploadFile) | **POST** /datasets/upload_file | 
*NucleusApi.NucleusApi* | [**postUploadUrl**](docs/NucleusApi.md#postUploadUrl) | **POST** /datasets/import_file_from_url | 
*NucleusApi.NucleusApi* | [**postUser**](docs/NucleusApi.md#postUser) | **POST** /users | 


## Documentation for Models

 - [NucleusApi.ApiCall](docs/ApiCall.md)
 - [NucleusApi.AppendJsonRespModel](docs/AppendJsonRespModel.md)
 - [NucleusApi.Appendjsonparams](docs/Appendjsonparams.md)
 - [NucleusApi.AuthorConnectRespModel](docs/AuthorConnectRespModel.md)
 - [NucleusApi.AuthorConnection](docs/AuthorConnection.md)
 - [NucleusApi.Consensus](docs/Consensus.md)
 - [NucleusApi.DatasetInfo](docs/DatasetInfo.md)
 - [NucleusApi.DatasetInfoModel](docs/DatasetInfoModel.md)
 - [NucleusApi.DatasetInfoRespModel](docs/DatasetInfoRespModel.md)
 - [NucleusApi.DeleteDatasetRespModel](docs/DeleteDatasetRespModel.md)
 - [NucleusApi.DeleteDocumentRespModel](docs/DeleteDocumentRespModel.md)
 - [NucleusApi.Deletedatasetmodel](docs/Deletedatasetmodel.md)
 - [NucleusApi.Deletedocumentmodel](docs/Deletedocumentmodel.md)
 - [NucleusApi.DocDisplay](docs/DocDisplay.md)
 - [NucleusApi.DocDisplayRespModel](docs/DocDisplayRespModel.md)
 - [NucleusApi.DocInfo](docs/DocInfo.md)
 - [NucleusApi.DocInfoRespModel](docs/DocInfoRespModel.md)
 - [NucleusApi.Document](docs/Document.md)
 - [NucleusApi.DocumentRecommendRespModel](docs/DocumentRecommendRespModel.md)
 - [NucleusApi.DocumentSummaryModel](docs/DocumentSummaryModel.md)
 - [NucleusApi.DocumentSummaryRespModel](docs/DocumentSummaryRespModel.md)
 - [NucleusApi.ExampleJobResponse](docs/ExampleJobResponse.md)
 - [NucleusApi.JobRespModel](docs/JobRespModel.md)
 - [NucleusApi.LegacyResponseModel](docs/LegacyResponseModel.md)
 - [NucleusApi.ListDatasetsModel](docs/ListDatasetsModel.md)
 - [NucleusApi.NestedAuthorConnect](docs/NestedAuthorConnect.md)
 - [NucleusApi.NestedAuthorConnect0](docs/NestedAuthorConnect0.md)
 - [NucleusApi.NestedDocDispModel](docs/NestedDocDispModel.md)
 - [NucleusApi.NestedDocInfoModel](docs/NestedDocInfoModel.md)
 - [NucleusApi.NestedDocRecModel](docs/NestedDocRecModel.md)
 - [NucleusApi.NestedDocumentSummaryModel](docs/NestedDocumentSummaryModel.md)
 - [NucleusApi.NestedSummaryModel](docs/NestedSummaryModel.md)
 - [NucleusApi.NestedTopicConsensusModel](docs/NestedTopicConsensusModel.md)
 - [NucleusApi.NestedTopicDeltaModel](docs/NestedTopicDeltaModel.md)
 - [NucleusApi.NestedTopicHistModel](docs/NestedTopicHistModel.md)
 - [NucleusApi.NestedTopicSentimentModel](docs/NestedTopicSentimentModel.md)
 - [NucleusApi.NestedTopicSummaryModel](docs/NestedTopicSummaryModel.md)
 - [NucleusApi.PostUserRespModel](docs/PostUserRespModel.md)
 - [NucleusApi.RecommendDocs](docs/RecommendDocs.md)
 - [NucleusApi.Sentiment](docs/Sentiment.md)
 - [NucleusApi.SummarizeDocs](docs/SummarizeDocs.md)
 - [NucleusApi.Summary](docs/Summary.md)
 - [NucleusApi.TopicConsensusRespModel](docs/TopicConsensusRespModel.md)
 - [NucleusApi.TopicDelta](docs/TopicDelta.md)
 - [NucleusApi.TopicDeltaRespModel](docs/TopicDeltaRespModel.md)
 - [NucleusApi.TopicHistoryModel](docs/TopicHistoryModel.md)
 - [NucleusApi.TopicHistoryRespModel](docs/TopicHistoryRespModel.md)
 - [NucleusApi.TopicL1RespModel](docs/TopicL1RespModel.md)
 - [NucleusApi.TopicRecommendModel](docs/TopicRecommendModel.md)
 - [NucleusApi.TopicRespModel](docs/TopicRespModel.md)
 - [NucleusApi.TopicSentimentRespModel](docs/TopicSentimentRespModel.md)
 - [NucleusApi.TopicSummaryRespModel](docs/TopicSummaryRespModel.md)
 - [NucleusApi.Topics](docs/Topics.md)
 - [NucleusApi.UploadFileRespModel](docs/UploadFileRespModel.md)
 - [NucleusApi.UploadURLModel](docs/UploadURLModel.md)
 - [NucleusApi.UploadUrlRespModel](docs/UploadUrlRespModel.md)
 - [NucleusApi.User](docs/User.md)
 - [NucleusApi.UserModel](docs/UserModel.md)


## Documentation for Authorization


### apikey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


Copyright 2019 SumUp Analytics, Inc
