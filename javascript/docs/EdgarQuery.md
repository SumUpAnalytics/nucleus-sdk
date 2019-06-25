# NucleusApi.EdgarQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_dataset** | **String** | Name of the new dataset where the scraped documents will be inserted. | 
**tickers** | **[String]** | List of tickers to be scraped (eg. [\&quot;GOOG\&quot;]) | 
**filing_types** | **[String]** | List of form types to be scraped (eg. [\&quot;10K\&quot;]) | 
**sections** | **[String]** | List of document sections to be scraped. If empty all sections will be scraped | [optional] 
**period_start** | **Date** | Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **Date** | End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 


