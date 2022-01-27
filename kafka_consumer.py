from kafka import KafkaConsumer, consumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer("registered_user",#Topic name
                            bootstrap_servers=['34.193.143.57:9092'],#Kaka server
                            auto_offset_reset='earliest',#from where to start read from offset
                            group_id="consumner-group-a")#consumner group id. if not provided, it will create one.

    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))