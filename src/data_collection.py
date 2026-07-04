import requests
import pandas as pd
from src.secret import *
import yfinance as yf

def get_response():
    api_key=get_api_key()
    url = f'https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=GOLD&interval=daily&apikey={api_key}'
    r = requests.get(url)
    return r


if __name__ == "__main__":
    # print(r.status_code) miejsce na test
    #r = get_response()
    #data_all = r.json()

    #data_AU = data_all['data']
    #df_AU = pd.DataFrame.from_dict(data_AU)
    #print(df_AU.isna().sum())

    gold=yf.download("GC=F",period="5y")
    gold.columns=gold.columns.droplevel(1)
    gold=gold.reset_index()
    gold.columns.name=None
    print(gold.head())
    #print(gold.isna().sum())
    #print(gold.info())
    #print(type(gold))



