# NucleusApi.TopicContrastModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**metadata_selection** | **Object** | JSON specifying metadata-based queries on the dataset. If titles or doc_ids are also provided, then this selection is ignored. Format: {\&quot;key\&quot;: \&quot;values\&quot;}. Metadata values are case-sensitive. | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 
**period_start** | **String** | Time range selection method 2: Start date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**period_end** | **String** | Time range selection method 2: End date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**metadata_selection_contrast** | **Object** | JSON object specifying the 2 classes subject to classification, of type: if based on content-selection {\&quot;content\&quot;: \&quot;word1 word2 ... wordN\&quot;}; if based on other field {\&quot;metadata_field\&quot;: [\&quot;values_class1\&quot;, \&quot;values_class2\&quot;} | 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**syntax_variables** | **Boolean** | If True, the classifier will include syntax-related variables                             on top of content variables | [optional] [default to false]
**num_keywords** | **Number** | Number of keywords for the contrasted topic that is extracted from the dataset. | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the                             analysis and retains only one copy of it. A quasi-duplicate                             would have the same NLP representation, but not necessarily the                             exact same text. | [optional] [default to false]


<a name="TimePeriodEnum"></a>
## Enum: TimePeriodEnum


* `1D` (value: `"1D"`)

* `2D` (value: `"2D"`)

* `1W` (value: `"1W"`)

* `2W` (value: `"2W"`)

* `1M` (value: `"1M"`)

* `3M` (value: `"3M"`)

* `6M` (value: `"6M"`)

* `12M` (value: `"12M"`)

* `3Y` (value: `"3Y"`)

* `5Y` (value: `"5Y"`)




