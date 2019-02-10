# TopicDeltaModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**query** | **str** | Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**num_topics** | **int** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **int** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**period_0_start** | **str** | Start date for the initial-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_0_end** | **str** | End date for the initial-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_1_start** | **str** | Start date for the final-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_1_end** | **str** | End date for the final-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**excluded_docs** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


