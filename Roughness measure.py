import time
import network
from machine import Pin
from umqtt.robust import MQTTClient
import imu
from decouple import config

TIMES = 100
SLEEP = 0.1 

## imu set up
acc = imu.acc
save = [0,0,0]
def diff(start, end):
    re = [0,0,0]
    for x in range (3):
        re[x] = start[x] - end[x]
    return re

def copy(target):
    re = [0,0,0]
    for x in range (3):
        re[x] = target[x]
    return re

def get_acc():
    global acc, save
    save = copy(acc)
    imu.update()
    return abs(diff(save, acc)[1])

def get_avg_acc(times,sleep_time):
    avg = 0
    for itera in range(times):
        avg += get_acc()
        time.sleep(sleep_time)
    return avg/times

## connect wifi
led_iot = Pin(12, Pin.OUT)
led_wifi = Pin(2, Pin.OUT)
led_wifi.value(1) # turn it off
led_iot.value(1)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("*** Connecting to WiFi...")
wlan.connect("WIFI_NAME","WIFI_PASSWORD")
while not wlan.isconnected():
    time.sleep(0.5)
print("*** Wifi connected")
led_wifi.value(0)
## connect broker
mqtt = MQTTClient("Acc","MQTT_SERVER")
print("*** Connecting to MQTT broker...")
mqtt.connect()
print("*** MQTT broker connected")
led_iot.value(0)

while True:
    mqtt.publish("ku/daq2020/cosmic/acc",str(get_avg_acc(TIMES,SLEEP)))