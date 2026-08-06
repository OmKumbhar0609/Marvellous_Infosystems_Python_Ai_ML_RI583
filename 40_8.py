# Decision Tree Visualization
# Use: from sklearn.tree import plot_tree
# Visualize the trained decision tree.
# Which feature appears at the root node?
# Why do you think that feature was selected first?

from pyexpat import model

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(18,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail","Pass"],
    filled=True
)

plt.show()

print("Root Feature =",X.columns[model.tree_.feature[0]])


# The root node is the feature with the highest information gain.
# It best separates Pass and Fail students.