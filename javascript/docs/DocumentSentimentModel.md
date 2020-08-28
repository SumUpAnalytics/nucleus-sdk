# NucleusApi.DocumentSentimentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**doc_title** | **String** | The title of the document to be analyzed. | [optional] 
**query** | **String** | Dataset-language-specific fulltext query, using SQL MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot; | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the document to estimate the document&#39; sentiment. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the document. | [optional] 
**custom_stop_words** | **[String]** | List of dataset-language-specific stopwords that should be excluded from the analysis. Example: [\&quot;word1\&quot;, \&quot;word2\&quot;, ..., \&quot;wordN\&quot;] | [optional] 
**custom_dict_file** | **Object** | JSON with custom sentiment dictionary: {\&quot;word1\&quot;: value1,  \&quot;word2\&quot;: value2, ..., \&quot;wordN\&quot;: valueN} | [optional] 
**cache_sentiment** | **Boolean** | If true, computes the sentiment for all docs in the dataset and saves it in a new \&quot;sentiment_category\&quot; metadata column. | [optional] [default to false]
**overwrite** | **Boolean** | If true, overwrites cached sentiment values for all documents in the dataset | [optional] [default to false]


