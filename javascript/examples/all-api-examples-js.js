
var NucleusApi = require('nucleus_api');
var fs = require('fs'); 
var csvParser = require('csv-parse');

var host = 'UPDATE-WITH-API-HOST';
var apiKey = 'UPDATE-WITH-API-KEY';

// Create API instance
var apiClient = new NucleusApi.ApiClient(host, apiKey);
var apiInstance = new NucleusApi.NucleusApi(apiClient);

console.log("--------- Append file from local drive to dataset -----------");
var file = "quarles20181109a.pdf"; // File | 
var dataset = "dataset_test"; // String | Destination dataset where the file will be inserted.
var payload = { 
    //'metadata': "" // String | Optional json containing additional document metadata. Eg: {\"time\":\"01/01/2001\",\"author\":\"me\"}
};

var fileStream = fs.createReadStream(file)

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log(data.result + ' added to dataset ' + dataset);
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postUploadFile(fileStream, dataset, payload, callback);
console.log('-------------------------------------------------------------');


console.log("------------ Append file from URL to dataset ---------------");

var file_url = "https://www.federalreserve.gov/newsevents/speech/files/quarles20181109a.pdf"
var dataset = "dataset_test"
var payload = {
    'dataset': dataset,
    'file_url': file_url
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log(data.result + ' added to dataset ' + dataset);
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postUploadUrl(payload, callback);

console.log('-------------------------------------------------------------');

// This dataset will be used to test all topics and documents APIs
console.log("----------- Append json from CSV to dataset -----------------");

var csvFile = "trump-tweets-100.csv"
var dataset = "trump_tweets"

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        //console.log('API called successfully. Returned data: ' + data.result);
    }
};

var processCsvData = function(data, rows, dataset) {
    console.log('Processing CSV data...');
    // The first row is header. Skip it.
    for (var i = 1; i < rows; i++) {
        var curRow = data[i];
        var payload = {
            'dataset': dataset,
            //'language': 'english', // optional.
            'document': {'time'   : curRow[2],
                         'title'  : curRow[4],
                         'content': curRow[1],
                         'source' : curRow[0],
                         'author' : curRow[3]}};
        
        apiInstance.postAppendJsonToDataset(payload, callback);
    }
    console.log(rows-1 + ' documents added to dataset ' + dataset);
    console.log('-------------------------------------------------------------')
}

var csvData=[];
fs.createReadStream(csvFile)
    .pipe(csvParser())
    .on('data', function(csvrow) {
        csvData.push(csvrow);        
    })
    .on('end',function() {
        processCsvData(csvData, csvData.length, dataset);
    });

console.log('-------------------------------------------------------------')

console.log('---------------- List available datasets ---------------------');

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        var listDatasets = data.result;
        var datasetCount = listDatasets.length;
        console.log(datasetCount + ' datasets in the database:')
        for (var i = 0; i < datasetCount; i++) {
            console.log('    ' + listDatasets[i]);
        }
        console.log('-------------------------------------------------------------')
    }
};
apiInstance.getListDatasets(callback);

console.log('-------------------------------------------------------------');

console.log('--------------- Get dataset information -------------------');
var payload = { 
    'dataset': 'dataset_test', // String | Dataset name
    'query': '', // String | Fulltext query, using mysql MATCH boolean query format.
    'metadata_selection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'time_period': '' // String | Time period selection
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('Information about dataset ' + dataset);
        console.log('    Language: ' + data.result.detected_language)
        console.log('    Number of documents: ' + data.result.num_documents);
        console.log('    Time range: ' + data.result.time_range[0] +
              ' to ' + data.result.time_range[1]);
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postDatasetInfo(payload, callback);

console.log('-------------------------------------------------------------');

console.log('--------------------- Delete document -----------------------');
var dataset = 'dataset_test';
var docid = '1';
var payload = {
    'dataset': dataset,
    'docid': docid
}; // Deletedocumentmodel | 


var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log(data.result);
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postDeleteDocument(payload, callback);

console.log('-------------------------------------------------------------');

console.log('--------------------- Delete dataset ------------------------');
var dataset = 'dataset_test';
var payload = {'dataset': dataset}; // Deletedatasetmodel | 

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log(dataset + ' ' + data.result);
    }
};
apiInstance.postDeleteDataset(payload, callback);


