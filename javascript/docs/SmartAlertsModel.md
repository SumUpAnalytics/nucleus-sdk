# NucleusApi.SmartAlertsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**tracked_queries** | **[String]** | List of user-defined queries to track | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset per query to aggregate back into a tracker. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset per query. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 
**period_start** | **String** | Time range selection method 2: Start date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**period_end** | **String** | Time range selection method 2: End date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**num_days_back** | **Number** | Number of days from the latest date of the dataset, which are considered as foreground for the novelty analysis. | [optional] 
**novelty_threshold** | **Number** | Value of novelty of a document above which a document is considered novel. This value should be between 0 and 1 and reflects the percentage of the document information unexplained by the background. | [optional] 
**num_new_words** | **Number** | Maximum number of new words returned from the new words detection | [optional] 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to false]


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




