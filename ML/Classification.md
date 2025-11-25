# Classification

## Confusion Matrix and Classification Report
classfication report
```py
from sklearn.metrics import (
    accuracy_score,
    mean_squared_error,
    mean_absolute_error,
    confusion_matrix,
    classification_report,
)
conf_matrix = confusion_matrix(y_actual, y_pred)   # confusion matrix
classif_report = classification_report(            # classification report
    y_actual, y_pred, zero_division=0
)
print(f'Confusion matrix:\n{conf_matrix}')
print(f'Classification report:\n{classif_report}')
```
