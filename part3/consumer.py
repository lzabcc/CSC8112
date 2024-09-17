import json
import pika
import pandas as pd
import matplotlib.pyplot as plt
import threading
import draw 
import predict as pre


rabbitmq_ip = "192.168.0.100"
rabbitmq_port = 5672
rabbitmq_queque = "pm2.5"
data_df= pd.DataFrame(columns=['Timestap','Values'])
data_list =[]
data_lock = threading.Lock()

def process_data(data_df):
    draw.draw_chart(data_df)
    pre.predict(data_df)

def consume_messages():
	channel.start_consuming()


def callback(ch, method, properties, body):
    global data_list,data_df
    data = json.loads(body)
    with data_lock: 
        for timestamp_str, value in data.items():
            timestamp_obj = (timestamp_str) 
            data_list.append({"Timestamp": timestamp_obj, "Value": value})
        data_df=pd.DataFrame(data_list)
		
    print(f"Got message from producer msg: {data_df}")
    process_data(data_df)
    data_list=[]


def on_connect(client, userdata, flags ,rc):
	if rc == 0:
		print('connection success', flush = True)
	else:
		print('connection fail',flush = True)



connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port))

channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queque)

channel.basic_consume(queue=rabbitmq_queque,auto_ack=True, on_message_callback=callback)


consumer_thread = threading.Thread(target=consume_messages)
consumer_thread.start()
#channel.start_consuming()
