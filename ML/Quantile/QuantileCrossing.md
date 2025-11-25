# Quantile crossing using lightgbm
Where lower quantile prediction (e.g., $\alpha=0.05$) is higher than central quantile prediction (e.g., $\alpha=0.50$ or the median) in quantile regression is called `Quantile Crossing` or `Quantile Non-Monotonicity`.

That's because we train separate models for each quantile independently.

Solutions:

## post processing with `sorting`
```py
sorted_preds = np.sort([q05_preds, q50_preds, q95_preds], axis=0)
q05_corrected = sorted_preds[0]
q50_corrected = sorted_preds[1]
q95_corrected = sorted_preds[2]
```

## post processing with `isotonic regression`
```py
import numpy as np
from sklearn.isotonic import IsotonicRegression

# Example quantile predictions from LightGBM model
q05_preds = model.predict(X, num_iteration=model.best_iteration, quantile=0.05)
q50_preds = model.predict(X, num_iteration=model.best_iteration, quantile=0.50)
q95_preds = model.predict(X, num_iteration=model.best_iteration, quantile=0.95)

# Quantile levels corresponding to the predictions
quantiles = np.array([0.05, 0.50, 0.95])

# Stack the predictions for isotonic regression
vals = np.array([q05_preds, q50_preds, q95_preds])

# Apply isotonic regression to enforce monotonicity
iso = IsotonicRegression(increasing=True)
corrected_vals = np.array([iso.fit_transform(quantiles, preds) for preds in vals])

# Corrected quantiles
q05_corrected = corrected_vals[0]
q50_corrected = corrected_vals[1]
q95_corrected = corrected_vals[2]
```

## Feature Selection / Regularization (Preventive)
Quantile crossing is often a sign of overfitting or instability in the model's structure.

Action: Before training, try these steps to stabilize the individual models:
- Reduce Overfitting: Increase regularization (lambda_l1, lambda_l2), decrease learning_rate, and increase min_child_samples.
- Feature Selection: Crossing often happens when the model latches onto noisy features. Try reducing the number of input features (X) to see if the crossing disappears.
- Bigger Dataset: If possible, train on more data. More data usually leads to more stable quantile estimates.

## Constraint Enforcement (Advanced/Robust)
For a robust, production-ready solution, you should enforce the constraint during the modeling process.

**Recursive/Sequential Modeling (The Best Approach)**. Instead of training $K$ independent models, you train them sequentially and use the output of the previous model as a feature in the next.
- Train $M_{0.05}$: Train the model for $\tau=0.05$.
- Train $M_{0.50}$: Train the model for $\tau=0.50$, but add the predictions from $M_{0.05}$ as a new input feature (X).
- Train $M_{0.95}$: Train the model for $\tau=0.95$, and add the predictions from $M_{0.50}$ as a new input feature (X).


