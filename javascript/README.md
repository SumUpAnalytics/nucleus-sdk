# nucleus_api

NucleusApi - JavaScript client for nucleus_api
Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://www.sumup.ai/apis/#nucleus-documentation

- API version: v4.0.9
- Package version: v4.0.9
For more information, please visit [https://www.sumup.ai](https://www.sumup.ai)

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
*NucleusApi.NucleusApi* | [**getListForensics**](docs/NucleusApi.md#getListForensics) | **GET** /forensics | 
*NucleusApi.NucleusApi* | [**getUser**](docs/NucleusApi.md#getUser) | **GET** /users | 
*NucleusApi.NucleusApi* | [**postAdminAddUser**](docs/NucleusApi.md#postAdminAddUser) | **POST** /admin/add_user | 
*NucleusApi.NucleusApi* | [**postAdminDeleteUser**](docs/NucleusApi.md#postAdminDeleteUser) | **POST** /admin/delete_user | 
*NucleusApi.NucleusApi* | [**postAdminList**](docs/NucleusApi.md#postAdminList) | **POST** /admin/list | 
*NucleusApi.NucleusApi* | [**postAdminManageDataset**](docs/NucleusApi.md#postAdminManageDataset) | **POST** /admin/manage_dataset | 
*NucleusApi.NucleusApi* | [**postAdminUpdateUser**](docs/NucleusApi.md#postAdminUpdateUser) | **POST** /admin/update_user | 
*NucleusApi.NucleusApi* | [**postAppendJsonToDataset**](docs/NucleusApi.md#postAppendJsonToDataset) | **POST** /datasets/append_json_to_dataset | 
*NucleusApi.NucleusApi* | [**postAuthorConnectivityApi**](docs/NucleusApi.md#postAuthorConnectivityApi) | **POST** /topics/author_connectivity | 
*NucleusApi.NucleusApi* | [**postAvailableSecFilings**](docs/NucleusApi.md#postAvailableSecFilings) | **POST** /feeds/available_sec_filings | 
*NucleusApi.NucleusApi* | [**postBulkInsertJson**](docs/NucleusApi.md#postBulkInsertJson) | **POST** /datasets/bulk_insert_json | 
*NucleusApi.NucleusApi* | [**postCreateDatasetFromSecFilings**](docs/NucleusApi.md#postCreateDatasetFromSecFilings) | **POST** /feeds/create_dataset_from_sec_filings | 
*NucleusApi.NucleusApi* | [**postCustomTrackerApi**](docs/NucleusApi.md#postCustomTrackerApi) | **POST** /dashboard/custom_tracker | 
*NucleusApi.NucleusApi* | [**postDatasetInfo**](docs/NucleusApi.md#postDatasetInfo) | **POST** /datasets/dataset_info | 
*NucleusApi.NucleusApi* | [**postDatasetTagging**](docs/NucleusApi.md#postDatasetTagging) | **POST** /datasets/dataset_tagging | 
*NucleusApi.NucleusApi* | [**postDeleteDataset**](docs/NucleusApi.md#postDeleteDataset) | **POST** /datasets/delete_dataset | 
*NucleusApi.NucleusApi* | [**postDeleteDocument**](docs/NucleusApi.md#postDeleteDocument) | **POST** /datasets/delete_document | 
*NucleusApi.NucleusApi* | [**postDeleteFilter**](docs/NucleusApi.md#postDeleteFilter) | **POST** /filters/delete_filter | 
*NucleusApi.NucleusApi* | [**postDeleteForensic**](docs/NucleusApi.md#postDeleteForensic) | **POST** /forensics/delete_forensic | 
*NucleusApi.NucleusApi* | [**postDocClassifyApi**](docs/NucleusApi.md#postDocClassifyApi) | **POST** /documents/document_classify | 
*NucleusApi.NucleusApi* | [**postDocDisplay**](docs/NucleusApi.md#postDocDisplay) | **POST** /documents/document_display | 
*NucleusApi.NucleusApi* | [**postDocInfo**](docs/NucleusApi.md#postDocInfo) | **POST** /documents/document_info | 
*NucleusApi.NucleusApi* | [**postDocNewWordsApi**](docs/NucleusApi.md#postDocNewWordsApi) | **POST** /documents/document_new_words | 
*NucleusApi.NucleusApi* | [**postDocNoveltyApi**](docs/NucleusApi.md#postDocNoveltyApi) | **POST** /documents/document_novelty | 
*NucleusApi.NucleusApi* | [**postDocRecommendApi**](docs/NucleusApi.md#postDocRecommendApi) | **POST** /documents/document_recommend | 
*NucleusApi.NucleusApi* | [**postDocSentimentApi**](docs/NucleusApi.md#postDocSentimentApi) | **POST** /documents/document_sentiment | 
*NucleusApi.NucleusApi* | [**postDocSummaryApi**](docs/NucleusApi.md#postDocSummaryApi) | **POST** /documents/document_summary | 
*NucleusApi.NucleusApi* | [**postDocumentContrastSummaryApi**](docs/NucleusApi.md#postDocumentContrastSummaryApi) | **POST** /documents/document_contrasted_summary | 
*NucleusApi.NucleusApi* | [**postExampleJob**](docs/NucleusApi.md#postExampleJob) | **POST** /jobs/start_example_job | 
*NucleusApi.NucleusApi* | [**postKeyAuthorsApi**](docs/NucleusApi.md#postKeyAuthorsApi) | **POST** /dashboard/key_authors | 
*NucleusApi.NucleusApi* | [**postLegacy**](docs/NucleusApi.md#postLegacy) | **POST** /legacy | 
*NucleusApi.NucleusApi* | [**postMetadataAutocomplete**](docs/NucleusApi.md#postMetadataAutocomplete) | **POST** /datasets/metadata_autocomplete | 
*NucleusApi.NucleusApi* | [**postMetadataHistogram**](docs/NucleusApi.md#postMetadataHistogram) | **POST** /datasets/metadata_histogram | 
*NucleusApi.NucleusApi* | [**postRenameDataset**](docs/NucleusApi.md#postRenameDataset) | **POST** /datasets/rename_dataset | 
*NucleusApi.NucleusApi* | [**postSaveFilter**](docs/NucleusApi.md#postSaveFilter) | **POST** /filters/save_filter | 
*NucleusApi.NucleusApi* | [**postSaveForensic**](docs/NucleusApi.md#postSaveForensic) | **POST** /forensics/save_forensic | 
*NucleusApi.NucleusApi* | [**postSetupConnector**](docs/NucleusApi.md#postSetupConnector) | **POST** /connectors/setup_connector | 
*NucleusApi.NucleusApi* | [**postSmartAlertsApi**](docs/NucleusApi.md#postSmartAlertsApi) | **POST** /dashboard/smart_alerts | 
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
*NucleusApi.NucleusApi* | [**postUpdateDatasetMetadata**](docs/NucleusApi.md#postUpdateDatasetMetadata) | **POST** /datasets/update_dataset_metadata | 
*NucleusApi.NucleusApi* | [**postUpdateForensic**](docs/NucleusApi.md#postUpdateForensic) | **POST** /forensics/update_forensic | 
*NucleusApi.NucleusApi* | [**postUploadFile**](docs/NucleusApi.md#postUploadFile) | **POST** /datasets/upload_file | 
*NucleusApi.NucleusApi* | [**postUploadUrl**](docs/NucleusApi.md#postUploadUrl) | **POST** /datasets/upload_url | 


## Documentation for Models

 - [NucleusApi.AdminAddUserModel](docs/AdminAddUserModel.md)
 - [NucleusApi.AdminAddUserRespModel](docs/AdminAddUserRespModel.md)
 - [NucleusApi.AdminDeleteUserModel](docs/AdminDeleteUserModel.md)
 - [NucleusApi.AdminDeleteUserRespModel](docs/AdminDeleteUserRespModel.md)
 - [NucleusApi.AdminListModel](docs/AdminListModel.md)
 - [NucleusApi.AdminListRespModel](docs/AdminListRespModel.md)
 - [NucleusApi.AdminManageDatasetModel](docs/AdminManageDatasetModel.md)
 - [NucleusApi.AdminManageDatasetRespModel](docs/AdminManageDatasetRespModel.md)
 - [NucleusApi.AdminUpdateUserModel](docs/AdminUpdateUserModel.md)
 - [NucleusApi.AdminUpdateUserRespModel](docs/AdminUpdateUserRespModel.md)
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
 - [NucleusApi.CustomTrackerL1RespModel](docs/CustomTrackerL1RespModel.md)
 - [NucleusApi.CustomTrackerModel](docs/CustomTrackerModel.md)
 - [NucleusApi.CustomTrackerRespModel](docs/CustomTrackerRespModel.md)
 - [NucleusApi.DatasetInfo](docs/DatasetInfo.md)
 - [NucleusApi.DatasetInfoModel](docs/DatasetInfoModel.md)
 - [NucleusApi.DatasetInfoRespModel](docs/DatasetInfoRespModel.md)
 - [NucleusApi.DatasetRespModel](docs/DatasetRespModel.md)
 - [NucleusApi.DatasetTagging](docs/DatasetTagging.md)
 - [NucleusApi.DatasetTaggingL1RespModel](docs/DatasetTaggingL1RespModel.md)
 - [NucleusApi.DatasetTaggingRespModel](docs/DatasetTaggingRespModel.md)
 - [NucleusApi.DeleteDatasetModel](docs/DeleteDatasetModel.md)
 - [NucleusApi.DeleteDatasetRespModel](docs/DeleteDatasetRespModel.md)
 - [NucleusApi.DeleteDocumentModel](docs/DeleteDocumentModel.md)
 - [NucleusApi.DeleteDocumentRespModel](docs/DeleteDocumentRespModel.md)
 - [NucleusApi.DeleteFilterModel](docs/DeleteFilterModel.md)
 - [NucleusApi.DeleteFilterRespModel](docs/DeleteFilterRespModel.md)
 - [NucleusApi.DeleteForensicModel](docs/DeleteForensicModel.md)
 - [NucleusApi.DeleteForensicRespModel](docs/DeleteForensicRespModel.md)
 - [NucleusApi.DocClassifyL1RespModel](docs/DocClassifyL1RespModel.md)
 - [NucleusApi.DocClassifyL2DRRespModel](docs/DocClassifyL2DRRespModel.md)
 - [NucleusApi.DocClassifyL2PMRespModel](docs/DocClassifyL2PMRespModel.md)
 - [NucleusApi.DocClassifyModel](docs/DocClassifyModel.md)
 - [NucleusApi.DocClassifyRespModel](docs/DocClassifyRespModel.md)
 - [NucleusApi.DocDisplay](docs/DocDisplay.md)
 - [NucleusApi.DocDisplayL1RespModel](docs/DocDisplayL1RespModel.md)
 - [NucleusApi.DocDisplayRespModel](docs/DocDisplayRespModel.md)
 - [NucleusApi.DocInfo](docs/DocInfo.md)
 - [NucleusApi.DocInfoRespL1Model](docs/DocInfoRespL1Model.md)
 - [NucleusApi.DocInfoRespModel](docs/DocInfoRespModel.md)
 - [NucleusApi.Document](docs/Document.md)
 - [NucleusApi.DocumentContrastSummaryL1Model](docs/DocumentContrastSummaryL1Model.md)
 - [NucleusApi.DocumentContrastSummaryL2Model](docs/DocumentContrastSummaryL2Model.md)
 - [NucleusApi.DocumentContrastSummaryModel](docs/DocumentContrastSummaryModel.md)
 - [NucleusApi.DocumentContrastSummaryRespModel](docs/DocumentContrastSummaryRespModel.md)
 - [NucleusApi.DocumentNewWordsL1Model](docs/DocumentNewWordsL1Model.md)
 - [NucleusApi.DocumentNewWordsModel](docs/DocumentNewWordsModel.md)
 - [NucleusApi.DocumentNewWordsRespModel](docs/DocumentNewWordsRespModel.md)
 - [NucleusApi.DocumentNoveltyL1Model](docs/DocumentNoveltyL1Model.md)
 - [NucleusApi.DocumentNoveltyModel](docs/DocumentNoveltyModel.md)
 - [NucleusApi.DocumentNoveltyRespModel](docs/DocumentNoveltyRespModel.md)
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
 - [NucleusApi.ForensicModel](docs/ForensicModel.md)
 - [NucleusApi.JobRespModel](docs/JobRespModel.md)
 - [NucleusApi.JsonPropertyModel](docs/JsonPropertyModel.md)
 - [NucleusApi.KeyAuthorsL1RespModel](docs/KeyAuthorsL1RespModel.md)
 - [NucleusApi.KeyAuthorsL2RespModel](docs/KeyAuthorsL2RespModel.md)
 - [NucleusApi.KeyAuthorsModel](docs/KeyAuthorsModel.md)
 - [NucleusApi.KeyAuthorsRespModel](docs/KeyAuthorsRespModel.md)
 - [NucleusApi.LegacyResponseModel](docs/LegacyResponseModel.md)
 - [NucleusApi.ListDatasetsRespModel](docs/ListDatasetsRespModel.md)
 - [NucleusApi.ListFiltersModel](docs/ListFiltersModel.md)
 - [NucleusApi.ListForensicsL1RespModel](docs/ListForensicsL1RespModel.md)
 - [NucleusApi.ListForensicsRespModel](docs/ListForensicsRespModel.md)
 - [NucleusApi.MetadataAutocomplete](docs/MetadataAutocomplete.md)
 - [NucleusApi.MetadataAutocompleteRespModel](docs/MetadataAutocompleteRespModel.md)
 - [NucleusApi.MetadataHistogram](docs/MetadataHistogram.md)
 - [NucleusApi.MetadataHistogramRespModel](docs/MetadataHistogramRespModel.md)
 - [NucleusApi.NestedTopicConsensusModel](docs/NestedTopicConsensusModel.md)
 - [NucleusApi.NestedTopicConsensusTransferModel](docs/NestedTopicConsensusTransferModel.md)
 - [NucleusApi.NestedTopicSentimentTransferModel](docs/NestedTopicSentimentTransferModel.md)
 - [NucleusApi.RenameDatasetModel](docs/RenameDatasetModel.md)
 - [NucleusApi.RenameDatasetRespModel](docs/RenameDatasetRespModel.md)
 - [NucleusApi.SaveFilterModel](docs/SaveFilterModel.md)
 - [NucleusApi.SaveFilterRespModel](docs/SaveFilterRespModel.md)
 - [NucleusApi.SaveForensicRespModel](docs/SaveForensicRespModel.md)
 - [NucleusApi.SetupConnectorModel](docs/SetupConnectorModel.md)
 - [NucleusApi.SetupConnectorRespModel](docs/SetupConnectorRespModel.md)
 - [NucleusApi.SmartAlertsL1RespModel](docs/SmartAlertsL1RespModel.md)
 - [NucleusApi.SmartAlertsL2RespModel](docs/SmartAlertsL2RespModel.md)
 - [NucleusApi.SmartAlertsModel](docs/SmartAlertsModel.md)
 - [NucleusApi.SmartAlertsRespModel](docs/SmartAlertsRespModel.md)
 - [NucleusApi.TopicConsensusModel](docs/TopicConsensusModel.md)
 - [NucleusApi.TopicConsensusRespModel](docs/TopicConsensusRespModel.md)
 - [NucleusApi.TopicConsensusTransferModel](docs/TopicConsensusTransferModel.md)
 - [NucleusApi.TopicConsensusTransferRespModel](docs/TopicConsensusTransferRespModel.md)
 - [NucleusApi.TopicContrastL1RespModel](docs/TopicContrastL1RespModel.md)
 - [NucleusApi.TopicContrastL21RespModel](docs/TopicContrastL21RespModel.md)
 - [NucleusApi.TopicContrastL22RespModel](docs/TopicContrastL22RespModel.md)
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
 - [NucleusApi.UpdateDatasetMetadataModel](docs/UpdateDatasetMetadataModel.md)
 - [NucleusApi.UpdateDatasetMetadataRespModel](docs/UpdateDatasetMetadataRespModel.md)
 - [NucleusApi.UpdateForensicModel](docs/UpdateForensicModel.md)
 - [NucleusApi.UpdateForensicsL1RespModel](docs/UpdateForensicsL1RespModel.md)
 - [NucleusApi.UploadFileRespModel](docs/UploadFileRespModel.md)
 - [NucleusApi.UploadURLModel](docs/UploadURLModel.md)
 - [NucleusApi.UploadUrlRespModel](docs/UploadUrlRespModel.md)
 - [NucleusApi.UrlPropertyModel](docs/UrlPropertyModel.md)
 - [NucleusApi.UserModel](docs/UserModel.md)


## Documentation for Authorization


### apikey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


Copyright 2018-2020 SumUp Analytics, Inc
