# Predict results for X_test. Display predicted values along with actual values.

from xml.parsers.expat import model

import pandas as pd

y_pred = model.predict(X_test)

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(result)