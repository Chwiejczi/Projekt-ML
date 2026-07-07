from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from feature_engineering import prepare_main_df
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

df=prepare_main_df()
#print(df.info())
#random forest doesnt take Date as a feature, so we need to delete it
X=df.drop(["Target","Date"],axis=1)
y=df["Target"]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=100)

print(f"Xtrain = {X_train.shape}, Xtest = {X_test.shape}")
print(f"ytrain = {y_train.shape}, ytest = {y_test.shape}")

classifier = RandomForestRegressor(random_state=100,n_estimators=100)
classifier.fit(X_train,y_train)

r2=classifier.score(X_test,y_test)
print(f"R2 = {r2}")
MSE=mean_squared_error(y_test,classifier.predict(X_test))
print(f"MSE = {MSE}, so it means that model's average fault is about {math.sqrt(MSE):.2f} ")





