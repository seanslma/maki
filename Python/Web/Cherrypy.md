# Cherrypy

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
