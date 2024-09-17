import json
import paho.mqtt.client as mqtt
import datetime
import pika 
previous_date = ''
daily_pm25_values = []
dataFormat = {}

def on_connection(client, userdata, flags, rc):
    if rc == 0:
        print('Connection success', flush = True)
    else:
        print('Connection Fail', flush = True)

def on_message(client, userdata, message):
    resultData = json.loads(message.payload)
    #result={}
    flag=1
    #print(type(resultData))
    for key, value in resultData.items():
        timestamp = int(key)/1000

        dt_object = datetime.datetime.fromtimestamp(timestamp)
        formatted_date = dt_object.strftime('%Y/%m/%d %H:%M:%S')
        ####if float(value.replace(',','')) > 50:
        if float(value) > 50:
            print("Expection value {} in {}".format(value, dt_object), flush = True) 
        else:
            global previous_date,daily_pm25_values
            #result[formatted_date] = value
            #print(formatted_date+' and '+previous_date)
            if formatted_date[:10] != previous_date[:10] and previous_date != ''or flag == len(resultData):
                #print(formatted_date,previous_date)
                average_pm25 = sum(daily_pm25_values) / len(daily_pm25_values)
                dataFormat[previous_date] = average_pm25
                daily_pm25_values = []  
            #daily_pm25_values.append(float(value.replace(',', '')))	
            daily_pm25_values.append(float(value))

        previous_date = formatted_date
        flag += 1
        
    #print("average PM2.5 value:")
    print(dataFormat)
    #print(result)
    
    rabbitmqIP = '192.168.0.100'
    rabbitmqPort  = 5672
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqIP,port = rabbitmqPort))
    channel = connection.channel()
    channel.queue_declare(queue = 'pm2.5')
    channel.basic_publish(exchange='',routing_key = 'pm2.5', body = json.dumps(dataFormat))
    print('sendings success')

client = mqtt.Client()

broker_address = "192.168.0.102"
port = 1883

client.on_connect = on_connection
client.connect(broker_address, port)

topic = "pm2.5_data"
client.subscribe(topic)

client.on_message = on_message

client.loop_forever()
