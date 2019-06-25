# NucleusApi.DatasetInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name. | 
**query** | **String** | Dataset-language-specific fulltext query, using mysql MATCH boolean query format. Example: \&quot;(word1 OR word2) AND (word3 OR word4)\&quot;  | [optional] 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Alternative 1: Time period selection | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**owner_email** | **String** | Has to be specified to access a shared dataset that is owned by another user | [optional] 


