# **summarize_file_url**
> DocumentSummaryRespModel summarize_file_url(api_instance, file_params)


Summarize the file using the URL and other optional parameters provided in file_params

### Example
```python
from __future__ import print_function
import time
import nucleus_api
from nucleus_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = nucleus_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = nucleus_api.NucleusApi(nucleus_api.ApiClient(configuration))

file_params = {
    'file_url': 'https://s3-us-west-2.amazonaws.com/sumup-public/nucleus-sdk/quarles20181109a.docx',
    'filename': 'quarles20181109a-newname.pdf',
    'custom_stop_words': ["document", "sometimes"],
    'summary_length': 6,
    'context_amount': 0,
    'short_sentence_length': 4,
    'long_sentence_length': 40}


result = summarize_file_url(api_instance, file_params)
print(result)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_instance** | **NucleusApi**| An instance of the NucleusAPI class. |
 **file_params** | **JSON string**| JSON string with the following fields. |
 **file_url** | **string**| the URL at which the file is stored (could be a S3 bucket address for instance)
 **filename** | **string**| filename saved on the server
 **custom_stop_words** | **string**| List of words possibly used by the target author that are considered not information-bearing. | [optional]
 **summary_length** | **integer**| the maximum number of bullet points a user wants to see in the document summary. DEFAULT: 6 | [optional]
 **context_amount** | **integer**| the number of sentences surrounding key summary sentences in the original document that a user wants to see in the document summary. DEFAULT: 0 | [optional]
 **short_sentence_length** | **integer**| The sentence length below which a sentence is excluded from summarization. DEFAULT: 4 words  | [optional]
 **long_sentence_length** | **integer**| The sentence length beyond which a sentence is excluded from summarization. DEFAULT: 40 words  | [optional]

### Return type

[**DocumentSummaryModel**](docs/DocumentSummaryModel.md)

