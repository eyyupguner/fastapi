from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTzpMf_ifwbgNjR0O4IaSnqz1_fd9TzKezLFehi9SJLpa-hs38qjh0Qr3wvXjcBez_25wnE4qufDtHr/pub?gid=0&single=true&output=csv'
df = pd.read_csv(url)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Veriyi sorgu yaparak al
    item_data = df[df["id"] == item_id].to_dict(orient="records")
    if item_data:
        return item_data[0]
    return {"message": "Ürün bulunamadı"}
