
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from src.feature_engineering import prepare_main_df
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import math


def ts_train_test_split(training_size,df):
    training_size=int(training_size)
    train=df.iloc[:training_size]
    test=df.iloc[training_size:]
    X_train=train.drop(columns=["Target","Date"])
    y_train=train["Target"]
    X_test=test.drop(columns=["Target","Date"])
    y_test=test["Target"]
    return X_train,X_test,y_train,y_test


df=prepare_main_df()
#print(df.info())
#random forest doesnt take Date as a feature, so we need to delete it
X=df.drop(["Target","Date"],axis=1)
y=df["Target"]

X_train, X_test, y_train, y_test=ts_train_test_split(0.8*df.shape[0],df)

print(f"Xtrain = {X_train.shape}, Xtest = {X_test.shape}")
print(f"ytrain = {y_train.shape}, ytest = {y_test.shape}")

classifier = RandomForestRegressor(random_state=100,n_estimators=100)
classifier.fit(X_train,y_train)

#r2=classifier.score(X_test,y_test)
r2=r2_score(y_test,classifier.predict(X_test))
print(f"R2 = {r2}")
MSE=mean_squared_error(y_test,classifier.predict(X_test))
print(f"MSE = {MSE}, so it means that model's average fault is about {math.sqrt(MSE):.2f} ")


print(f"Train range:{ y_train.min()}, {y_train.max()}")
print(f"Test range:{ y_test.min()}, {y_test.max()}")

