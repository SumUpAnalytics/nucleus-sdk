from __future__ import print_function
import csv, json
import time
import nucleus_client
from nucleus_client.rest import ApiException
from pprint import pprint


# Configure API host and key authorization
configuration = nucleus_client.Configuration()
configuration.host = 'API_HOST_HERE'
configuration.api_key['x-api-key'] = 'API_KEY_HERE'

# Add documents to dataset
csv_file = 'trump_tweets.csv'
dataset = 'trump_tweets_test'   

api_instance = nucleus_client.DatasetsApi(nucleus_client.ApiClient(configuration))

with open(csv_file, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        payload = nucleus_client.Appendjsonparams(dataset=dataset, 
                                                  language='english', 
                                                  document={'time': row['time'],
                                                            'title': row['title'],
                                                            'content': row['content']}
                                                 )

        try:
            response = api_instance.post_append_json_to_dataset(payload)
        except ApiException as e:
            print("Exception when calling DatasetsApi->post_append_json_to_dataset: %s\n" % e)


# list available dataset
api_instance = nucleus_client.DatasetsApi(nucleus_client.ApiClient(configuration))

try:
    api_response = api_instance.get_list_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_list_datasets: %s\n" % e)


# get list of topics from dataset
api_instance = nucleus_client.TopicsApi(nucleus_client.ApiClient(configuration))

query = '("Trump" OR "president")' # str | Fulltext query, using mysql MATCH boolean query format. Example, (\"word1\" OR \"word2\") AND (\"word3\" OR \"word4\") (optional)
custom_stop_words = ["real","hillary"] # ERRORUNKNOWN | List of stop words. (optional)
num_topics = 8 # int | Number of topics to be extracted from the dataset. (optional) (default to 8)
metadata_selection ="" # str | json object of {\"metadata_field\":[\"selected_values\"]} (optional)
time_period =""# str | Time period selection (optional)

try:
    api_response = api_instance.get_topic_api(dataset, 
                                              query=query, 
                                              custom_stop_words=custom_stop_words, 
                                              num_topics=num_topics, 
                                              metadata_selection=metadata_selection,
                                              time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopicsApi->get_get_topic_api: %s\n" % e)


