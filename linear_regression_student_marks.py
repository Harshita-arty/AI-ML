import numpy as np
from sklearn.linear_model import LinearRegression

# Data: Hours studied vs Marks
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([20, 40, 50, 65, 80])

model = LinearRegression()
model.fit(X, y)

hours = 10
predicted = model.predict([[hours]])
print(f"Predicted marks for {hours} hours of study = {predicted[0]:.2f}")