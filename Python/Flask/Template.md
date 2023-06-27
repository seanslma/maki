# Template

In Flask, the render_template function is used to render HTML templates and generate dynamic content to be displayed in the web browser.

## example
```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "My Flask App"
    name = {
        'first_name': 'John',
        'last_name': 'Dale',
    }
    return render_template('index.html', title=tile, name=name)

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    {% if name['first_name'] == "": %}
    <h1>Hello my love</h1>
	  {% else %}
    <h1>Hello {{ name['first_name'] + " " + name['last_name'] }}</h1>
	  {% endif %}  
</body>
</html>
```
