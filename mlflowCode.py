import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


mlflow.set_experiment("mlflow-models-demo")

with mlflow.start_run():

    model = LinearRegression()
    model.fit(X_train, y_train)


    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)


    mlflow.log_metric("mse", mse)


    mlflow.sklearn.log_model(model, "linear-regression-model")

    print("Model trained and logged with MSE:", mse)
