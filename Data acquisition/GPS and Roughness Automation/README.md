# GPS and roughness automation

This programs provide you a way to collect average roughness of a road and store it to Database.

This repository is for Data Acquisition class final project.

## Requirements

- Kidbright device
- Python3
- Mobile Device
- Facebook account
- Node-RED on mobile
- MQTT Broker

## Setting up

### Setting up roughness measurement for Kidbright

1. Install imu.py module in your Kidbright device from git <a href=https://github.com/microBlock-IDE/micropython/tree/master/ports/esp32/boards/KidBright32/modules/imu.py>Here</a>.
2. In file `Roughness_measure.py`, change the following:    
    - In line 46, change `WIFI_NAME` and `WIFI_PASSWORD` to the name and password of the wifi your kidbright will use.    
    - In line 52, change `MQTT_BROKER` to MQTT Broker you will use. 
3. Change TIMES and SLEEP in line 7,8 to the amount of times you will measure roughness to average and interval between each measures.

### Setting up GPS tracker

1. Download python libraries from `requirements.txt` using    
```pip install -r requirements.txt```

2. Create `.env` files that contains the following:
    - MQTT_BROKER={your MQTT broker (must be the same as the one you used for Kidbright) }  
    
Example `.env` fle:
```
MQTT_BROKER=iot.cpe.ku.ac.th
```

### Setting up Node-RED Database Handler (For PC or Moblie)

1. Import `Node-RED_GPS_Automation.json` to your Node-RED

2. Edit node `Edit your Mqtt Broker node here` and edit `Your MQTT Broker` then change `MQTT_BROKER` to your MQTT Broker

3. Edit node `Edit your Database Here` and edit `Your Database` based on your database setting

### Setting up Node-RED GPS tracker (Mobile only)

1. Import `Node-RED-Mobile_GPS_tracking.json` to your mobile Node-RED

2. Edit node `ku/daq2020/cosmic/gps` and edit `Your MQTT Broker` then change `MQTT_BROKER` to your MQTT Broker

## Running

### Running Node-RED Database Handler

Press the Deploy button

### Setting up Node-RED GPS tracker 

Press the button next to `Subscribe` Node

### Running Kidbright

You can run your kidbright with the file `Roughness_measure.py` to run on your Kidbright with program like <a href=https://thonny.org/>Thonny<a>.
    
### Running GPS tracker

1. Run `GPSextract.py` on Idle

2. Enter your grouping are on the prompt `Enter your grouping : `

## Once you ran all 4 programs, your location and roughness will be track and automatically added to your database
