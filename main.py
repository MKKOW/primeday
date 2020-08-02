from fastapi import FastAPI
from sympy import isprime
from datetime import date
import json

app = FastAPI()


@app.get("/")
def read_root() -> json:
    return json.dumps({'result': isprime(date.today().day)})
