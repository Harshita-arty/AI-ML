import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([500, 1000, 1500, 2000, 2500]).reshape(-1,1) # Size in sq ft
y = np.array([100000, 200000, 300000, 400000, 500000])   # Price

# Train
model = LinearRegression()
model.fit(X, y)

# Predict
pred = model.predict([[1800]])
print("Predicted Price for 1800 sq ft =", pred[0])

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.show()