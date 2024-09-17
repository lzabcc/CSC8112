import requests
import json

import paho.mqtt.client as mqtt


if __name__ == '__main__':
    url = "http://uoweb3.ncl.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime=20230601&endtime=20230831"

    # #get data previous
    # resp = requests.get(url)
    # data_str = resp.text
    #
    # dict_strings = data_str.split('},')
    # dict_final = {}
    #
    # for dict_string in dict_strings:
    #     if "PM2.5" in dict_string:
    #
    #         timestamp_index = dict_string.find("Timestamp")
    #         value_index = dict_string.find("Value")
    #
    #         timestamp = dict_string[timestamp_index + 12:timestamp_index + 25]
    #         value = dict_string[value_index + 8:value_index + 13]
    #         dict_final[timestamp] = value
    # #print(dict_final)

    resp = requests.get(url)
    data_dict = json.loads(resp.text)

    filtered_data = data_dict.get('sensors', [])[0].get('data', {}).get('PM2.5', [])
    pm25_data = {}

    for item in filtered_data:
        timestamp = item['Timestamp']
        value = item['Value']
        pm25_data[timestamp] = value


    ##########
    #send data
    emqx_host = "192.168.0.102"
    emqx_port = 1883

    mqtt_topic = "pm2.5_data"

    client = mqtt.Client()
    client.connect(emqx_host, emqx_port, 60)


    payload = json.dumps(pm25_data)

    try:
        # publish to emqx server
        client.publish(mqtt_topic, payload)
        print("PM2.5 data is sended successfully")
    except Exception as e:
        print("something went wrong when" +
              "sending these datas:", str(e))


