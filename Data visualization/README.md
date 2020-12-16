# Data visualization

## Setting up

1. Go to Data visualization directory
2. Create config.py using config.py.example as a template
3. Go to Data visualization directory on command prompt
```cd "Data visualization"```
4. Install requirements using
```pip install -r requirements.txt```
5. Autogen using
```java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/road.yaml -o autogen -g python-flask```

## Running

### Run app.py to provide API for Graphql

1. Go to Data visualization directory on command prompt
```cd "Data visualization"```
2. Run app.py
```py app.py```
3. You can check if app.py run correctly by go to http://localhost:8080/road/v1/ui/#/ on your browser

### Run Graphql for data visualization
1. Run another command prompt then go to Data visualization directory
```cd "Data visualization"```
2. Type the following to run Graphql
```openapi-to-graphql --cors -u http://localhost:8080/road/v1 openapi/road.yaml```
3. You can check if Graphql run correctly by go to http://localhost:3000/graphql on your browser

## See data visualization
1. Go to Roughness-measurement-respository\Data visualization\html
2. Open index.html on your browser
3. See data visualization!
