# NucleusApi.FilterModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**metadata_selection** | **Object** | JSON specifying metadata-based queries on the dataset. If titles or doc_ids are also provided, then this selection is ignored. Format: {\&quot;key\&quot;: \&quot;values\&quot;}. Metadata values are case-sensitive. | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 


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




