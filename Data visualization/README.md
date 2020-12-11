# Data visualization

## STEP1: Run app.py to provide API for Graphql
1. Go to Data visualization directory
```cd "Data visualization"```
2. Run app.py
```py app.py```
3. You can check if app.py run correctly by go to http://localhost:8080/road/v1

## STEP2: Run Graphql for data visualization
1. Run another command prompt then go to Data visualization directory
```cd "Data visualization"```
2. Type the following to run Graphql on http://localhost:8090
```openapi-to-graphql --cors -u http://localhost:8080/road/v1 openapi/road.yaml```
