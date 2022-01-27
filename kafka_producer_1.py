#Produce message to a single topic and to any partition.
from kafka import KafkaProducer
import json, time
from random_data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['34.193.143.57:9092'],value_serializer=json_serializer)#Connect to kafka server running on AWS.

if __name__ == "__main__":
    while 1 == 1:
        registerd_user = get_registered_user()
        print(registerd_user)
                      #(topic name,           data    )
        producer.send("mynew", registerd_user)#if no topic's in there in Kafka, then it will create a new topic of this name provided.
        time.sleep(4)
