# NucleusApi.DocumentNoveltyModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_days_back** | **Number** | Number of days from the latest date of the dataset, which are considered as foreground for the novelty analysis. | [optional] 
**novelty_threshold** | **Number** | Value of novelty of a document above which a document is considered novel. This value should be between 0 and 1 and reflects the percentage of the document information unexplained by the background. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Alternative 1: Time period selection for the period considered as background for the novelty analysis | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period considered as background for the novelty analysis. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period considered as background for the novelty analysis. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**short_sentence_length** | **Number** | The sentence length (in number of words) below which a sentence is excluded from novelty analysis. | [optional] 
**long_sentence_length** | **Number** | The sentence length (in number of words) beyond which a sentence is excluded from novelty analysis. | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to false]


<a name="TimePeriodEnum"></a>
## Enum: TimePeriodEnum


* `2D` (value: `"2D"`)

* `1W` (value: `"1W"`)

* `2W` (value: `"2W"`)

* `1M` (value: `"1M"`)

* `3M` (value: `"3M"`)

* `6M` (value: `"6M"`)

* `12M` (value: `"12M"`)

* `3Y` (value: `"3Y"`)

* `5Y` (value: `"5Y"`)




