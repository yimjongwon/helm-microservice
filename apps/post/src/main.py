
from fastapi import FastAPI

app = FastAPI()

SERVICE = "post-app"

@app.get("/posts")
def read_posts():
    return {
        "title":"post api",
        "articles": [
            {"num": 77, "title": "감격", "writer": "수강생B"},
            {"num": 78, "title": "질문", "writer": "주니어"}
        ]
    }

@app.get("/health")
def health():
    return{"service":SERVICE, "message":"post service is running"}