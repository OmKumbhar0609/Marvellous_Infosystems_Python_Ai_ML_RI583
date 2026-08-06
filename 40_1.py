# After training the Decision Tree model, use: model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

# Feature Importance

from re import X

import pandas as pd
from pyexpat import model
from turtle import pd


importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(importance)

# Most important feature
most = importance.loc[importance["Importance"].idxmax()]
print("\nMost Important Feature:")
print(most)

# Least important feature
least = importance.loc[importance["Importance"].idxmin()]
print("\nLeast Important Feature:")
print(least)