## cyclical features
links:
- https://mlpills.substack.com/p/issue-89-encoding-cyclical-features
- https://skforecast.org/0.16.0/faq/cyclical-features-time-series.html

```py
df['cyc_sncs'] = df['cyc_sin'] * df['cyc_cos']
# Add squared terms to capture non-linear relationships
df['cyc_sin2'] = df['cyc_sin'] ** 2
df['cyc_cos2'] = df['cyc_cos'] ** 2
```

encoding types:
- one-hot
- sin/cos
- spine
- rbf

pros and cons:
- nn: sin/cos is good
- tree-based models (Random Forest, XGBoost, LightGBM): split features one at a time - cannot do that for sin/cos together
- prophet: automatically models seasonality using Fourier transformations - no need to encode cyclical features
