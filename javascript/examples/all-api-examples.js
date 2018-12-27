
var NucleusApi = require('nucleus_api');

var host = "http://localhost:5000";
var apiKey = "p2Hbhk1J2cTnO6VFrNUP1Q";


// Create API instance
var apiClient = new NucleusApi.ApiClient(host, apiKey);
var apiInstance = new NucleusApi.NucleusApi(apiClient);

console.log("--------- Append file from local drive to dataset -----------");

var file = "./quarles20181109a.pdf"; // File | 
var dataset = "dataset_test"; // String | Destination dataset where the file will be inserted.
var opts = { 
    'metadata': "metadata_example" // String | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"}
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postUploadFile(file, dataset, opts, callback);


console.log("------------ Append file from URL to dataset ---------------");

var file_url = "https://www.federalreserve.gov/newsevents/speech/files/quarles20181109a.pdf"
var dataset = "dataset_test"
var payload = new NucleusApi.UploadURLModel(dataset=dataset,
                 file_url=file_url); // UploadURLModel | 

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postUploadUrl(payload, callback);



console.log("----------- Append json from CSV to dataset -----------------");

var csvFile = "trump-tweets-100.csv"
var dataset = "dataset_test"
var row = {
    'time' : '12/23/2018',
    'title' : 'test title',
    'content' : 'test content',
    'author' : 'test author'
}
var payload = new NucleusApi.Appendjsonparams(
    dataset=dataset,
    language='english',
    document={'time'   : row['time'],
              'title'  : row['title'],
              'content': row['content'],
              'author' : row['author']}); // Appendjsonparams | 


var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postAppendJsonToDataset(payload, callback);




var doc_cnt = 0
// with open(csv_file, encoding='utf-8-sig') as csvfile:
//     reader = csv.DictReader(csvfile)
//     for row in reader:
//         if doc_cnt < 1:
//             payload = nucleus_api.Appendjsonparams(dataset=dataset,
//                                                   language='english',
//                                                   document={'time'   : row['time'],
//                                                             'title'  : row['title'],
//                                                             'content': row['content'],
//                                                             'author' : row['author']}
//                                                  )
//
//             try:
//                 api_response = api_instance.post_append_json_to_dataset(payload)
//                 #print('api_response', api_response)
//             except ApiException as e:
//                 print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
//
//         doc_cnt = doc_cnt + 1
//
// print('Dataset', dataset, 'now has', api_response.result, 'documents.')
// print('-------------------------------------------------------------')

console.log('---------------- List available datasets ---------------------');

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getListDatasets(callback);

console.log('-------------------------------------------------------------')

console.log('--------------- Get dataset information -------------------');

// print('Information about dataset', dataset)
// print('    Language:', api_response.result.detected_language)
// print('    Number of documents:', api_response.result.num_documents)
// print('    Time range:', datetime.datetime.fromtimestamp(float(api_response.result.time_range[0])),
//              'to', datetime.datetime.fromtimestamp(float(api_response.result.time_range[1])))
//
//

var dataset = 'dataset_test'; // String | Dataset name.
var opts = { 
  'query': '', // String | Fulltext query, using mysql MATCH boolean query format.
  'metadataSelection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': '' // String | Time period selection
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDatasetInfo(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('--------------------- Delete document -----------------------');
var dataset = 'dataset_test'
var docid = '1'
var payload = new NucleusApi.Deletedocumentmodel(
    dataset=dataset,
    docid=docid); // Deletedocumentmodel | 


var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postDeleteDocument(payload, callback);

console.log('-------------------------------------------------------------');

console.log('--------------------- Delete dataset ------------------------');
var dataset = 'dataset_test'
var payload = new NucleusApi.Deletedatasetmodel(
    dataset=dataset); // Deletedatasetmodel | 

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postDeleteDataset(payload, callback);


console.log('-------------------------------------------------------------');

console.log('--------- Create a full dataset for testing other APIs ---------');
// # add documents to dataset
// csv_file = 'trump-tweets-100.csv'
// dataset = 'trump_tweets'
//
// with open(csv_file, encoding='utf-8-sig') as csvfile:
//     reader = csv.DictReader(csvfile)
//     for row in reader:
//         payload = nucleus_api.Appendjsonparams(dataset=dataset,
//                                                   language='english',
//                                                   document={'time'   : row['time'],
//                                                             'title'  : row['title'],
//                                                             'content': row['content'],
//                                                             'author' : row['author']}
//                                                  )
//
//         try:
//             api_response = api_instance.post_append_json_to_dataset(payload)
//             #print('api_response=', api_response)
//         except ApiException as e:
//             print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)
//
// print('Dataset', dataset, 'now has', api_response.result, 'documents.')
console.log('-------------------------------------------------------------');

console.log('------------- Get list of topics from dataset --------------');
var dataset = "trump_tweets"; // String | Dataset name.

var opts = { 
    'query': '', // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "\["real", "hillary"\]", // String | List of stop words.
    'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
    'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadataSelection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'timePeriod': '' // String | Time period selection
    //'excludedDocs': '' // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getTopicApi(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('------------------- Get topic summary -----------------------');
var dataset = "trump_tweets"; // String | Dataset name.

var opts = { 
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "customStopWords_example", // String | List of stop words
    'numTopics': 8, // Number | Number of topics to be extracted from the dataset and summarized.
    'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'timePeriod': "", // String | Time period selection
    'summaryLength': 6, // Number | The maximum number of bullet points a user wants to see in each topic summary.
    'contextAmount': 0, // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
    'numDocs': 20 // Number | The maximum number of key documents to use for summarization.
    //'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.getTopicSummaryApi(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('---------------- Get topic sentiment ------------------------');
var dataset = "trump_tweets"; // String | Dataset name.
var opts = { 
  'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
  //'customStopWords': "customStopWords_example", // String | List of stop words
  'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
  'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
  'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
  'timePeriod': "", // String | Time period selection
  //'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
  //'customDictFile': "/path/to/file.txt" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postTopicSentimentApi(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('---------------- Get topic consensus ------------------------')
var dataset = "trump_tweets"; // String | Dataset name.

var opts = { 
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "", // String | List of stop words
    'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
    'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'timePeriod': "", // String | Time period selection
    //'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
    'customDictFile': "" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postTopicConsensusApi(dataset, opts, callback);

console.log('-------------------------------------------------------------')

console.log('------------ Get topic historical analysis ----------------');

var dataset = "trump_tweets"; // String | Dataset name.
var timePeriod = "6M"; // String | Time period selection
var updatePeriod = "d"; // String | Frequency at which the historical anlaysis is performed

var opts = { 
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "", // String | List of stop words
    'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
    'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'incStep': 1, // Number | Number of increments of the udpate period in between two historical computations.
    //'excludedDocs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
    'customDictFile': "" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.postTopicHistoricalAnalysisApi(dataset, timePeriod, updatePeriod, opts, callback);

console.log('-------------------------------------------------------------');

console.log('----------------- Get author connectivity -------------------');


var dataset = "trump_tweets"; // String | Dataset name.
var targetAuthor = "D_Trump16"; // String | Name of the author to be analyzed.
var timePeriod = "12M"; // String | Time period selection
var opts = { 
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': [""], // String | List of words possibly used by the target author that are considered not information-bearing.
    'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    //'excludedDocs': [""] // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getAuthorConnectivityApi(dataset, targetAuthor, timePeriod, opts, callback);

console.log('-------------------------------------------------------------');

console.log('------------------- Get topic deltas -----------------------');

var dataset = "trump_tweets"; // String | Dataset with a time series component. These docs should reference a universe of entities that overlaps through time.
var timeStartT0 = "2018-08-12 00:00:00"; // String | Start date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
var timeEndT0 = "2018-08-15 13:00:00"; // String | End date for the start-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
var timeStartT1 = "2018-08-16 00:00:00"; // String | Start date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 
var timeEndT1 = "2018-08-19 00:00:00"; // String | End date for the end-of-period dataset. Format: \"YYYY-MM-DD HH:MM:SS\" 

var opts = { 
   'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
   //'customStopWords': "customStopWords_example", // String | List of stop words.
   'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
   'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
   'metadataSelection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
   //'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getTopicDeltaApi(dataset, timeStartT0, timeEndT0, timeStartT1, timeEndT1, opts, callback);

console.log('-------------------------------------------------------------');
//

console.log('----------------- Display document information --------------------');
var dataset = "trump_tweets"; // String | Dataset name.
var opts = { 
    'docTitles': [ "\"D_Trump2018_8_18_1_47\"" ], // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
    //'docIds': [ "\"11, 20, 21\"" ] // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getDocInfo(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('----------------- Display document details --------------------');

var dataset = "trump_tweets"; // String | Dataset name.

var opts = { 
    'docTitles': [ "\"D_Trump2018_8_18_1_47\"" ], // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
    //'docIds': "docIds_example" // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getDocDisplay(dataset, opts, callback);

console.log('-------------------------------------------------------------')

console.log('------------- Get document recommendations -----------------')
var dataset = "trump_tweets"; // String | Dataset name.
var opts = { 
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "customStopWords_example", // String | List of stop words.
    'numTopics': 8, // Number | Number of topics to be extracted from the dataset.
    'numKeywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'numDocs': 20, // Number | Number of desired recommended docs per topic.
    //'metadataSelection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    //'timePeriod': "timePeriod_example", // String | Time period selection
    //'excludedDocs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getDocRecommendApi(dataset, opts, callback);

console.log('-------------------------------------------------------------')

console.log('------------------ Get document summary  --------------------')

var dataset = "trump_tweets"; // String | Dataset name.
var docTitle = "D_Trump2018_8_15_15_4"; // String | The title of the document to be summarized.

var opts = { 
    //'customStopWords': "customStopWords_example", // String | List of stop words
    'summaryLength': 6, // Number | The maximum number of bullet points a user wants to see in the document summary.
    'contextAmount': 0 // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ' + data);
    }
};
apiInstance.getDocSummaryApi(dataset, docTitle, opts, callback);

console.log('-------------------------------------------------------------')

