# NucleusApi.DeleteDocumentRespModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **String** | If the job is taking too long, job_id is returned, GET /jobs can then be used to poll for results. | [optional] 
**result** | **Object** | JSON with status: [{\&quot;doc_id\&quot;: doc_id1, \&quot;status\&quot;: \&quot;deleted\&quot;}, {\&quot;doc_id\&quot;: doc_id2, \&quot;status\&quot;: \&quot;deleted\&quot;}] | [optional] 


