# NucleusApi.DatasetTagging

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name. | 
**query** | **String** | Dataset-language-specific fulltext query specifying an entity to tag in the dataset, with possibly several alternative namings, using mysql MATCH boolean query format. Example: \&quot;word1 OR word2 OR word3 OR word4\&quot;  | 
**metadata_selection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Alternative 1: Time period selection from now | [optional] 
**period_start** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 


