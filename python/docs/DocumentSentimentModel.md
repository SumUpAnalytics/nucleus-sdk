# DocumentSentimentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**doc_title** | **str** | The title of the document to be analyzed. | 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**num_topics** | **int** | Number of topics to be extracted from the document to estimate the document&#39; sentiment. | [optional] 
**num_keywords** | **int** | Number of keywords per topic that is extracted from the document. | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**custom_dict_file** | **object** | Custom sentiment dictionary JSON file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


