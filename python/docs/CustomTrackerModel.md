# CustomTrackerModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**num_topics** | **int** | Number of topics to be extracted from the dataset per query to aggregate back into a tracker. | [optional] 
**num_keywords** | **int** | Number of keywords per topic that is extracted from the dataset per query. | [optional] 
**metadata_selection** | **object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **str** | Alternative 1: Time period selection | [optional] 
**period_start** | **str** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **str** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**n_steps** | **int** | Number of steps in the historical analysis over the requested period. Each step is such that they contain an equal number of documents. | [optional] 
**excluded_docs** | **list[str]** |  | [optional] 
**custom_dict_file** | **object** | Custom sentiment dictionary JSON file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


