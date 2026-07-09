#Gold price prediction project: 
Machine learning project focused on predicting gold price 

#Technologies:  
Python 
Docker 
FastAPI(planned)
requests
pandas
pytest
yfinance
matplotlib  
numpy
scipy
statsmodels
#Project Status: 
In progress 

##database
In SQL Server Management Studio execute file database/init.sql , then database will be ready to use

#conclusions  
8.07.2026
Training proces showed that it is very difficult to 
predict real glold price value, depending on only financial 
aspects. Random Forest Regressor showed the inabilty 
of tree-based models to extrapolate beyond traning data 

8.07.2026 
After experimenting with traditional machine learning approach  
(analyzing and transforming data with  Random Forest Regression), 
we turned this project towards time series modeling 
with usage of ARIMA model. It is very effective when 
it comes to predict values in the nearest future and  
it is based only on actual values from stock, unlike  
to Random Forest it bases on historical values and 
require less feature engineering.
