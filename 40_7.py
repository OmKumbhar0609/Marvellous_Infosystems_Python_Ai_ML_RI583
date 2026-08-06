# Train model using:
# random_state = 0
# random_state = 10
# random_state = 42
# Compare testing accuracy.
# Does the result change?

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

states = [0,10,42]

for rs in states:

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=rs
    )

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test,y_pred)

    print("Random State =",rs)
    print("Accuracy =",acc*100,"%")
    print("----------------------")

 # accuracy may change because each random state creates a different train-test split.