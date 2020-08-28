# NucleusApi.DocumentContrastSummaryModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**metadata_selection** | **Object** | JSON specifying metadata-based queries on the dataset. If titles or doc_ids are also provided, then this selection is ignored. Format: {\&quot;key\&quot;: \&quot;values\&quot;}. Metadata values are case-sensitive. | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**time_period** | **String** | Alternative 1: Time period selection from now | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**metadata_selection_contrast** | **Object** | JSON object specifying the 2 classes subject to contrasted summarization, of type: if based on content-selection {\&quot;content\&quot;: \&quot;word1 word2 ... wordN\&quot;} ; if based on other field {\&quot;metadata_field\&quot;: [\&quot;values_class1\&quot;, \&quot;values_class2\&quot;} | 
**summary_length** | **Number** | The maximum number of bullet points a user wants to see in each topic summary. | [optional] 
**context_amount** | **Number** | The number of sentences surrounding key summary sentences in the documents that they come from. | [optional] 
**short_sentence_length** | **Number** | The sentence length (in number of words) below which a sentence is excluded from summarization. | [optional] 
**long_sentence_length** | **Number** | The sentence length (in number of words) beyond which a sentence is excluded from summarization. | [optional] 
**background_summary** | **Boolean** | If True, the contrasted summary will include a contrasted summary for each of the foreground and the background | [optional] [default to false]
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**syntax_variables** | **Boolean** | If True, the contrasted summary will leverage syntax-related variables on top of content variables to better separate the document from the rest | [optional] [default to false]
**num_keywords** | **Number** | Number of keywords of the contrasted topic that is extracted from the dataset. | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis and retains only one copy of it. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to false]


<a name="TimePeriodEnum"></a>
## Enum: TimePeriodEnum


* `1M` (value: `"1M"`)

* `3M` (value: `"3M"`)

* `6M` (value: `"6M"`)

* `12M` (value: `"12M"`)

* `3Y` (value: `"3Y"`)

* `5Y` (value: `"5Y"`)




