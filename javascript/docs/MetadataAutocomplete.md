# NucleusApi.MetadataAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Dataset name | 
**metadata_column** | **Object** | The name of metadata column for which autocomplete is requested | 
**metadata_selection** | **Object** | JSON object specifying pre-existing filters on the dataset, of type {\&quot;metadata_field\&quot;: \&quot;selected_values\&quot;} | [optional] 
**time_period** | **String** | Time range selection method 1: time period from now | [optional] 
**query** | **String** | The query to autocomplete (can also be left empty)\&quot;  | [optional] 
**fulltext_query** | **String** | Autocomplete only on documents which match this fulltext query | [optional] 


<a name="TimePeriodEnum"></a>
## Enum: TimePeriodEnum


* `1D` (value: `"1D"`)

* `2D` (value: `"2D"`)

* `1W` (value: `"1W"`)

* `2W` (value: `"2W"`)

* `1M` (value: `"1M"`)

* `3M` (value: `"3M"`)

* `6M` (value: `"6M"`)

* `12M` (value: `"12M"`)

* `3Y` (value: `"3Y"`)

* `5Y` (value: `"5Y"`)




