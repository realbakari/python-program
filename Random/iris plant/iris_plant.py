from sklearn import datasets
from sklearn import tree

# load the iris dataset
iris = datasets.load_iris()

# extract the features and labels
X = iris.data
y = iris.target

# split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# create the classifier
clf = tree.DecisionTreeClassifier()

# train the classifier
clf = clf.fit(X_train, y_train)

# make predictions on the testing data
y_pred = clf.predict(X_test)
