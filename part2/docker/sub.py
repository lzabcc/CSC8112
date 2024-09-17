import json
import paho.mqtt.client as mqtt
import datetime

previous_date = ''
daily_pm25_values = []
dataFormat = {}

def on_connection(client, userdata, flags, rc):
    if rc == 0:
        print('Connection success')
    else:
        print('file')

def on_message(client, userdata, message):
    resultData = json.loads(message.payload)
    result={}
    flag=1
    #print(type(resultData))
    for key, value in resultData.items():
        timestamp = int(key)/1000

        dt_object = datetime.datetime.fromtimestamp(timestamp)
        formatted_date = dt_object.strftime('%Y/%m/%d/%H/%M')
        if float(value.replace(',','')) > 50:
            print("Expection value {} in {}".format(value, dt_object)) 
        else:
            global previous_date,daily_pm25_values
            result[formatted_date] = value
            #print(formatted_date+' and '+previous_date)
            if formatted_date[:10] != previous_date[:10] and previous_date != ''or flag == len(resultData):
                #print(formatted_date,previous_date)
                average_pm25 = sum(daily_pm25_values) / len(daily_pm25_values)
                dataFormat[previous_date] = average_pm25
                daily_pm25_values = []  # 重置当天的PM2.5数据
	
            daily_pm25_values.append(float(value.replace(',', '')))

        previous_date = formatted_date
        flag += 1
        
    print("每天的平均PM2.5值:")
    print(dataFormat)
    #print(result)

client = mqtt.Client()

broker_address = "localhost"
port = 1883

client.on_connect = on_connection
client.connect(broker_address, port)

topic = "pm25_data"
client.subscribe(topic)

client.on_message = on_message

client.loop_forever()
