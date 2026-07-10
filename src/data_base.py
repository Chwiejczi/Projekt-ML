import pyodbc

def insert_gold_price(date,price):
    cursor.execute("""Insert into gold_prices(Stock_Date,price)  
                   values(?,?)   
                   """,date,price)
    conn.commit()

def load_gold_prices():
    cursor.execute("""Select Price from gold_prices ORDER BY Stock_Date""")
    return cursor.fetchall()

def insert_predictions(date,pred_price):
    cursor.execute("""Insert into gold_predictions(Prediction_Date,Predicted_Price, Name_Model)  
                   values(?,?,?)   
                   """,date,pred_price,"ARIMA")
    conn.commit()

def load_predictions():
    cursor.execute("""Select * from gold_predictions ORDER BY Prediction_Date""")
    return cursor.fetchall()

def clear_gold_prices():
    cursor.execute("""
        Delete from gold_prices
    """)
    conn.commit()

def clear_gold_preds():
    cursor.execute("""
        Delete from gold_predictions
    """)
    conn.commit()

def date_in_database(date):
    cursor.execute("""
        select count(*) from gold_prices where Stock_Date=?
    """,date)
    count=cursor.fetchone()[0]#it return a tuple ex. (1,) , we need only 1st elem
    return bool(count)


def date_in_gold_pred(date):
    cursor.execute("""
        select count(*) from gold_predictions where Prediction_Date =?
    """,date)


    count=cursor.fetchone()[0]#it return a tuple ex. (1,) , we need only 1st elem
    return bool(count)

DRIVER_NAME="SQL Server"
SERVER_NAME="DESKTOP-G28JJ96\SQLEXPRESS"
DATABASE_NAME="Predictor_db"

#print(pyodbc.drivers())

connection_string=(f"DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};  Trusted_Connection=yes"
)
conn=pyodbc.connect(connection_string)
print(conn)

cursor=conn.cursor()