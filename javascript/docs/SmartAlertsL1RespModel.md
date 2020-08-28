# NucleusApi.SmartAlertsL1RespModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **String** | Query analyzed. If no query was provided, then these are the hot topics. | [optional] 
**novel_docs** | [**[SmartAlertsL2RespModel]**](SmartAlertsL2RespModel.md) |  | [optional] 
**new_words** | **[String]** | New words in the foreground | [optional] 
**new_sents** | **[String]** | Sentences from the foreground containing new words | [optional] 
**new_sents_titles** | **[String]** | Titles of documents from the foreground containing new words | [optional] 
**new_sents_urls** | **[String]** | URLs of documents from the foreground containing new words | [optional] 
**new_sents_docids** | **[String]** | doc_ids of documents from the foreground containing new words | [optional] 


