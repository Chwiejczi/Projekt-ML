IF DB_ID('Predictor_db') IS NOT NULL
BEGIN
    DROP DATABASE Predictor_db;
END
GO

Create Database Predictor_db;
go

use Predictor_db;
go

Create table gold_prices(
ID int IDENTITY(1,1) NOT null primary key,
Stock_Date DATE not null unique,
price Float not null
);

Create table gold_predictions(
ID int IDENTITY(1,1) NOT null primary key,
Prediction_date Date not null,
Predicted_price float not null,
Name_Model VARCHAR(30) not null
);


