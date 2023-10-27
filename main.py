from fastapi import FastAPI
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTzpMf_ifwbgNjR0O4IaSnqz1_fd9TzKezLFehi9SJLpa-hs38qjh0Qr3wvXjcBez_25wnE4qufDtHr/pub?gid=0&single=true&output=csv'
df = pd.read_csv(url)

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item": df.labels}
