from decouple import config
import time
import paho.mqtt.client as mqtt

gps = [-1,-1]
acc = 0

Grouping = input('Enter your grouping : ')

def on_message(client, userdata, message):
    global gps, acc
    if (str(message.topic) == "ku/daq2020/cosmic/gps"):  
        gps = str(message.payload.decode("utf-8"))
        buff = dict()

        for subString in gps.split(","):
            split = subString.split(":")
            buff[split[0].strip('"')] = split[1]
        gps = [buff['{"latitude'],buff['longitude']]
        
    elif (str(message.topic) == "ku/daq2020/cosmic/acc"):
        acc = str(message.payload.decode("utf-8"))
        if (gps != [-1,-1]):
            client.publish("ku/daq2020/cosmic/suit",
                           gps[0]+","+gps[1]+","+acc+',"'+Grouping+'"')

mqttBroker = config('MQTT_BROKER')
client = mqtt.Client("GPS")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("ku/daq2020/cosmic/acc")
client.subscribe("ku/daq2020/cosmic/gps")
client.on_message=on_message
print(f"""Currently listening to {mqttBroker}/ku/daq2020/cosmic/suit and {mqttBroker}/ku/daq2020/cosmic/acc
then combine the data and publish to {mqttBroker}/ku/daq2020/cosmic/suit""")