console.log('-------------------------------------------------------------');

console.log('------------- Get list of topics from dataset --------------');

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name
    'query': '', // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "\["real", "hillary"\]", // String | List of stop words.
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadata_selection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'time_period': '' // String | Time period selection
    //'excludedDocs': '' // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Topic', i, 'keywords:');
            console.log('    Keywords:', res.topic);
            console.log('    Keyword weights:',  res.keywords_weight);
            console.log('    Strength:', res.strength);
            var doc_topic_exposure_sel = [];  // list of non-zero doc_topic_exposure
            var doc_id_sel = [];    // list of doc ids matching doc_topic_exposure_sel
            for (var j = 0; j < res.doc_topic_exposure.length; j++) {
                var doc_topic_exp = parseFloat(res.doc_topic_exposure[j]);
                if (doc_topic_exp != 0) {
                    doc_topic_exposure_sel.push(doc_topic_exp)
                    doc_id_sel.push(res.doc_id[j])
                }
            }
            console.log('    Document IDs:', doc_id_sel)
            console.log('    Document exposures:', doc_topic_exposure_sel)

            console.log('---------------')
        }
    }
};
apiInstance.postTopicApi(payload, callback);

console.log('-------------------------------------------------------------');

console.log('------------------- Get topic summary -----------------------');

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'custom_stop_words': "customStopWords_example", // String | List of stop words
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset and summarized.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadata_selection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'time_period': "", // String | Time period selection
    'summary_length': 6, // Number | The maximum number of bullet points a user wants to see in each topic summary.
    'context_amount': 0, // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
    'num_docs': 20 // Number | The maximum number of key documents to use for summarization.
    //'excluded_docs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Topic', i, 'summary:')
            console.log('    Keywords:', res.topic)
            for (var j = 0; j < res.summary.length; j++) {
                var summary = res.summary[j];
                console.log('    Document ID: ' + summary.sourceid);
                console.log('        Title: ' + summary.title);
                console.log('        Sentences: ' + summary.sentences);
                console.log('        Author: ' + summary.attribute.author);
                console.log('        Source: ' + summary.attribute.source);
                var docTimestamp = parseFloat(summary.attribute.time);
                var docTime = new Date(docTimestamp * 1000);
                console.log('        Time: ' + docTime.getFullYear() + '-' +
                                               docTime.getMonth() + '-' +
                                               docTime.getDate());
                console.log('---------------');
            }
        }
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postTopicSummaryApi(payload, callback);

console.log('-------------------------------------------------------------');

console.log('---------------- Get topic sentiment ------------------------');

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "customStopWords_example", // String | List of stop words
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadata_selection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'time_period': "", // String | Time period selection
    //'excluded_docs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
    //'custom_dict_file': "/path/to/file.txt" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];

            console.log('Topic', i, 'sentiment:');
            console.log('    Keywords:', res.topic);
            console.log('    Sentiment:', res.sentiment);
            console.log('    Strength:', res.strength);
            console.log('    Document IDs:', res.doc_id);
            console.log('    Document Sentiments:', res.doc_sentiment);
            console.log('    Document Scores:', res.doc_score);
    
            console.log('---------------');
        }
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postTopicSentimentApi(payload, callback);

console.log('-------------------------------------------------------------');

console.log('---------------- Get topic consensus ------------------------')

