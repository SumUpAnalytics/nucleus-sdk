# NucleusApi.EdgarAvailableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickers** | **Object** | Mapping of tickers and company names (eg: {\&quot;GOOG\&quot;:\&quot;Google\&quot;}) | [optional] 
**filing_types** | **[String]** | List of form types to be scraped (eg. [\&quot;10K\&quot;]) | [optional] 
**sections** | **[String]** | List of document sections to be scraped. If empty all sections will be scraped | [optional] 
**count** | **Number** | Number of available filings matching the input filter (if sections is specified, count is the number of matching sections) | [optional] 
**date_range** | **[Date]** | Available date range matching the input filter | [optional] 


