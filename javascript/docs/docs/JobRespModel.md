# NucleusApi.JobRespModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobId** | **String** | If the job is taking too long, job_id is returned, GET /jobs can then be used to poll for results | [optional] 
**progress** | **String** | JSON encoded progress of the job. | [optional] 
**result** | **String** | JSON encoded result of the job. | [optional] 
**error** | **String** | error messages | [optional] 
**lastUpdate** | **Number** | Last time the job progress was updated (UNIX seconds from 1970) | [optional] 


