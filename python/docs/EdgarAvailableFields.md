# EdgarAvailableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickers** | **object** | Mapping of tickers and company names (eg: {\&quot;GOOG\&quot;:\&quot;Google\&quot;}) | [optional] 
**filing_types** | **list[str]** | List of form types to be scraped (eg. [\&quot;10K\&quot;]) | [optional] 
**sections** | **list[str]** | List of document sections to be scraped. If empty all sections will be scraped | [optional] 
**count** | **int** | Number of available filings matching the input filter (if sections is specified, count is the number of matching sections) | [optional] 
**date_range** | **list[date]** | Available date range matching the input filter | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


