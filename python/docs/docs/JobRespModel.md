# JobRespModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | If the job is taking too long, job_id is returned, GET /jobs can then be used to poll for results | [optional] 
**progress** | **str** | JSON encoded progress of the job. | [optional] 
**result** | **str** | JSON encoded result of the job. | [optional] 
**error** | **str** | error messages | [optional] 
**last_update** | **int** | Last time the job progress was updated (UNIX seconds from 1970) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


