"""
Main application module for FastAPI.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: float, b: float):
    """return the result after addition"""
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: float, b: float):
    """return the result after multiply"""
    return {"result": a * b}


