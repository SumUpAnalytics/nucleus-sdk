# TopicTransferModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset0** | **str** | Name of reference dataset, on which topics are extracted. | 
**dataset1** | **str** | Alternative 1: Name of validation dataset, on which topics are applied. Only pass in this argument if the validation dataset has been separately created. | [optional] 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**num_topics** | **int** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **int** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**period_0_start** | **str** | Alternative 2: Start date for the reference dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_0_end** | **str** | Alternative 2: End date for the reference dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_1_start** | **str** | Alternative 2: Start date for the validation dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_1_end** | **str** | Alternative 2: End date for the validation dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**excluded_docs** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


