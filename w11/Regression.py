import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=1, noise=25, random_state=1)

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)

plt.scatter(X, y, color='orange', label='Points')
plt.plot(X, pred, color='blue', label='Line')
plt.title("Regression Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