var payload = {
    'dataset': 'trump_tweets', // String | Dataset name
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "", // String | List of stop words
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadata_selection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'time_period': "", // String | Time period selection
    //'excluded_docs': "excludedDocs_example", // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
    'custom_dict_file': "" // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Topic', i, 'consensus:');
            console.log('    Keywords: ' + res.topic);
            console.log('    Consensus: ' + res.consensus);
            console.log('    Strength: ' + res.strength);
        
            console.log('---------------');
        }
    }
};
apiInstance.postTopicConsensusApi(payload, callback);

console.log('-------------------------------------------------------------')

console.log('------------ Get topic historical analysis ----------------');

var timePeriod = "6M"; // String | Time period selection
var updatePeriod = "d"; // String | Frequency at which the historical anlaysis is performed

var payload = {
    'dataset': 'trump_tweets', // String | Dataset name
    'time_period': '6M', // String | Time period selection. Choices: ["1M","3M","6M","12M","3Y","5Y",""]
    'update_period': 'M',  // String | Frequency at which the historical anlaysis is performed
    'query': '', // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'custom_stop_words': '' , // String | List of stop words
    'num_topics': 6, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 7, // Number | Number of keywords per topic that is extracted from the dataset.
    'metadata_selection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
    'inc_step': 1, // Number | Number of increments of the udpate period in between two historical computations.
    //'excluded_docs': 'excludedDocs_example', // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
    'custom_dict_file': '' // File | Custom sentiment dictionary JSON file.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('Printing historical metrics data...')
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Topic', i, res.topic);
            console.log('    Timestamps:', res.time_stamps);
            console.log('    Strength:', res.strength);
            console.log('    Consensus:', res.consensus);
            console.log('    Sentiment:', res.sentiment);
            console.log('----------------');
        }
        console.log('-------------------------------------------------------------');
    }
};
apiInstance.postTopicHistoricalAnalysisApi(payload, callback);

console.log('-------------------------------------------------------------');

console.log('----------------- Get author connectivity -------------------');

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name,
    'target_author': "D_Trump16", // String | Name of the author to be analyzed.
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Subject covered by the author, on which to focus the analysis of connectivity. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'custom_stop_words': [""], // String | List of words possibly used by the target author that are considered not information-bearing.
    'time_period': '12M',  // String | Time period selection Choices: ["1M","3M","6M","12M","3Y","5Y",""]
    'metadata_selection': "", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    //'excluded_docs': [""] // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        var res = data.result;
        console.log('Mainstream connections:')
        for (var i = 0; i < res.mainstream_connection.length; i++) {
            var mc = res.mainstream_connection[i];
            console.log('    Topic:', mc.topic);
            console.log('    Authors:', mc.authors);
        }
        
        console.log('Niche connections:')
        for (var i = 0; i < res.niche_connection.length; i++) {
            var nc = res.niche_connection[i];
            console.log('    Topic:', nc.topic);
            console.log('    Authors:', nc.authors);
        }
        console.log('-------------------------------------------------------------');
  }
};
apiInstance.postAuthorConnectivityApi(payload, callback);

console.log('-------------------------------------------------------------');

console.log('------------------- Get topic deltas -----------------------');

var payload = {
    'dataset': 'trump_tweets',                               
    'query': '', // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'custom_stop_words': "customStopWords_example", // String | List of stop words.
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'period_0_start': '2018-08-12 00:00:00',
    'period_0_end': '2018-08-15 13:00:00',
    'period_1_start': '2018-08-16 00:00:00',
    'period_1_end': '2018-08-19 00:00:00',
    'metadata_selection': '', // String | json object of {\"metadata_field\":[\"selected_values\"]}
    //'excluded_docs': 'excludedDocs_example' // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Topic', i, 'changes in exposure:');
            console.log('    Keywords:', res.topic);
            console.log('    Document ID:', res.doc_id_t0, res.doc_id_t1);
            console.log('    Per Source Change in Exposure:', res.doc_topic_exposure_delta);
            console.log('---------------');
        }
    }
};
apiInstance.postTopicDeltaApi(payload, callback);

