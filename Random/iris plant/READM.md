Here is an example of a simple machine learning model in Python using the scikit-learn library. This model is a decision tree classifier, which is a type of model that makes predictions based on the value of different features in the data. In this example, we will train the model to predict the type of iris plant based on its sepal and petal length and width.

First, we need to import the necessary libraries:
```
from sklearn import datasets
from sklearn import tree
```
Next, we will load the iris dataset and split it into training and testing sets:

```
# load the iris dataset
iris = datasets.load_iris()

# extract the features and labels
X = iris.data
y = iris.target

# split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
```
Now, we will create the decision tree classifier and train it on the training data:

```
# create the classifier
clf = tree.DecisionTreeClassifier()

# train the classifier
clf = clf.fit(X_train, y_train)
```

Finally, we can use the trained model to make predictions on the testing data:

```
# make predictions on the testing data
y_pred = clf.predict(X_test)
```
This simple example shows how to use the scikit-learn library to build and train a machine learning model in Python. Of course, there are many other types of machine learning models and algorithms that can be used in a similar way.