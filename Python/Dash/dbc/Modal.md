# Modal

Can use `Modal` to show errors in callbacks
```py
  html.Div(
      [
          dbc.Modal(
              [
                  dbc.ModalHeader(dbc.ModalTitle("Error"), close_button=True),
                  dbc.ModalBody(id='error-modal-message'),
                  dbc.ModalFooter(
                      dbc.Button(
                          "Try again",
                          id="close-error-modal",
                          className="ms-auto",
                          n_clicks=0,
                      )
                  ),
              ],
              id="error-modal",
              centered=True,
              is_open=False,
          ),
      ]
  ),

@app.callback
Output('error-modal', 'is_open'),
Output('error-modal-message', 'children'),

# get exception stacktrace
msg = str(exc) + '\n' + traceback.format_exc()
return html.Div(
    msg,
    className='h-100',
    style={
        'fontSize': '1.15rem',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
    },
)
```
