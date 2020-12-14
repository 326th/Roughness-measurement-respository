from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import config
import time
import paho.mqtt.client as mqtt

DRIVER_PATH = config('DRIVER_PATH')
BROWSER_PATH = config('BROWSER_PATH')
DELAY = 1

def set_up(driver_path,browser_path):
    """
    set up  browser with custom driver and browser path
    """

    option = webdriver.ChromeOptions()
    option.binary_location = browser_path
    browser = webdriver.Chrome(executable_path=driver_path,  options=option)
    return browser

area_group = input("please enter area grouping : ")
browser_host = set_up(DRIVER_PATH,BROWSER_PATH)
browser_host.get("https://www.facebook.com/")
time.sleep(DELAY)
username_field = browser_host.find_element_by_name("email")
username_field.send_keys(config('EMAIL'))
password_field = browser_host.find_element_by_name("pass")
password_field.send_keys(config('PASS'))
password_field.send_keys(Keys.ENTER)
facebook = browser_host.window_handles[0]

while True:
    try:
        Xpath = input("enter Xpath for gps tracking : ")
        break
    except:
        print("can't press the button, try again")

def set_up_facebook():
    time.sleep(DELAY)
    browser_host.find_element_by_xpath(Xpath).click()
def get_coor():
    set_up_facebook()
    time.sleep(DELAY)
    coor = browser_host.window_handles[1]

    browser_host.switch_to.window(coor)
    browser_host.find_element_by_xpath('//*[@id="maps_sb_container"]/div[1]/div[2]/a').click()
    time.sleep(DELAY)
    browser_host.find_element_by_xpath('//*[@id="maps_sb_container"]/div[1]/a/div/div/div').click()
    time.sleep(DELAY)
    latlong = browser_host.find_element_by_xpath('//*[@id="bm_overflowText"]').text
    browser_host.close()
    browser_host.switch_to.window(facebook)
    return latlong

def on_message(client, userdata, message):
    latlong = get_coor()
    client.publish("ku/daq2020/cosmic/suit", latlong + "," + str(message.payload.decode("utf-8"))+',"'+area_group+'"')

mqttBroker = config('MQTT_BROKER')
client = mqtt.Client("GPS")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("ku/daq2020/cosmic/acc")
client.on_message=on_message
print(f"""Currently listening to {mqttBroker}/ku/daq2020/cosmic/acc for acceleration data
After receiveing the data, it will be sent along with latitude and longtitude and area to {mqttBroker}/ku/daq2020/cosmic/suit""")



