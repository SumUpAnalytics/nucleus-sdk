# NucleusApi.HistoAnalysis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name. | 
**query** | **String** | Fulltext query, using mysql MATCH boolean query format. Example, (\&quot;word1\&quot; OR \&quot;word2\&quot;) AND (\&quot;word3\&quot; OR \&quot;word4\&quot;) | [optional] 
**customStopWords** | **[String]** |  | [optional] 
**numTopics** | **Number** | Number of topics to be extracted from the dataset and summarized. | [optional] 
**numKeywords** | **Number** | Number of keywords per topic that is extracted from the dataset. | [optional] 
**metadataSelection** | **Object** | JSON object specifying metadata-based queries on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**timePeriod** | **String** | Alternative 1: Time period selection | [optional] 
**periodStart** | **String** | Alternative 2: Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**periodEnd** | **String** | Alternative 2: End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD HH:MM:SS\&quot;  | [optional] 
**updatePeriod** | **String** | Frequency at which the historical anlaysis is performed | [optional] [default to &#39;d&#39;]
**incStep** | **Number** | Number of increments of the udpate period in between two historical computations. | [optional] 
**excludedDocs** | **[String]** |  | [optional] 
**customDictFile** | **Object** | Custom sentiment dictionary JSON file. | [optional] 


