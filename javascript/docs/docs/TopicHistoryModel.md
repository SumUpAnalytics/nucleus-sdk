# NucleusApi.TopicHistoryModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name. | 
**query** | **String** | Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
**custom_stop_words** | **[String]** |  | [optional] 
**num_topics** | **Number** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**num_keywords** | **Number** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Alternative 1: Time period selection | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**update_period** | **String** | Frequency at which the historical anlaysis is performed | [optional] [default to &#39;d&#39;]
**inc_step** | **Number** | Number of increments of the udpate period in between two historical computations. | [optional] 
**excluded_docs** | **[String]** |  | [optional] 
**custom_dict_file** | **Object** | Custom sentiment dictionary JSON file. | [optional] 


