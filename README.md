## Python flask app

This is a flask app that has the following API Endpoint 

```
GET /pathway/stats
```

This is a GET endpoint to query the local CSV file which has the following columns 

```
session_end_date,age_range,itla_code,gender,pathway_start,pathway_end,dx_count,final_dx_code,final_dx_description,count
```

The API endpoint accepts **any** of the column name as a **query parameter**. 
- When query parameters are passed, the app will look for exact match based on the query parameters and returns the filtered data.
- When no query parameters are passed, the whole dataset is returned


### How to run?

```
pip install Flask

flask run
```
This will expose the API on `http://127.0.0.1:5000`