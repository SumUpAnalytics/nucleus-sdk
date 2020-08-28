# NucleusApi.DocDisplay

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**doc_titles** | **[String]** | The titles of the documents on which info is requested. Example: [\&quot;title 1\&quot;, \&quot;title 2\&quot;] | [optional] 
**doc_ids** | **[String]** | List of document IDs (e.g [\&quot;doc_id1\&quot;, \&quot;doc_id2\&quot;]) | [optional] 
**metadata_selection** | **Object** | JSON specifying metadata-based queries on the dataset. If titles or doc_ids are also provided, then this selection is ignored. Format: {\&quot;key\&quot;: \&quot;values\&quot;}. Metadata values are case-sensitive. | [optional] 
**block** | **Number** | Documents are returned in blocks of 100 documents each. By default only the first block is returned. Use block to select specific block of documents | [optional] 


