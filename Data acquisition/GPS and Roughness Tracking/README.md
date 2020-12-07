# Roughness-measurement

This repository provide you a way to collect average roughness of a road and publish it to MQTT server for futher use.

This repository is for Data Acquisition class final project.

## Requirements

- Kidbright device
- Python3
- Mobile Device
- Facebook account

## Setting up

### Setting up roughness measurement for Kidbright

1. Install imu.py module in your Kidbright device from git <a href=https://github.com/microBlock-IDE/micropython/tree/master/ports/esp32/boards/KidBright32/modules/imu.py>Here</a>.
2. In file <a href=https://github.com/326th/Roughness-measurement-respository/blob/master/Roughness%20measure.py>Roughness measure.py</a>, change the following:    
    - In line 46, change `WIFI_NAME` and `WIFI_PASSWORD` to the name and password of the wifi your kidbright will use.    
    - In line 52, change `MQTT_SERVER` to MQTT server you will use. 
3. Change TIMES and SLEEP in line 7,8 to the amount of times you will measure roughness to average and interval between each measures.

### Setting up GPS tracker

1. Download python libraries from <a href=https://github.com/326th/Roughness-measurement-respository/blob/master/requirements.txt>requirements.txt</a> using    
```pip install -r requirements.txt```

2. Create `.env` files that contains the following:
    - EMAIL={your Facebook username}  
    - PASS={your Facebook password}  
    - DRIVER_PATH={path to your Chrome driver (include the file name in the path) }  
    - BROWSER_PATH={path to your Chrome/Brave executable (include the file name in the path) }  
    - MQTT_SERVER={your MQTT server (must be the same as the one you used for Kidbright) }  
    
Example `.env` fle:
```
EMAIL=Example@exmail.com
PASS=PassWordGoesHere
DRIVER_PATH=C:/Users/USER/Desktop/chromedriver.exe
BROWSER_PATH=C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe
MQTT_SERVER=example.org
```

## Running

### Running Kidbright

You can run your kidbright with the file Roughness measure.py to run on your Kidbright with program like <a href=https://thonny.org/>Thonny<a>.
    
### Running GPS tracker

On Facebook, start sharing your location on any chat.  

run the following commmand,    
`python GPSextract.py`    
After that, the program will ask for the grouping name, you can enter any name.    

The program will boot up your browser and log in to Facebook for you. Open the chat containing your GPS tracking and press Ctrl + Shift + C then click the link to open gps location on map. This will highlight part of the code that links you to Bing map, right click then select Copy > Copy Xpath. Paste the Xpath in command line.  

Now the program will track everytime Kidbright signal then forward it to ku/daq2020/cosmic/suit with latitude, longitude and grouping name.
