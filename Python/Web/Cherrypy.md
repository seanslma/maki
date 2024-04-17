# Cherrypy

We can leverage CherryPy as the web server and Flask as the application framework within that server. 

**CherryPy as the Web Server:**
* CherryPy is a full-fledged web framework with its own routing and request handling mechanisms. However, it also offers the flexibility to function purely as a lightweight WSGI (Web Server Gateway Interface) compliant web server.

**Flask as the WSGI Application:**
* Flask, on the other hand, is a minimalistic web framework that focuses on building web applications but relies on a separate WSGI server to handle the underlying communication with web clients.

**Integration Approach:**
1. **Create Flask App:** Develop your web application logic using Flask's routing, templating, and other functionalities.
2. **WSGI Conversion:**  Convert your Flask application into a WSGI callable object. Flask applications inherently follow the WSGI specification, so you typically don't need extensive modifications.
3. **CherryPy Configuration:** Configure CherryPy to act as the WSGI server and mount your Flask application at a specific URL path. CherryPy provides mechanisms to mount WSGI applications like Flask.

**Benefits:**
* **Leverage CherryPy's Features:** You can potentially benefit from CherryPy's built-in features like static file serving or advanced session management alongside your Flask application.

**Drawbacks:**
* **Increased Complexity:**  This approach adds a layer of complexity compared to using Flask's built-in development server for simple deployments.
* **Potential Conflicts:**  There might be subtle conflicts between routing or configuration options between CherryPy and Flask if not managed carefully.

**Alternatives:**
* **Consider Gunicorn:** Gunicorn is a popular WSGI server specifically designed for production use with Python web frameworks like Flask. It offers a simpler and more focused solution compared to using CherryPy as a WSGI server.
* **Standalone Flask Server:** For development or testing, you can often leverage Flask's built-in development server by running your Flask application directly. This is a quick and easy way to get started without needing a separate WSGI server.

**Choosing the Right Approach:**
The decision of whether to use CherryPy as a WSGI server with Flask depends on your specific needs. If your application requires features beyond Flask's core functionality and you're comfortable managing some additional complexity, then using CherryPy as the WSGI server can be an option. However, for many scenarios, using Gunicorn or Flask's built-in development server might be more straightforward and suitable.

## Cherrypy and Flask
CherryPy handling static files and Flask handling application 

app.py
```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello from Flask!"
```

server.py
```py
import cherrypy

from .app import app  # Assuming app.py is in the same directory

# Define the static directory path
class HelloWorld(object):
  @cherrypy.expose
  def index(self):
    return "Hello world!"

  @cherrypy.expose
  def goodbye(self):
    return "Goodbye world!"

# Optional: Additional configuration
cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 5000
})

cfg = {}
cfg['/static'] = {
    'tools.staticdir.dir': str(static).replace('\\','/'),
    'tools.staticdir.on': True,
}

# Mount static handler
cherrypy.tree.mount(HelloeWorld(), '/', cfg)
# Mount Flask app at the root path (`/app`)
cherrypy.tree.mount(app, '/api')

# Start the CherryPy server
cherrypy.engine.start()
cherrypy.engine.block()
```
