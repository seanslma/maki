# Forecast

## Train model
```py
# Train the LightGBM model
params = {
    'objective':'regression', 
    'metric':'mae',
    'seed': 13, 
    'verbosity': -1,  # suppress all output [-1, 0, 1, 2]
    'force_col_wise': True, # only for cpu
    'learning_rate': 0.05, 
    'num_leaves': 40,
    'max_depth': 20, 
    'min_data_in_leaf': 100, 
    'feature_fraction': 0.8, 
    'bagging_fraction': 0.9, 
    'bagging_freq': 2, 
    'lambda_l1': 0.5, 
    'lambda_l2': 2.5,
}

# Create dataset for LightGBM
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Train the model
t0 = time()
model = lgb.train(
    params=params, 
    train_set=train_data, 
    valid_sets=[test_data], 
    num_boost_round=10000, 
    callbacks=[
        lgb.early_stopping(stopping_rounds=100, verbose=False), # verbose: log message with early stopping information
        lgb.log_evaluation(500), # output every 500 boosts
    ],
)
print(f'lgb model training time: {time() - t0:.3f} seconds')
```

## Predict
```py
# Make predictions
y_pred = model.predict(X_test, num_iteration=model.best_iteration)

# Evaluate the model
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'RMSE: {rmse:.3f}')

# Plot the actual vs predicted values
plt.figure(figsize=(14, 4))
plt.plot(y_test.index, y_test.values, label='Actual', color='black')
plt.plot(y_test.index, y_pred, label='Predicted', color='blue')
plt.plot(y_test.index, y_pred - y_test.values + 1000, label='Error', color='red')
plt.legend()
plt.title('Forecasting with LightGBM')
plt.grid(True)
plt.show()
```

## plotly
```py
fig = go.Figure()

# Add traces
x_val = y_test.index
y_val = y_test.values
fig.add_trace(go.Scatter(x=[x_val[0], x_val[-1]], y=[-100, -100], mode='lines', name='', line=dict(color='white'), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=y_val, mode='lines', name='Actual', line=dict(color='black')))
fig.add_trace(go.Scatter(x=x_val, y=y_pred, mode='lines', name='Predicted', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=x_val, y=y_pred - y_val + 1000.0, mode='lines', name='Error', line=dict(color='red')))

# Customize the layout
fig.update_layout(
    title='Forecasting with LightGBM',
    xaxis_title='Time',
    yaxis_title='Forecast',
    showlegend=True,
    xaxis_gridcolor='lightgray',
    yaxis_gridcolor='lightgray',
    height=600,
    margin=dict(t=0, b=0, l=0, r=0),
)
fig.show()
```
