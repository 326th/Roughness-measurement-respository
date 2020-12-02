# Roughness-measurement

This repository provide you a way to collect average roughness of a road and publish it to MQTT server for futher use.

This repository is for Data Acquisition class final project.

## Requirements

- Kidbright device
- Python3
- Mobile Device
- Facebook account

## Setting up

### Running roughness measurement for Kidbright

1. Install imu.py module in your Kidbright device from git <a href=https://github.com/microBlock-IDE/micropython/tree/master/ports/esp32/boards/KidBright32/modules/imu.py>Here</a>
2. In file <a href=https://github.com/326th/Roughness-measurement-respository/blob/master/Roughness%20measure.py>Roughness measure.py</a>, change the following:

   WIFI_NAME and WIFI_PASSWORD in line 46 to the name and password of the wifi your kidbright will use
   MQTT_SERVER in line 52 to MQTT server you will use
   
3. Change TIMES and SLEEP in line 7,8 to the amount of times you will measure roughness to average and interval between each measures
4. Run your Kidbright device

Your Kidbright device will now sent the average roughness and send them to channel ku/daq2020/cosmic/acc

For future uses, you only need to run step 4.
### Running GPS tracker
