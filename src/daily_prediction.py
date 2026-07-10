from src.data_collection import *
from src.data_base import *
from train_ARIMA import *
from datetime import datetime,timedelta
def run_daily_pipeline():
    #df=data_prep("GC=F","5y")
    #latest=df.iloc[-1]
    data=get_latest_value_from_API()
    date=data['date']
    if date_in_database(date):
        pass
    else:
        insert_gold_price(date,float(data["price"]))

if __name__=="__main__":
    clear_gold_preds()
    #check if stock updated values
    #stock doesnt work during weekends
    weekno = datetime.today().weekday()
    if weekno in [5,6]:
        pass
    else:
        run_daily_pipeline()
        ARIMA_params = (0, 1, 1)
        history = load_gold_prices()
        pred_val = ARIMA_pred(history, ARIMA_params)
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow = tomorrow.strftime("%Y-%m-%d")

        #ensure that we will not make duplicates
        if not date_in_gold_pred(tomorrow):
            insert_predictions(tomorrow,pred_val[0])

    print(load_predictions())




