from fastapi import FastAPI
from datetime import date
import json


def isprime(number: int) -> bool:
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i*i < number:
        if number % i == 0:
            return False
        i += 2
    return True


app = FastAPI()


@app.get("/")
def read_root() -> json:
    return {'result': isprime(date.today().day)}
