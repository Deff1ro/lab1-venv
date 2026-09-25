import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Python:", sys.version.split()[0])
print("numpy:", np.__version__, "| pandas:", pd.__version__,
      "| sklearn:", sklearn.__version__, "| seaborn:", sns.__version__)

df = pd.read_csv("data/bottle_small.csv")
df_binary = df[["Salnty", "T_degC"]].copy()
df_binary.columns = ["Sal", "Temp"]
print(df_binary.head())

def fit(data, name):
    data = data.ffill().dropna()
    X = data[["Sal"]].to_numpy()
    y = data[["Temp"]].to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    regr = LinearRegression().fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    print(f"\n[{name}] R2 score: {regr.score(X_test, y_test):.4f}")
    plt.figure()
    plt.scatter(X_test, y_test, color="b", s=5)
    plt.plot(X_test, y_pred, color="k")
    plt.savefig(f"result_{name}.png")
    return y_test, y_pred

fit(df_binary, "full")

df500 = df_binary[:500]
sns.lmplot(x="Sal", y="Temp", data=df500, order=2, ci=None)
plt.savefig("scatter_500.png")
y_test, y_pred = fit(df500, "first500")

mse = mean_squared_error(y_test, y_pred)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mse)
print("RMSE:", np.sqrt(mse))