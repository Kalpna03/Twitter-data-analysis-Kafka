import csv
import json
from kafka import KafkaProducer
from configparser import ConfigParser
import time

def read_and_send_tweets(dataset_path, producer, topic_name):
    with open(dataset_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tweet_text = row["Tweet"]
            producer.send(topic_name, value={"text": tweet_text})
            time.sleep(1)  # Simulate real-time ingestion by adding a delay

if _name_ == "_main_":
    config_file_path = "../conf/hashtags.conf"  # Update with the path to your config file
    config = ConfigParser()
    config.read(config_file_path)

    bootstrap_server = config['Kafka_param']['bootstrap.servers']
    topic_name = config['Resources']['app_topic_name']

    producer = KafkaProducer(bootstrap_servers=[bootstrap_server],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    dataset_path = "C:/Users/Kalpn/Downloads/REF TWEETS.csv"  # Update with the path to your dataset
    read_and_send_tweets(dataset_path, producer, topic_name)
