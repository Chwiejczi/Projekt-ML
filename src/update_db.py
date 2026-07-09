from src.data_collection import *
from src.data_base import *
import pyodbc

if __name__ =='__main__':
    #insert data form yfinance to db
    DRIVER_NAME = "SQL Server"
    SERVER_NAME = "DESKTOP-G28JJ96\SQLEXPRESS"
    DATABASE_NAME = "Predictor_db"

    connection_string = (f"DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};  Trusted_Connection=yes"
    )
    conn = pyodbc.connect(connection_string)
    print(conn)
    df = data_prep("GC=F", "5y")

    clear_gold_prices()

    for index, row in df.iterrows():
        #print(row["Close"], row["Open"])
        insert_gold_price(row["Date"],row["Close"])

    print(load_gold_prices())
