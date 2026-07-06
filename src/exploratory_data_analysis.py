import matplotlib.pyplot as plt
from data_collection import *
import numpy as np
from scipy.stats import norm,iqr
from scipy import stats

if __name__ == "__main__":
    #============GOLD=====================
    gold=data_prep("GC=F","5y")
    fig,(ax1,ax2,ax3)=plt.subplots(3,1)
    ax1.plot(gold["Date"],gold["Open"])
    ax1.set(xlabel='time',ylabel='Open values for gold')
    ax1.grid(True)
    corr=gold.corr()
    print(corr["Volume"])
    #no major correlation between volume and other


    # ============OIL======================
    oil=data_prep("CL=F","5y")
    #fig2,ax2=plt.subplots()
    ax2.plot(oil["Date"],oil["Open"])
    ax2.set(xlabel='time',ylabel='Open values for oil')
    ax2.grid(True)
    corr=oil.corr()
    print(corr["Volume"])
    # small negative correlation between volume and date

    # ============USD=====================
    usd=data_prep("USDEUR=X","5y")
    ax3.plot(usd["Date"],usd["Open"])
    ax3.set(xlabel='time',ylabel='Open values for usd')
    ax3.grid(True)
    usd = columns_to_delete(usd, "Volume")
    corr=usd.corr()
    print(corr)


    plt.show()

    #correlation between gold,usd,oil

    df1 = gold[["Date", "Open"]]
    df1 = df1.set_index("Date")
    df1.rename(columns={"Open": "Open_gold"}, inplace=True)

    df2 = oil[["Date", "Open"]]
    df2 = df2.set_index("Date")
    df2.rename(columns={"Open": "Open_oil"}, inplace=True)

    df3 = usd[["Date", "Open"]]
    df3 = df3.set_index("Date")
    df3.rename(columns={"Open": "Open_usd"}, inplace=True)

    df = merge_df([df1, df2, df3])
    df = df.reset_index()
    print("dataframe merged")
    print(df.tail())

    corr_df=df.corr()
    print("correlation matrix for oil,gold,usd")
    print(corr_df["Open_gold"])

    #percentage change
    print("percentage change- periad=1day")
    gold["pct_change_1day"]=gold["Open"].pct_change()
    print(gold.tail())

    #histogram pct_change
    mean=np.mean(gold["pct_change_1day"])
    sd=np.std(gold["pct_change_1day"])
    x=np.linspace(gold["pct_change_1day"].min(), gold["pct_change_1day"].max(), 100)
    print(f"mean={mean}, sd={sd}")
    plt.hist(gold["pct_change_1day"], bins=50,density=True,)
    plt.plot(x,norm.pdf(x,mean,sd),linewidth=2)
    plt.show()

    shapiro=stats.shapiro(gold["pct_change_1day"].dropna())
    #print(shapiro.pvalue)
    if shapiro.pvalue <=0.05:
        print(f"not normal distribution, p-value={shapiro}")
    else:
        print(f"normal distribution, p-value={shapiro}")

    #Shapiro-Wilk test said that the pct_change of gold price hasn't got normal distribution, what is really
    # normal in economical field. Max value is near 0, so a lot of values hasn't got big changes
    # , distribution looks similar to normal distribution,but it has fatter tails

    IQR=iqr(gold["pct_change_1day"].dropna())
    print(f"IQR={IQR}")
    #it says that 50% of the values are in 1.15% breadth. Values outside this range are possible outliers


    #============Lags==================

    gold["lag_1_pct"]=gold["pct_change_1day"].shift(1)
    print("values with lag")
    print(gold.tail())

    corr_lag = gold[["lag_1_pct", "pct_change_1day"]].dropna().corr()
    print(corr_lag)

    #pct_change changes dont depends on past values

