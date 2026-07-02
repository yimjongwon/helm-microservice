# main.py (for fastapi-market)
from fastapi import FastAPI

app = FastAPI()

SERVICE = "market-app"

@app.get("/market")
def read_market():
    return {
        "title":"market api",
        "products": [
            {"id": 1, "name": "아이폰", "price": "품절"},
            {"id": 2, "name": "안드로이드", "price": "0원"}
        ]
    }

@app.get("/health")
def health():
    return{"service":SERVICE, "message":"market service is running"}