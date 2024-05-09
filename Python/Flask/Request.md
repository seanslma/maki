# Flask request

## attributes
In Flask, the `request` object represents the HTTP request sent by the client to your Flask application. 
It contains all the information about the request, such as headers, form data, files, and other metadata.

Here are some common attributes and methods of the `request` object:
- **`request.method`**: Returns the HTTP method used for the request (e.g., GET, POST, PUT, DELETE).
- **`request.args`**: Contains the query parameters from the URL.
- **`request.form`**: Contains the form data submitted with a POST request.
- **`request.files`**: Contains any files uploaded as part of the request.
- **`request.cookies`**: Contains any cookies sent with the request.
- **`request.headers`**: Contains the HTTP headers sent with the request.
- **`request.json`**: Returns the JSON data sent with the request (if the request body is JSON).

## example
We can access these attributes and methods within the Flask routes to retrieve information 
about the incoming request and process it accordingly. 
```py
from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        name = request.args.get('name')
        return f'Hello, {name}!'
    elif request.method == 'POST':
        data = request.form
        return f'Received data: {data}'

if __name__ == '__main__':
    app.run()
```

In this example, the `/example` route handles both GET and POST requests. If a GET request is received, it retrieves the 'name' query parameter from the URL using `request.args`. If a POST request is received, it retrieves the form data using `request.form`.
