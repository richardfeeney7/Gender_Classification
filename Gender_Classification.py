from sklearn import tree

classifier = tree.DecisionTreeClassifier()

Y = ['male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male'] # 10 People

# Store a list containing list in the variable x. The 3 numbers are the length, width and shoe size of a person
X = [ [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],[190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

classifier = classifier.fit(X, Y)

pred = classifier.predict([[160, 70, 37]])

print(pred)