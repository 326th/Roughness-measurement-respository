# Data visualization

# Setting up

1. Go to Data visualization directory
2. Create config.py using config.py.example as a template
3. Go to Data visualization directory on command prompt
```cd "Data visualization"```
4. Install requirements using
```pip install -r requirements.txt```
5. Generate API using
```java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/road.yaml -o autogen -g python-flask```

# Running

## Run app.py to provide API for Graphql

1. Go to Data visualization directory on command prompt
```cd "Data visualization"```
2. Run app.py
```py app.py```
3. You can check if app.py run correctly by go to http://localhost:8080/road/v1/ui/#/ on your browser

## Run Graphql for data visualization
1. Run another command prompt then go to Data visualization directory
```cd "Data visualization"```
2. Type the following to run Graphql
```openapi-to-graphql --cors -u http://localhost:8080/road/v1 openapi/road.yaml```
3. You can check if Graphql run correctly by go to http://localhost:3000/graphql on your browser

## See data visualization
1. Go to Roughness-measurement-respository\Data visualization\html
2. Open index.html on your browser
3. See data visualization!

#API
The API to this Data visualization are describe as below
## Get the height of the road
URL ```road/v1/heights```
### Request
```
{
    "Accept": "application/json"
}
```
### Response
Example value
```
status code : 200
[
  {
    "ID": 0,
    "Latitude": 0,
    "Longitude": 0,
    "Height": 0
  }
]
```

## Get the accelerations
URL ```road/v1/accelerations```
###Request
```
{
    "Accept": "application/json"
}
```
###Response
Example value
```
status code : 200
[
  {
    "ID": 0,
    "Latitude": 0,
    "Longitude": 0,
    "Acceleration": 0
  }
]
```
## Get the average height of road
URL ```road/v1//heightAVG```
###Request
```
{
    "Accept": "application/json"
}
```
###Response
Example value
```
status code : 200
[
  {
    "Grouping": "string",
    "HeightAVG": 0
  }
]
```
## Get the average accelerations
URL ```road/v1//accelerationAVG```
###Request
```
{
    "Accept": "application/json"
}
```
###Response
Example value
```
status code : 200
[
  {
    "Grouping": "string",
    "AccelerationAVG": 0
  }
]
```
## Get the correlation
URL ```road/v1/correlation```
###Request
```
{
    "Accept": "application/json"
}
```
###Response
Example value
```
status code : 200
[
  {
    "Grouping": "string",
    "Correlation": 0
  }
]
```
## Get the a height and correlation of all grouping
URL ```road/v1//heightAndAcceleration```
###Request
```
{
    "Accept": "application/json"
}
```
###Response
Example value
```
status code : 200
[
  {
    "ID": 0,
    "Latitude": 0,
    "Longitude": 0,
    "Height": 0,
    "Acceleration": 0,
    "Grouping": "string"
  }
]
```