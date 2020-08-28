# NucleusApi.KeyAuthorsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**tracked_queries** | **[String]** | List of user-defined queries to track | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset per query to aggregate back into the key authors analysis. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset per query. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 
**period_start** | **String** | Time range selection method 2: Start date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**period_end** | **String** | Time range selection method 2: End date for the period to analyze. Format: \&quot;YYYY-MM-DD\&quot; | [optional] 
**num_authors** | **Number** | Max number of key contributors that the user wants to see returned by the analysis. | [optional] 
**num_keydocs** | **Number** | Max number of key contributions from key contributors that the user wants to see returned by the analysis. | [optional] 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**custom_dict_file** | **Object** | JSON with custom sentiment dictionary: {\&quot;word1\&quot;: value1,  \&quot;word2\&quot;: value2, ..., \&quot;wordN\&quot;: valueN} | [optional] 


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




