# NucleusApi.SetupConnectorModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Destination dataset name. Data from the connector will be inserted into this dataset. | 
**settings** | **Object** | Json settings, specific for each connector. Check connector documentation | 
**period_seconds** | **Number** | Update frequency, in seconds. Default 1 hour. | [optional] 
**connector** | **String** | Name of the connector. | [optional] [default to &#39;servicenow&#39;]


