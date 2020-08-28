# NucleusApi.TopicTransferModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset0** | **String** | Name of reference dataset, on which topics are extracted. | 
**dataset1** | **String** | Alternative 1: Name of validation dataset, on which topics are applied. Only pass in this argument if the validation dataset has been separately created. | [optional] 
**fixed_topics** | **Object** | JSON object specifying the topics that are exogenously fixed, of type {\&quot;keywords\&quot;: [\&quot;keyword_1\&quot;, \&quot;keyword_2\&quot;, \&quot;keyword_3\&quot;], \&quot;weights\&quot;: [weight_1, weight_2, weight_3]} | [optional] 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**period_0_start** | **String** | Alternative 2: Start date for the reference dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_0_end** | **String** | Alternative 2: End date for the reference dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_1_start** | **String** | Alternative 2: Start date for the validation dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_1_end** | **String** | Alternative 2: End date for the validation dataset. Use this approach if reference and validation datasets are different time slices of a superset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**excluded_docs** | **[String]** | List of document IDs that should be excluded from the analysis. Example: [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;, ..., \&quot;doc_idN\&quot;] | [optional] 
**remove_redundancies** | **Boolean** | If True, this option removes quasi-duplicates from the analysis. A quasi-duplicate would have the same NLP representation, but not necessarily the exact same text. | [optional] [default to true]


