import re
import json
from collections import defaultdict
import plotly.graph_objects as go
from kafka import KafkaConsumer

# Initialize Kafka consumer
consumer = KafkaConsumer('tweet', bootstrap_servers=['localhost:9092'])

# Initialize data structure for visualization
data = defaultdict(int)

# Function to extract hashtags from text
def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

# Function to consume messages from Kafka
def consume_messages():
    while True:
        for msg in consumer:
            msg_value = json.loads(msg.value.decode('utf-8'))
            text = msg_value.get('text')
            print("Received message:", text)
            if text:
                hashtags = extract_hashtags(text)
                if hashtags:
                    for hashtag in hashtags:
                        data[hashtag] += 1
                    update_graph()
                else:
                    print("No hashtags found in the message. Moving to the next message.")

# Function to update and display the graph
def update_graph():
    x_vals = list(data.keys())
    y_vals = list(data.values())
    fig = go.Figure([go.Bar(x=x_vals, y=y_vals, name='Hashtag Counts')])
    fig.update_layout(title='Real-Time Hashtag Analysis', xaxis_title='Hashtag', yaxis_title='Count')
    fig.show()

# Main function to run the real-time data processing and visualization
def main():
    consume_messages()

if _name_ == "_main_":
    main()
