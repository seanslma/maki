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
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def api_get():
    name = request.args.get('name')
    return f'Hello, {name}!'

@app.route('/files', methods=['POST'])
def api_post():
    file = request.files.get('file')
    name = request.form.get('name')
    platform = request.form.get('platform')
    
    return Response(status=200)

if __name__ == '__main__':
    app.run()
```

how to call the api (assume the api is mounted on `/api`)
```py
import requests
def publish_file(
    filepath,
    *,
    name='test',
    platform='linux-64',
    api_url='https://example.com',
):
    url = f'{api_url}/api/files'
    files = {'file': open(filepath, 'rb')}
    params = {'name': name, 'platform': platform}
    r = requests.post(url, files=files, data=params)
    if r.status_code != 200:
        try:
            msg = r.json().get('message')
        except json.JSONDecodeError:
            msg = r.text
        finally:
            raise Exception(msg)

filepath = '/path/to/file/data.csv'
publish_file(filepath)
```
