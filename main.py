
from fastapi import FastAPI

app = FastAPI(title="Worknest API")


@app.get("/")
def home():
    return {
        "message": "Welcome to Worknest!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
