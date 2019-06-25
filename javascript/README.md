# nucleus_api

NucleusApi - JavaScript client for nucleus_api
Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://github.com/SumUpAnalytics/nucleus-sdk

- API version: v2.4.0
- Package version: v2.4.0

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
*NucleusApi.NucleusApi* | [**getListFilters**](docs/NucleusApi.md#getListFilters) | **GET** /filters | 
*NucleusApi.NucleusApi* | [**getUser**](docs/NucleusApi.md#getUser) | **GET** /users | 
*NucleusApi.NucleusApi* | [**postAppendJsonToDataset**](docs/NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
*NucleusApi.NucleusApi* | [**postAuthorConnectivityApi**](docs/NucleusApi.md#postAuthorConnectivityApi) | **POST** /topics/author_connectivity | 
*NucleusApi.NucleusApi* | [**postAvailableSecFilings**](docs/NucleusApi.md#postAvailableSecFilings) | **POST** /feeds/available_sec_filings | 
*NucleusApi.NucleusApi* | [**postBulkInsertJson**](docs/NucleusApi.md#postBulkInsertJson) | **POST** /datasets/bulk_insert_json | 
*NucleusApi.NucleusApi* | [**postCreateDatasetFromSecFilings**](docs/NucleusApi.md#postCreateDatasetFromSecFilings) | **POST** /feeds/create_dataset_from_sec_filings | 
*NucleusApi.NucleusApi* | [**postDatasetInfo**](docs/NucleusApi.md#postDatasetInfo) | **POST** /datasets/dataset_info | 
*NucleusApi.NucleusApi* | [**postDatasetTagging**](docs/NucleusApi.md#postDatasetTagging) | **POST** /datasets/dataset_tagging | 
*NucleusApi.NucleusApi* | [**postDeleteDataset**](docs/NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
*NucleusApi.NucleusApi* | [**postDeleteDocument**](docs/NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
*NucleusApi.NucleusApi* | [**postDeleteFilter**](docs/NucleusApi.md#postDeleteFilter) | **POST** /filters/delete_filter | 
*NucleusApi.NucleusApi* | [**postDocClassifyApi**](docs/NucleusApi.md#postDocClassifyApi) | **POST** /documents/document_classify | 
*NucleusApi.NucleusApi* | [**postDocDisplay**](docs/NucleusApi.md#postDocDisplay) | **POST** /documents/document_display | 
*NucleusApi.NucleusApi* | [**postDocInfo**](docs/NucleusApi.md#postDocInfo) | **POST** /documents/document_info | 
*NucleusApi.NucleusApi* | [**postDocRecommendApi**](docs/NucleusApi.md#postDocRecommendApi) | **POST** /documents/document_recommend | 
*NucleusApi.NucleusApi* | [**postDocSentimentApi**](docs/NucleusApi.md#postDocSentimentApi) | **POST** /documents/document_sentiment | 
*NucleusApi.NucleusApi* | [**postDocSummaryApi**](docs/NucleusApi.md#postDocSummaryApi) | **POST** /documents/document_summary | 
*NucleusApi.NucleusApi* | [**postDocumentContrastSummaryApi**](docs/NucleusApi.md#postDocumentContrastSummaryApi) | **POST** /documents/document_contrasted_summary | 
*NucleusApi.NucleusApi* | [**postExampleJob**](docs/NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
*NucleusApi.NucleusApi* | [**postLegacy**](docs/NucleusApi.md#postLegacy) | **POST** /legacy | 
*NucleusApi.NucleusApi* | [**postRenameDataset**](docs/NucleusApi.md#postRenameDataset) | **POST** /datasets/rename_dataset | 
*NucleusApi.NucleusApi* | [**postSaveFilter**](docs/NucleusApi.md#postSaveFilter) | **POST** /filters/save_filter | 
*NucleusApi.NucleusApi* | [**postTopicApi**](docs/NucleusApi.md#postTopicApi) | **POST** /topics/topics | 
*NucleusApi.NucleusApi* | [**postTopicConsensusApi**](docs/NucleusApi.md#postTopicConsensusApi) | **POST** /topics/topic_consensus | 
*NucleusApi.NucleusApi* | [**postTopicConsensusTransferApi**](docs/NucleusApi.md#postTopicConsensusTransferApi) | **POST** /topics/topic_consensus_transfer | 
*NucleusApi.NucleusApi* | [**postTopicContrastApi**](docs/NucleusApi.md#postTopicContrastApi) | **POST** /topics/topic_contrast | 
*NucleusApi.NucleusApi* | [**postTopicDeltaApi**](docs/NucleusApi.md#postTopicDeltaApi) | **POST** /topics/topic_delta | 
*NucleusApi.NucleusApi* | [**postTopicHistoricalAnalysisApi**](docs/NucleusApi.md#postTopicHistoricalAnalysisApi) | **POST** /topics/topic_historical | 
*NucleusApi.NucleusApi* | [**postTopicSentimentApi**](docs/NucleusApi.md#postTopicSentimentApi) | **POST** /topics/topic_sentiment | 
*NucleusApi.NucleusApi* | [**postTopicSentimentTransferApi**](docs/NucleusApi.md#postTopicSentimentTransferApi) | **POST** /topics/topic_sentiment_transfer | 
*NucleusApi.NucleusApi* | [**postTopicSummaryApi**](docs/NucleusApi.md#postTopicSummaryApi) | **POST** /topics/topic_summary | 
*NucleusApi.NucleusApi* | [**postTopicTransferApi**](docs/NucleusApi.md#postTopicTransferApi) | **POST** /topics/topic_transfer | 
*NucleusApi.NucleusApi* | [**postUploadFile**](docs/NucleusApi.md#postUploadFile) | **POST** /datasets/upload_file | 
*NucleusApi.NucleusApi* | [**postUploadUrl**](docs/NucleusApi.md#postUploadUrl) | **POST** /datasets/import_file_from_url | 
*NucleusApi.NucleusApi* | [**postUser**](docs/NucleusApi.md#postUser) | **POST** /users | 


## Documentation for Models

 - [NucleusApi.ApiCall](docs/ApiCall.md)
 - [NucleusApi.AppendJsonRespModel](docs/AppendJsonRespModel.md)
 - [NucleusApi.Appendjsonparams](docs/Appendjsonparams.md)
 - [NucleusApi.AuthorConnectL1RespModel](docs/AuthorConnectL1RespModel.md)
 - [NucleusApi.AuthorConnectL2RespModel](docs/AuthorConnectL2RespModel.md)
 - [NucleusApi.AuthorConnectRespModel](docs/AuthorConnectRespModel.md)
 - [NucleusApi.AuthorConnection](docs/AuthorConnection.md)
 - [NucleusApi.AvailableFilingsResponseModel](docs/AvailableFilingsResponseModel.md)
 - [NucleusApi.BulkInsertParams](docs/BulkInsertParams.md)
 - [NucleusApi.BulkInsertRespModel](docs/BulkInsertRespModel.md)
 - [NucleusApi.CreateSecDatasetResponseModel](docs/CreateSecDatasetResponseModel.md)
 - [NucleusApi.DatasetInfo](docs/DatasetInfo.md)
 - [NucleusApi.DatasetInfoModel](docs/DatasetInfoModel.md)
 - [NucleusApi.DatasetInfoRespModel](docs/DatasetInfoRespModel.md)
 - [NucleusApi.DatasetModel](docs/DatasetModel.md)
 - [NucleusApi.DatasetTagging](docs/DatasetTagging.md)
 - [NucleusApi.DatasetTaggingL1RespModel](docs/DatasetTaggingL1RespModel.md)
 - [NucleusApi.DatasetTaggingRespModel](docs/DatasetTaggingRespModel.md)
 - [NucleusApi.DeleteDatasetRespModel](docs/DeleteDatasetRespModel.md)
 - [NucleusApi.DeleteDocumentRespModel](docs/DeleteDocumentRespModel.md)
 - [NucleusApi.DeleteFilterModel](docs/DeleteFilterModel.md)
 - [NucleusApi.DeleteFilterRespModel](docs/DeleteFilterRespModel.md)
 - [NucleusApi.Deletedatasetmodel](docs/Deletedatasetmodel.md)
 - [NucleusApi.Deletedocumentmodel](docs/Deletedocumentmodel.md)
 - [NucleusApi.DocClassifyL1RespModel](docs/DocClassifyL1RespModel.md)
 - [NucleusApi.DocClassifyL2DRRespModel](docs/DocClassifyL2DRRespModel.md)
 - [NucleusApi.DocClassifyL2PMRespModel](docs/DocClassifyL2PMRespModel.md)
 - [NucleusApi.DocClassifyModel](docs/DocClassifyModel.md)
 - [NucleusApi.DocClassifyRespModel](docs/DocClassifyRespModel.md)
 - [NucleusApi.DocDisplay](docs/DocDisplay.md)
 - [NucleusApi.DocDisplayL1RespModel](docs/DocDisplayL1RespModel.md)
 - [NucleusApi.DocDisplayRespModel](docs/DocDisplayRespModel.md)
 - [NucleusApi.DocInfo](docs/DocInfo.md)
 - [NucleusApi.DocInfoRespModel](docs/DocInfoRespModel.md)
 - [NucleusApi.Document](docs/Document.md)
 - [NucleusApi.DocumentContrastSummaryL1Model](docs/DocumentContrastSummaryL1Model.md)
 - [NucleusApi.DocumentContrastSummaryL2Model](docs/DocumentContrastSummaryL2Model.md)
 - [NucleusApi.DocumentContrastSummaryModel](docs/DocumentContrastSummaryModel.md)
 - [NucleusApi.DocumentContrastSummaryRespModel](docs/DocumentContrastSummaryRespModel.md)
 - [NucleusApi.DocumentRecommendL1RespModel](docs/DocumentRecommendL1RespModel.md)
 - [NucleusApi.DocumentRecommendL2RespModel](docs/DocumentRecommendL2RespModel.md)
 - [NucleusApi.DocumentRecommendModel](docs/DocumentRecommendModel.md)
 - [NucleusApi.DocumentRecommendRespModel](docs/DocumentRecommendRespModel.md)
 - [NucleusApi.DocumentSentimentL1Model](docs/DocumentSentimentL1Model.md)
 - [NucleusApi.DocumentSentimentModel](docs/DocumentSentimentModel.md)
 - [NucleusApi.DocumentSentimentRespModel](docs/DocumentSentimentRespModel.md)
 - [NucleusApi.DocumentSummaryL1Model](docs/DocumentSummaryL1Model.md)
 - [NucleusApi.DocumentSummaryL2Model](docs/DocumentSummaryL2Model.md)
 - [NucleusApi.DocumentSummaryModel](docs/DocumentSummaryModel.md)
 - [NucleusApi.DocumentSummaryRespModel](docs/DocumentSummaryRespModel.md)
 - [NucleusApi.EdgarAvailableFields](docs/EdgarAvailableFields.md)
 - [NucleusApi.EdgarFields](docs/EdgarFields.md)
 - [NucleusApi.EdgarQuery](docs/EdgarQuery.md)
 - [NucleusApi.ExampleJobInnerResponse](docs/ExampleJobInnerResponse.md)
 - [NucleusApi.ExampleJobResponse](docs/ExampleJobResponse.md)
 - [NucleusApi.FilePropertyModel](docs/FilePropertyModel.md)
 - [NucleusApi.FilterModel](docs/FilterModel.md)
 - [NucleusApi.JobRespModel](docs/JobRespModel.md)
 - [NucleusApi.JobStatusRespModel](docs/JobStatusRespModel.md)
 - [NucleusApi.JsonPropertyModel](docs/JsonPropertyModel.md)
 - [NucleusApi.LegacyResponseModel](docs/LegacyResponseModel.md)
 - [NucleusApi.ListDatasetsModel](docs/ListDatasetsModel.md)
 - [NucleusApi.ListFiltersModel](docs/ListFiltersModel.md)
 - [NucleusApi.NestedDocInfoModel](docs/NestedDocInfoModel.md)
 - [NucleusApi.NestedTopicConsensusModel](docs/NestedTopicConsensusModel.md)
 - [NucleusApi.NestedTopicConsensusTransferModel](docs/NestedTopicConsensusTransferModel.md)
 - [NucleusApi.NestedTopicSentimentTransferModel](docs/NestedTopicSentimentTransferModel.md)
 - [NucleusApi.PostUserRespModel](docs/PostUserRespModel.md)
 - [NucleusApi.RenameDatasetRespModel](docs/RenameDatasetRespModel.md)
 - [NucleusApi.Renamedatasetmodel](docs/Renamedatasetmodel.md)
 - [NucleusApi.SaveFilterModel](docs/SaveFilterModel.md)
 - [NucleusApi.SaveFilterRespModel](docs/SaveFilterRespModel.md)
 - [NucleusApi.TopicConsensusModel](docs/TopicConsensusModel.md)
 - [NucleusApi.TopicConsensusRespModel](docs/TopicConsensusRespModel.md)
 - [NucleusApi.TopicConsensusTransferModel](docs/TopicConsensusTransferModel.md)
 - [NucleusApi.TopicConsensusTransferRespModel](docs/TopicConsensusTransferRespModel.md)
 - [NucleusApi.TopicContrastL1RespModel](docs/TopicContrastL1RespModel.md)
 - [NucleusApi.TopicContrastL2RespModel](docs/TopicContrastL2RespModel.md)
 - [NucleusApi.TopicContrastModel](docs/TopicContrastModel.md)
 - [NucleusApi.TopicContrastRespModel](docs/TopicContrastRespModel.md)
 - [NucleusApi.TopicDeltaL1RespModel](docs/TopicDeltaL1RespModel.md)
 - [NucleusApi.TopicDeltaL2RespModel](docs/TopicDeltaL2RespModel.md)
 - [NucleusApi.TopicDeltaModel](docs/TopicDeltaModel.md)
 - [NucleusApi.TopicDeltaRespModel](docs/TopicDeltaRespModel.md)
 - [NucleusApi.TopicHistoryL1RespModel](docs/TopicHistoryL1RespModel.md)
 - [NucleusApi.TopicHistoryModel](docs/TopicHistoryModel.md)
 - [NucleusApi.TopicHistoryRespModel](docs/TopicHistoryRespModel.md)
 - [NucleusApi.TopicL1RespModel](docs/TopicL1RespModel.md)
 - [NucleusApi.TopicL2RespModel](docs/TopicL2RespModel.md)
 - [NucleusApi.TopicRespModel](docs/TopicRespModel.md)
 - [NucleusApi.TopicSentimentL1RespModel](docs/TopicSentimentL1RespModel.md)
 - [NucleusApi.TopicSentimentModel](docs/TopicSentimentModel.md)
 - [NucleusApi.TopicSentimentRespModel](docs/TopicSentimentRespModel.md)
 - [NucleusApi.TopicSentimentTransferModel](docs/TopicSentimentTransferModel.md)
 - [NucleusApi.TopicSentimentTransferRespModel](docs/TopicSentimentTransferRespModel.md)
 - [NucleusApi.TopicSummaryL1RespModel](docs/TopicSummaryL1RespModel.md)
 - [NucleusApi.TopicSummaryL2RespModel](docs/TopicSummaryL2RespModel.md)
 - [NucleusApi.TopicSummaryModel](docs/TopicSummaryModel.md)
 - [NucleusApi.TopicSummaryRespModel](docs/TopicSummaryRespModel.md)
 - [NucleusApi.TopicTransferL1RespModel](docs/TopicTransferL1RespModel.md)
 - [NucleusApi.TopicTransferL2RespModel](docs/TopicTransferL2RespModel.md)
 - [NucleusApi.TopicTransferModel](docs/TopicTransferModel.md)
 - [NucleusApi.TopicTransferRespModel](docs/TopicTransferRespModel.md)
 - [NucleusApi.Topics](docs/Topics.md)
 - [NucleusApi.UploadFileRespModel](docs/UploadFileRespModel.md)
 - [NucleusApi.UploadURLModel](docs/UploadURLModel.md)
 - [NucleusApi.UploadUrlRespModel](docs/UploadUrlRespModel.md)
 - [NucleusApi.UrlPropertyModel](docs/UrlPropertyModel.md)
 - [NucleusApi.User](docs/User.md)
 - [NucleusApi.UserModel](docs/UserModel.md)


## Documentation for Authorization


### apikey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


Copyright 2019 SumUp Analytics, Inc
