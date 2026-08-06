# Train model with: max_depth = None
# Calculate:
# Training accuracy
# Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(
max_depth=None,
random_state=42
)

model.fit(X_train,y_train)

train_pred = model.predict(X_train)

test_pred = model.predict(X_test)

train_acc = accuracy_score(y_train,train_pred)

test_acc = accuracy_score(y_test,test_pred)

print("Training Accuracy =",train_acc*100,"%")

print("Testing Accuracy =",test_acc*100,"%")


# If training accuracy is 100% but testing accuracy is lower, the model is overfitting.
# The Decision Tree memorizes the training data instead of learning general patterns.
# It performs perfectly on the training set but poorly on unseen data.
# Limiting the tree depth (max_depth) helps reduce overfitting.