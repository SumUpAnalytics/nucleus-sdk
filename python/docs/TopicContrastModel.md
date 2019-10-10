# TopicContrastModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**metadata_selection** | **object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**time_period** | **str** | Alternative 1: Time period selection from now | [optional] 
**period_start** | **str** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **str** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**metadata_selection_contrast** | **object** | JSON object specifying the 2 classes subject to classification, of type: if based on content-selection {\&quot;content\&quot;: \&quot;word1 word2 ... wordN\&quot;} ; if based on other field {\&quot;metadata_field\&quot;: [\&quot;values_class1\&quot;, \&quot;values_class2\&quot;} | 
**excluded_docs** | **list[str]** |  | [optional] 
**syntax_variables** | **bool** | If True, the classifier will include syntax-related variables on top of content variables | [optional] [default to False]
**num_keywords** | **int** | Number of keywords for the contrasted topic that is extracted from the dataset. | [optional] 
**remove_redundancies** | **bool** | If True, this option removes quasi-duplicates from the analysis and retains only one copy of it. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


