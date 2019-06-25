# NucleusApi.FilterModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **String** | Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
**custom_stop_words** | **[String]** |  | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Alternative 1: Time period selection | [optional] 


