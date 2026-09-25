import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sklearn, dash
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

print("Python:", sys.version.split()[0])
print("numpy:", np.__version__, "| sklearn:", sklearn.__version__, "| dash:", dash.__version__)

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:, np.newaxis, 2]
X_train, X_test = X[:-20], X[-20:]
y_train, y_test = y[:-20], y[-20:]

model = linear_model.LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("MSE: %.2f" % mean_squared_error(y_test, y_pred))
print("R2:  %.2f" % r2_score(y_test, y_pred))

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.savefig("ols_result.png")
print("График сохранён в ols_result.png")