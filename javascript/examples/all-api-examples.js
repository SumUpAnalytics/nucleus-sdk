
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
var opts = {
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
apiInstance.postUploadFile(fileStream, dataset, opts, callback);
console.log('-------------------------------------------------------------');


console.log("------------ Append file from URL to dataset ---------------");

var file_url = "https://www.federalreserve.gov/newsevents/speech/files/quarles20181109a.pdf"
var dataset = "dataset_test"
var payload = new NucleusApi.UploadURLModel(dataset=dataset,
                 file_url=file_url); // UploadURLModel |

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
        console.log('Information about dataset ' + dataset);
        console.log('    Language: ' + data.result.detected_language)
        console.log('    Number of documents: ' + data.result.num_documents);
        console.log('    Time range: ' + data.result.time_range[0] +
              ' to ' + data.result.time_range[1]);
        console.log('-------------------------------------------------------------');
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
        console.log(data.result);
        console.log('-------------------------------------------------------------');
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
        console.log(dataset + ' ' + data.result);
    }
};
apiInstance.postDeleteDataset(payload, callback);


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
apiInstance.getTopicDeltaApi(dataset, timeStartT0, timeEndT0, timeStartT1, timeEndT1, opts, callback);

console.log('-------------------------------------------------------------');
//

console.log('----------------- Display document information --------------------');
var dataset = "trump_tweets"; // String | Dataset name.
var opts = {
    'docTitles': "[ \"D_Trump2018_8_18_1_47\" ]", // String | The title of the documents on which info is requested. Example: [ \"title 1\", \"title 2\" ]
    'docIds': "[ \"11\", \"12\", \"13\" ]" // String | The docid of the documents on which info is requested. Example:[ \"docid1, docid2\" ]
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
apiInstance.getDocInfo(dataset, opts, callback);

console.log('-------------------------------------------------------------');

console.log('----------------- Display document details --------------------');

var dataset = "trump_tweets"; // String | Dataset name.

var opts = {
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
        console.log('Document Summary');
        console.log('    ID:', data.result.summary.sourceid);
        console.log('    Title:', data.result.doc_title);
        console.log('    Summary:', data.result.summary.sentences);
    }
};
apiInstance.getDocSummaryApi(dataset, docTitle, opts, callback);

console.log('-------------------------------------------------------------')
