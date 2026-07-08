from src.data_collection import *
import datetime as dt



def prepare_main_df():
    gold=data_prep("GC=F","5y")
    oil = data_prep("CL=F", "5y")
    usd = data_prep("USDEUR=X", "5y")
    gold["Target"]=gold["Close"].shift(-1)

    gold.rename(columns={'Close': 'Close_gold'}, inplace=True)
    oil.rename(columns={'Close': 'Close_oil'}, inplace=True)
    usd.rename(columns={'Close': 'Close_usd'}, inplace=True)

    gold["MA"] = gold["Close_gold"].rolling(window=20).mean()

    gold["pct_change_1day_gold"]=gold["Close_gold"].pct_change()
    oil["pct_change_1day_oil"] = oil["Close_oil"].pct_change()
    usd["pct_change_1day_usd"] = usd["Close_usd"].pct_change()

    gold["lag_1_pct_gold"]=gold["pct_change_1day_gold"].shift(1)
    oil["lag_1_pct_oil"] = oil["pct_change_1day_oil"].shift(1)
    usd["lag_1_pct_usd"] = usd["pct_change_1day_usd"].shift(1)

    usd=usd.drop(["High","Low","Open","Volume"],axis=1)
    oil=oil.drop(["High","Low","Open","Volume"],axis=1)

    gold=gold.set_index("Date")
    oil=oil.set_index("Date")
    usd=usd.set_index("Date")

    df = merge_df([gold, oil, usd])
    df = df.reset_index()
    #df["Target"]=gold["Close_gold"].shift(-1)

    df = data_imputation(df)
    df=df.dropna()
    return df




if __name__ == "__main__":

    df=prepare_main_df()
    print(df.tail())
    print(check_missing_values(df))