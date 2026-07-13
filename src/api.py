from fastapi import FastAPI
from src.data_base import *

app = FastAPI()
@app.get("/")
def root():
    latest_pred = last_pred()[0]
    latest_date = latest_pred[1]
    latest_value = latest_pred[2]
    return {"Predicted date":latest_date,"Predicted value":latest_value}

@app.get("/message")
def get_message():
    return {"message":"Gold Price prediction API"}

@app.get("/goldValues")
def get_gold_values():
    top_30=load_all_gold()[:30]
    dict_top_30 = {x[1]: x[2] for x in top_30}
    return dict_top_30

