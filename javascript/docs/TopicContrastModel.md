# NucleusApi.TopicContrastModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name. | 
**query** | **String** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**metadata_selection** | **Object** | JSON object specifying the 2 classes subject to classification, of type: if based on content-selection {\&quot;content\&quot;: \&quot;word1 word2 ... wordN\&quot;} ; if based on other field {\&quot;metadata_field\&quot;: [\&quot;values_class1\&quot;, \&quot;values_class2\&quot;} | 
**custom_stop_words** | **[String]** |  | [optional] 
**time_period** | **String** | Alternative 1: Time period selection from now | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**excluded_docs** | **[String]** |  | [optional] 
**syntax_variables** | **Boolean** | If True, the classifier will include syntax-related variables on top of content variables | [optional] [default to false]
**compression** | **Number** | Parameter controlling the breadth of the contrasting topic. Contained between 0 and 1, the smaller it is, the more contrasting terms will be captured, with decreasing weight. | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis and retains only one copy of it. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to false]


