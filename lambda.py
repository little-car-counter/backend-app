import json
import trafficlog_to_es


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))

    # Load data into ES
    try:
        trafficlog_to_es.load(event['device_id'], event['traffic_instances'])

    except Exception as e:
        print(e)
        print('Error loading data into ElasticSearch')
        raise e
