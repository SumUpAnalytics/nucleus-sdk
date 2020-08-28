# NucleusApi.TopicHistoryModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **Object** | JSON specifying metadata-based queries on the dataset. If titles or doc_ids are also provided, then this selection is ignored. Format: {\&quot;key\&quot;: \&quot;values\&quot;}. Metadata values are case-sensitive. | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 
**period_start** | **String** | Time range selection method 2: Start date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**period_end** | **String** | Time range selection method 2: End date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**n_steps** | **Number** | Number of steps in the historical analysis over the requested period. Each step is such that they contain an equal number of documents. | [optional] 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**custom_dict_file** | **Object** | JSON with custom sentiment dictionary: {\&quot;word1\&quot;: value1,  \&quot;word2\&quot;: value2, ..., \&quot;wordN\&quot;: valueN} | [optional] 
**recompute_topics** | **Boolean** | If True, this option will trigger a recomputation of the topics at each past point in time. Especially helpful if conducting historical analysis of a query. | [optional] [default to false]
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to true]


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




