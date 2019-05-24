# nucleus-api
Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://github.com/SumUpAnalytics/nucleus-sdk

- Package version: v2.0.2


## Requirements.

Python 3.5 or 3.6 is set up in a virtual environment. More details: https://docs.python.org/3/tutorial/venv.html. 
All commands in this documents assume running python from the virtual environment.

## Installation & Usage
### pip install
Run pip from Python virtual environment
```sh
pip install nucleus_api --upgrade
```

Then import the package:
```python
import nucleus_api 
```

## Getting Started

1. Go to the examples directory `cd examples`
1. An example using all APIs is provided in a Jupyter Notebook (all-api-examples-py.ipynb) and a Python script all-api-examples-py.py
1. Open the example in Jupyter Notebook or a text editor and update the lines below with provided host name and API key
    ```
    configuration.host = 'API_HOST_HERE'
    configuration.api_key['x-api-key'] = 'API_KEY_HERE'
    ```
1. Execute the example in Jupyter Notebook or use the command line: 'python3 all-api-examples-py.py'

## Guideline for Calibration
[Guideline for Calibration](examples/Guidelines%20for%20Calibrating%20Nucleus%20APIs.pdf) is available
in examples/(examples) directory.

##  Documentation for Helper Functions
[**upload_files**](HelperFunc.md#upload_files)  
[**upload_jsons**](HelperFunc.md#upload_jsons)  
[**upload_urls**](HelperFunc.md#upload_urls)  
[**summarize_file_url**](HelperFunc.md#summarize_file_url)  

## Documentation for APIs

All methods are in *NucleusApi* class  
All URIs are relative to *configuration.host*

### Dataset Management APIs
Method | HTTP request  
------------ | -------------  
[**post_append_json_to_dataset**](docs/NucleusApi.md#post_append_json_to_dataset) | **POST** /datasets/append_json_to_dataset | 
[**post_upload_file**](docs/NucleusApi.md#post_upload_file) | **POST** /datasets/upload_file | 
[**post_upload_url**](docs/NucleusApi.md#post_upload_url) | **POST** /datasets/import_file_from_url | 
[**get_list_datasets**](docs/NucleusApi.md#get_list_datasets) | **GET** /datasets | 
[**post_dataset_info**](docs/NucleusApi.md#post_dataset_info) | **POST** /datasets/dataset_info | 
[**post_delete_dataset**](docs/NucleusApi.md#post_delete_dataset) | **POST** /datasets/delete_dataset | 
[**post_delete_document**](docs/NucleusApi.md#post_delete_document) | **POST** /datasets/delete_document | 
[**post_rename_dataset**](docs/NucleusApi.md#post_rename_dataset) | **POST** /datasets/rename_dataset | 

### Topics Analysis APIs
Method | HTTP request 
------------ | -------------  
[**post_topic_api**](docs/NucleusApi.md#post_topic_api) | **POST** /topics/topics | 
[**post_topic_consensus_api**](docs/NucleusApi.md#post_topic_consensus_api) | **POST** /topics/topic_consensus | 
[**post_topic_sentiment_api**](docs/NucleusApi.md#post_topic_sentiment_api) | **POST** /topics/topic_sentiment | 
[**post_topic_summary_api**](docs/NucleusApi.md#post_topic_summary_api) | **POST** /topics/topic_summary | 

### Document Analysis APIs
Method | HTTP request 
------------ | -------------  
[**post_doc_display**](docs/NucleusApi.md#post_doc_display) | **POST** /documents/document_display | 
[**post_doc_info**](docs/NucleusApi.md#post_doc_info) | **POST** /documents/document_info | 
[**post_doc_recommend_api**](docs/NucleusApi.md#post_doc_recommend_api) | **POST** /documents/document_recommend | 
[**post_doc_sentiment_api**](docs/NucleusApi.md#post_doc_sentiment_api) | **POST** /documents/document_sentiment | 
[**post_doc_summary_api**](docs/NucleusApi.md#post_doc_summary_api) | **POST** /documents/document_summary | 

### Advanced APIs
Method | HTTP request 
------------- | ------------- 
[**post_author_connectivity_api**](docs/NucleusApi.md#post_author_connectivity_api) | **POST** /topics/author_connectivity | 
[**post_dataset_tagging**](docs/NucleusApi.md#post_dataset_tagging) | **POST** /datasets/dataset_tagging | 
[**post_topic_transfer_api**](docs/NucleusApi.md#post_topic_transfer_api) | **POST** /topics/topic_transfer | 
[**post_topic_sentiment_transfer_api**](docs/NucleusApi.md#post_topic_sentiment_transfer_api) | **POST** /topics/topic_sentiment_transfer | 
[**post_topic_consensus_transfer_api**](docs/NucleusApi.md#post_topic_consensus_transfer_api) | **POST** /topics/topic_consensus_transfer | 
[**post_topic_delta_api**](docs/NucleusApi.md#post_topic_delta_api) | **POST** /topics/topic_delta | 
[**post_topic_historical_analysis_api**](docs/NucleusApi.md#post_topic_historical_analysis_api) | **POST** /topics/topic_historical | 
[**post_topic_contrast_api**](docs/NucleusApi.md#post_topic_contrast_api) | **POST** /topics/topic_contrast | 
[**post_doc_classify_api**](docs/NucleusApi.md#post_doc_classify_api) | **POST** /documents/document_classify | 
[**post_document_contrast_summary_api**](docs/NucleusApi.md#post_document_contrast_summary_api) | **POST** /documents/document_contrasted_summary | 


## Documentation For Models
### Dataset Management Models
 - [AppendJsonRespModel](docs/AppendJsonRespModel.md)
 - [Appendjsonparams](docs/Appendjsonparams.md)
 - [UploadFileRespModel](docs/UploadFileRespModel.md)
 - [UploadURLModel](docs/UploadURLModel.md)
 - [UploadUrlRespModel](docs/UploadUrlRespModel.md)
 - [UrlPropertyModel](docs/UrlPropertyModel.md)
 - [DatasetInfo](docs/DatasetInfo.md)
 - [DatasetInfoModel](docs/DatasetInfoModel.md)
 - [DatasetInfoRespModel](docs/DatasetInfoRespModel.md)
 - [DeleteDatasetRespModel](docs/DeleteDatasetRespModel.md)
 - [DeleteDocumentRespModel](docs/DeleteDocumentRespModel.md)
 - [Deletedatasetmodel](docs/Deletedatasetmodel.md)
 - [Deletedocumentmodel](docs/Deletedocumentmodel.md)
 - [ListDatasetsModel](docs/ListDatasetsModel.md)
 - [RenameDatasetRespModel](docs/RenameDatasetRespModel.md)
 - [Renamedatasetmodel](docs/Renamedatasetmodel.md)

### Topics Analysis Models
 - [TopicConsensusModel](docs/TopicConsensusModel.md)
 - [TopicConsensusRespModel](docs/TopicConsensusRespModel.md)
 - [NestedTopicConsensusModel](docs/NestedTopicConsensusModel.md)
 - [TopicDeltaL1RespModel](docs/TopicDeltaL1RespModel.md)
 - [TopicDeltaL2RespModel](docs/TopicDeltaL2RespModel.md)
 - [TopicDeltaModel](docs/TopicDeltaModel.md)
 - [TopicDeltaRespModel](docs/TopicDeltaRespModel.md)
 - [TopicL1RespModel](docs/TopicL1RespModel.md)
 - [TopicL2RespModel](docs/TopicL2RespModel.md)
 - [TopicRespModel](docs/TopicRespModel.md)
 - [TopicSentimentL1RespModel](docs/TopicSentimentL1RespModel.md)
 - [TopicSentimentModel](docs/TopicSentimentModel.md)
 - [TopicSentimentRespModel](docs/TopicSentimentRespModel.md)
 - [TopicSummaryL1RespModel](docs/TopicSummaryL1RespModel.md)
 - [TopicSummaryL2RespModel](docs/TopicSummaryL2RespModel.md)
 - [TopicSummaryModel](docs/TopicSummaryModel.md)
 - [TopicSummaryRespModel](docs/TopicSummaryRespModel.md)
 - [Topics](docs/Topics.md)

### Document Analysis Management Models
 - [DocDisplay](docs/DocDisplay.md)
 - [DocDisplayL1RespModel](docs/DocDisplayL1RespModel.md)
 - [DocDisplayRespModel](docs/DocDisplayRespModel.md)
 - [DocInfo](docs/DocInfo.md)
 - [DocInfoRespModel](docs/DocInfoRespModel.md)
 - [Document](docs/Document.md)
 - [DocumentRecommendL1RespModel](docs/DocumentRecommendL1RespModel.md)
 - [DocumentRecommendL2RespModel](docs/DocumentRecommendL2RespModel.md)
 - [DocumentRecommendModel](docs/DocumentRecommendModel.md)
 - [DocumentRecommendRespModel](docs/DocumentRecommendRespModel.md)
 - [DocumentSentimentL1Model](docs/DocumentSentimentL1Model.md)
 - [DocumentSentimentModel](docs/DocumentSentimentModel.md)
 - [DocumentSentimentRespModel](docs/DocumentSentimentRespModel.md)
 - [DocumentSummaryL1Model](docs/DocumentSummaryL1Model.md)
 - [DocumentSummaryL2Model](docs/DocumentSummaryL2Model.md)
 - [DocumentSummaryModel](docs/DocumentSummaryModel.md)
 - [DocumentSummaryRespModel](docs/DocumentSummaryRespModel.md)
 - [NestedDocInfoModel](docs/NestedDocInfoModel.md)

### Advanced API Models
 - [AuthorConnectL1RespModel](docs/AuthorConnectL1RespModel.md)
 - [AuthorConnectL2RespModel](docs/AuthorConnectL2RespModel.md)
 - [AuthorConnectRespModel](docs/AuthorConnectRespModel.md)
 - [AuthorConnection](docs/AuthorConnection.md)
 - [DatasetTagging](docs/DatasetTagging.md)
 - [DatasetTaggingL1RespModel](docs/DatasetTaggingL1RespModel.md)
 - [DatasetTaggingRespModel](docs/DatasetTaggingRespModel.md)
 - [TopicTransferModel](docs/TopicTransferModel.md)
 - [TopicTransferRespModel](docs/TopicTransferRespModel.md)
 - [TopicTransferL1RespModel](docs/TopicTransferL1RespModel.md)
 - [TopicTransferL2RespModel](docs/TopicTransferL2RespModel.md)
 - [NestedTopicConsensusTransferModel](docs/NestedTopicConsensusTransferModel.md)
 - [NestedTopicSentimentTransferModel](docs/NestedTopicSentimentTransferModel.md)
 - [TopicConsensusTransferModel](docs/TopicConsensusTransferModel.md)
 - [TopicConsensusTransferRespModel](docs/TopicConsensusTransferRespModel.md)
 - [TopicSentimentTransferModel](docs/TopicSentimentTransferModel.md)
 - [TopicSentimentTransferRespModel](docs/TopicSentimentTransferRespModel.md)
 - [TopicHistoryModel](docs/TopicHistoryModel.md)
 - [TopicHistoryRespModel](docs/TopicHistoryRespModel.md)
 - [TopicHistoryL1RespModel](docs/TopicHistoryL1RespModel.md)
 - [TopicContrastL1RespModel](docs/TopicContrastL1RespModel.md)
 - [TopicContrastModel](docs/TopicContrastModel.md)
 - [TopicContrastRespModel](docs/TopicContrastRespModel.md)
 - [DocClassifyL1RespModel](docs/DocClassifyL1RespModel.md)
 - [DocClassifyL2RespModel](docs/DocClassifyL2RespModel.md)
 - [DocClassifyModel](docs/DocClassifyModel.md)
 - [DocClassifyRespModel](docs/DocClassifyRespModel.md)
 - [DocumentContrastSummaryL1Model](docs/DocumentContrastSummaryL1Model.md)
 - [DocumentContrastSummaryL2Model](docs/DocumentContrastSummaryL2Model.md)
 - [DocumentContrastSummaryModel](docs/DocumentContrastSummaryModel.md)
 - [DocumentContrastSummaryRespModel](docs/DocumentContrastSummaryRespModel.md)


Copyright 2019 SumUp Analytics, Inc

