# NucleusApi.TopicDeltaModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**period_0_start** | **String** | Start date for the initial-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_0_end** | **String** | End date for the initial-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_1_start** | **String** | Start date for the final-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**period_1_end** | **String** | End date for the final-period dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to true]


