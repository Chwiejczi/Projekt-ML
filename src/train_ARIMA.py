from statsmodels.tsa.arima.model import ARIMA
from src.data_collection import *
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error,r2_score
import math
import matplotlib.pyplot as plt
import pandas as pd

def ts_arima_split(df, size):
    df=df["Close"]
    training_size=int(size)
    train=df.iloc[:training_size]
    test=df.iloc[training_size:]
    return train,test
if __name__ == "__main__":
    df=data_prep("GC=F","5y")
    #df=df["Close"]
    #we do it instantly, because we checked this in EDA
    df_diff=df["Close"].diff().dropna()

    #stationary check
    stationary_after_diff = adfuller(df_diff)
    print("\n\ncheck if time series is stationary after differential:")
    if stationary_after_diff[1] <= 0.05:
        print(f"stationary, p-value={stationary_after_diff[1]}")
    else:
        print(f"not stationary, p-value={stationary_after_diff[1]}")


    print(df)
    train,test = ts_arima_split(df,0.8 * len(df))

    #ARIMA model
    model = ARIMA(train,order=(1,1,1))
    fitted_model = model.fit()
    print("model1")
    print(fitted_model.summary())

    model2 = ARIMA(train,order=(0,1,0))
    fitted_model2= model2.fit()
    print("model2")
    print(fitted_model2.summary())

    model3 = ARIMA(train,order=(1,1,0))
    fitted_model3 = model3.fit()
    print("model3")
    print(fitted_model3.summary())

    model4 = ARIMA(train,order=(0,1,1))
    fitted_model4 = model4.fit()
    print("model4")
    print(fitted_model4.summary())

    #we take model4

    #y_pred=fitted_model4.forecast(steps=len(test))
    #print(len(test))
    #print(len(y_pred))
    history=train.copy()
    predictions=[]
    for t in range(len(test)):
        model = ARIMA(history, order=(0, 1, 1))
        fitted = model.fit()
        pred=fitted.forecast(steps=1)
        predictions.append(pred.iloc[0])
        history=pd.concat([history,test.iloc[t:t+1]])
    r2 = r2_score(test, predictions)
    print(f"R2 = {r2}")
    MSE = mean_squared_error(test, predictions)
    print(f"MSE = {MSE}, so it means that model's average fault is about {math.sqrt(MSE):.2f} ")

    plt.figure(figsize=(12, 6))

    plt.plot(test.index, test, label="True")
    plt.plot(test.index, predictions, label="Forecast")

    plt.legend()
    plt.grid(True)
    plt.show()