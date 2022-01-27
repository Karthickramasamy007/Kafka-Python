#Produce message to a single topic and to a selected partition.
from kafka import KafkaProducer
import json, time
from random_data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

#Return partition that producer want to send message to.
def get_partition(key, all, available):
    return 1


#Connecte to Kafka server on AWS, convert data into Json format, and seleted partition to publish.
producer = KafkaProducer(bootstrap_servers=['52.201.34.4:9092'],
                                            value_serializer=json_serializer,
                                            partitioner=get_partition)

if __name__ == "__main__":
    while 1 == 1:
        registerd_user = get_registered_user()
        print(registerd_user)
        producer.send("registered_user", registerd_user)#if no topic's in there in Kafka, then it will create a new topic of this name provided.
        time.sleep(4)
