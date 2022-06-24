# Dashboard

## output logging info from dashboard
https://ipywidgets.readthedocs.io/en/latest/examples/Output%20Widget.html
```
import logging
import ipywidgets as widgets

class OutHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super(OutHandler, self).__init__(*args, **kwargs)
        layout = {
            'width': '100%',
            'height': '160px',
            'border': '1px solid black'
        }
        self.out = widgets.Output(layout=layout)

    def emit(self, record):
        formatted_record = self.format(record)
        new_output = {
            'name': 'stdout',
            'output_type': 'stream',
            'text': formatted_record+'\n'
        }
        self.out.outputs = (new_output, ) + self.out.outputs

    def show_logs(self):
        display(self.out)

    def clear_logs(self):
        self.out.clear_output()

logger = logging.getLogger(__name__)
out_hdr = OutHandler()
out_hdr.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s'))
logger.addHandler(out_hdr)
logger.setLevel(logging.INFO)
out_hdr.show_logs()

# In app
out_hdr.clear_logs()

try:
    x = 1/ 0
excep as Exception as exec:
    logger.exception(exec)
```