console.log('-------------------------------------------------------------');
//

console.log('----------------- Display document information --------------------');

var payload = {
    'dataset': 'trump_tweets', // String | Dataset name,
    'docTitles': "[ \"D_Trump2018_8_18_1_47\" ]", // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
    'docIds': "[ \"11\", \"12\", \"13\" ]", // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
    'metadata_selection': ''
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Document ID:', res.sourceid);
            console.log('    Title:', res.title);
            console.log('    Author:', res.attribute.author);
            console.log('    Source:', res.attribute.source);
            console.log('    Time:', res.attribute.time);

            console.log('---------------')
        }
    }
};
apiInstance.postDocInfo(payload, callback);

console.log('-------------------------------------------------------------');

console.log('----------------- Display document details --------------------');

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name,
    'docTitles': "[ \"D_Trump2018_8_18_1_47\" ]", // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ] 
    'docIds': "[ \"11\", \"12\", \"13\" ]" // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Document ID:' + res.sourceid);
            console.log('    Title:' + res.title);
            console.log('    Author:' + res.attribute.author);
            console.log('    Source:' + res.attribute.source);
            console.log('    Time:', res.attribute.time);
            console.log('    Content', res.content);

            console.log('---------------')
        }
        console.log('-------------------------------------------------------------')
    }
};
apiInstance.postDocDisplay(payload, callback);

console.log('-------------------------------------------------------------')

console.log('------------- Get document recommendations -----------------')

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name,
    'query': "", // String | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\")
    //'customStopWords': "customStopWords_example", // String | List of stop words.
    'num_topics': 8, // Number | Number of topics to be extracted from the dataset.
    'num_keywords': 8, // Number | Number of keywords per topic that is extracted from the dataset.
    'num_docs': 20, // Number | Number of desired recommended docs per topic.
    //'metadata_selection': "metadataSelection_example", // String | json object of {\"metadata_field\":[\"selected_values\"]}
    //'time_period': "timePeriod_example", // String | Time period selection
    //'excluded_docs': "excludedDocs_example" // String | List of document IDs that should be excluded from the analysis. Example, \"docid1, docid2, ..., docidN\" 
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        for (var i = 0; i < data.result.length; i++) {
            var res = data.result[i];
            console.log('Document recommendations for topic', i, ':')
            console.log('    Keywords:', res.topic);

            for (var j = 0; j < res.recommendations.length; j++) {
                var doc = res.recommendations[j];
                console.log('    Recommendation', j, ':')
                console.log('        Document ID:', doc.sourceid)
                console.log('        Title:', doc.title)
                console.log('        Author:', doc.attribute.author)
                console.log('        Source:', doc.attribute.source)
                console.log('        Time:', doc.attribute.time)
            }
    
            console.log('---------------')
        }
    }
};
apiInstance.postDocRecommendApi(payload, callback);

console.log('-------------------------------------------------------------')

console.log('------------------ Get document summary  --------------------')

var dataset = "trump_tweets"; // String | Dataset name.
var doc_title = "D_Trump2018_8_15_15_4"; // String | The title of the document to be summarized.

var payload = { 
    'dataset': 'trump_tweets', // String | Dataset name,
    'doc_title': 'D_Trump2018_8_15_15_4', // String | The title of the document to be summarized.
    //'custom_stop_words': "customStopWords_example", // String | List of stop words
    'summary_length': 6, // Number | The maximum number of bullet points a user wants to see in the document summary.
    'context_amount': 0 // Number | The number of sentences surrounding key summary sentences in the documents that they come from.
};

var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('Document Summary');
        console.log('    ID:', data.result.summary.sourceid);
        console.log('    Title:', data.result.doc_title);
        console.log('    Summary:', data.result.summary.sentences);
    }
};
apiInstance.postDocSummaryApi(payload, callback);

console.log('-------------------------------------------------------------')



