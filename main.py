from fastapi import FastAPI
import schemas, models
from database import engine

app = FastAPI()
models.Base.metadata.create_all(engine)

@app.get("/")
def home():
    return "home"


@app.post("/transactions")
def transaction(request: schemas.Transaction):
    return request