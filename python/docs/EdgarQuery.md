# EdgarQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_dataset** | **str** | Name of the new dataset where the scraped documents will be inserted. | 
**tickers** | **list[str]** | List of tickers to be scraped (eg. [\&quot;GOOG\&quot;]) | 
**filing_types** | **list[str]** | List of form types to be scraped (eg. [\&quot;10K\&quot;]) | 
**sections** | **list[str]** | List of document sections to be scraped. If empty all sections will be scraped | [optional] 
**period_start** | **date** | Start date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 
**period_end** | **date** | End date for the period to analyze within the dataset. Format: \&quot;YYYY-MM-DD\&quot;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


