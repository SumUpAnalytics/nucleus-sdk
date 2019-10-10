# DocumentNoveltyModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**custom_stop_words** | **list[str]** |  | [optional] 
**num_days_back** | **int** | Number of days from the latest date of the dataset, which are considered as foreground for the novelty analysis. | [optional] 
**novelty_threshold** | **float** | Value of novelty of a document above which a document is considered novel. This value should be between 0 and 1 and reflects the percentage of the document information unexplained by the background. | [optional] 
**metadata_selection** | **object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **str** | Alternative 1: Time period selection for the period considered as background for the novelty analysis | [optional] 
**period_start** | **str** | Alternative 2: Start date for the period considered as background for the novelty analysis. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **str** | Alternative 2: End date for the period considered as background for the novelty analysis. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**excluded_docs** | **list[str]** |  | [optional] 
**short_sentence_length** | **int** | The sentence length (in number of words) below which a sentence is excluded from novelty analysis. | [optional] 
**long_sentence_length** | **int** | The sentence length (in number of words) beyond which a sentence is excluded from novelty analysis. | [optional] 
**remove_redundancies** | **bool** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


