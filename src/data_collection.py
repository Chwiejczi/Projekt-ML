import requests
import pandas as pd
from src.secret import *
import yfinance as yf


def get_response():
    api_key=get_api_key()
    url = f'https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=GOLD&interval=daily&apikey={api_key}'
    r = requests.get(url)
    return r
def data_prep(ticker,prd):
    gold = yf.download(tickers=ticker, period=prd)
    gold.columns = gold.columns.droplevel(1)
    gold = gold.reset_index()
    gold.columns.name = None
    return gold
def check_missing_values(df):
    return df.isnull().sum()

def data_imputation(df):
    df=df.interpolate()
    return df

def columns_to_delete(df,col_names):
    df=df.drop(col_names, axis=1)
    return df

def merge_df(dframes):
    res=pd.concat(dframes,join="inner",axis=1)
    return res



if __name__ == "__main__":

    gold=data_prep("GC=F","5y")
    #print(gold.tail())
    missingValues_gold = check_missing_values(gold)
    #print(missingValues_gold)
#
    oil=data_prep("CL=F","5y")
    #print(oil.tail())
    missingValues_oil = check_missing_values(oil)
    #print(missingValues_oil)
#
    usd = data_prep("USDEUR=X", "5y")
    #print(usd.tail())
#
    usd=columns_to_delete(usd,"Volume")
    #print(usd.tail())
    missingValues_usd = check_missing_values(usd)
    #print(missingValues_usd)
#
#
#
    ##merge_df
    df1=gold[["Date", "Open"]]
    df1=df1.set_index("Date")
    df1.rename(columns={"Open": "Open_gold"}, inplace=True)
    df2=oil[["Date", "Open"]]
    df2 = df2.set_index("Date")
    df2.rename(columns={"Open": "Open_oil"}, inplace=True)
    df3=usd[["Date", "Open"]]
    df3 = df3.set_index("Date")
    df3.rename(columns={"Open": "Open_usd"}, inplace=True)
#
    df=merge_df([df1,df2,df3])
    df=df.reset_index()
    #print("dataframe merged")
    #print(df)




