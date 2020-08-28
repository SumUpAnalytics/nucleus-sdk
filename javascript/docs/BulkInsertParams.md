# NucleusApi.BulkInsertParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**language** | **String** | Specify a language to override language detection. | [optional] 
**documents** | [**[Document]**](Document.md) |  | [optional] 
**dateformat** | **String** | Specify the date format in the document to help date parsing. For example, if the date is \&quot;Tue Jun 12 00:30:00 +0000 2018\&quot;, set dateformat to \&quot;%a %b %d %H:%M:%S %z %Y\&quot;. If dateformat is not set, Nucleus guesses the date format with different methods. | [optional] 


