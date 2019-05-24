# DocClassifyModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Dataset name. | 
**query** | **str** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**fixed_topics** | **object** | JSON object specifying the contrasting topic that is exogenously fixed, of type {\&quot;keywords\&quot;: [\&quot;keyword_1\&quot;, \&quot;keyword_2\&quot;, \&quot;keyword_3\&quot;], \&quot;weights\&quot;: [weight_1, weight_2, weight_3]} | 
**metadata_selection** | **object** | JSON object specifying the 2 classes subject to classification, of type: if based on content-selection {\&quot;content\&quot;: \&quot;word1 word2 ... wordN\&quot;} ; if based on other field {\&quot;metadata_field\&quot;: [\&quot;values_class1\&quot;, \&quot;values_class2\&quot;} | 
**custom_stop_words** | **list[str]** |  | [optional] 
**time_period** | **str** | Alternative 1: Time period selection from now | [optional] 
**period_start** | **str** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **str** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**excluded_docs** | **list[str]** |  | [optional] 
**syntax_variables** | **bool** | If True, the classifier will include syntax-related variables on top of content variables | [optional] [default to False]
**validation_phase** | **bool** | If True, the classifier assumes that the dataset provided is labeled with the 2 classes and will use that to compute accuracy/precision/recall | [optional] [default to False]
**threshold** | **float** | Threshold value for a document exposure to the contrastic topic, above which the document is assigned to class 1 specified through metadata_selection | [optional] 
**remove_redundancies** | **bool** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


