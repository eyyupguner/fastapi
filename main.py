from fastapi import FastAPI
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1Tq5KEhwBO9FSlcftABHNeFKmSBtVP2cMznapsgqrYzI/gviz/tq?tqx=out:csv&sheet=RH_C'
df = pd.read_csv(url)

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item": df.labels}
