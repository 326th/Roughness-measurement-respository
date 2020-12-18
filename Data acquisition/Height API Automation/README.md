# Height API Automation

These Node-RED files allow you to get data from GPS in Acceleration table and then migrate to Height table and assign its sea elevation value via Open elevation API

## Requirements

- Data of GPS locations in Acceleration table (Can get by following [GPS and roughness automation](https://github.com/326th/Roughness-measurement-respository/blob/master/Data%20acquisition/GPS%20and%20Roughness%20Automation/README.md))
- Node-RED server

## Set up

1. Import `API request Automation.json` and `Height table migrate.json` to your Node-RED server
2. Open the flow imported from `Height table migrate.json` (Import lat lon to height) then click on the either of node `Edit your database here` and edit `Your Database` based on your database setting
3. Hit deploy

## Running

1. In the flow imported from`Height table migrate.json` (Import lat lon to height), click inject node and waits until it import every unique location to Height table (when done, it will display the message)
2. In the flow imported from `API request Automation.json` (Height API request) then click inject and waits until it assigns elevation to every GPS (when done, it will display the message)
