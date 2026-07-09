import pyodbc

def insert_gold_price(date,price):
    cursor.execute("""Insert into gold_prices(Stock_Date,price)  
                   values(?,?)   
                   """,date,price)
    conn.commit()

def load_gold_prices():
    cursor.execute("""Select * from gold_prices ORDER BY Stock_Date""")
    return cursor.fetchall()

def insert_predictions(date,pred_price):
    cursor.execute("""Insert into gold_predictions(Prediction_date,Predicted_price, Name_Model)  
                   values(?,?,?)   
                   """,date,pred_price,"ARIMA")
    conn.commit()

def load_predictions():
    cursor.execute("""Select * from gold_predictions ORDER BY Predicted_Date""")
    return cursor.fetchall()


DRIVER_NAME="SQL Server"
SERVER_NAME="DESKTOP-G28JJ96\SQLEXPRESS"
DATABASE_NAME="Predictor_db"

#print(pyodbc.drivers())

connection_string=(f"DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};  Trusted_Connection=yes"
)
conn=pyodbc.connect(connection_string)
print(conn)

cursor=conn.cursor()