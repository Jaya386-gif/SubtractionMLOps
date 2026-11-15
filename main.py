
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI(title="Subtraction API")

# Define input structure
class Numbers(BaseModel):
    num1: float
    num2: float

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Subtraction API"}

# Subtraction operation
@app.post("/subtract")
def subtract(numbers: Numbers):
    result = numbers.num1 - numbers.num2

    return {
        "num1": numbers.num1,
        "num2": numbers.num2,
        "subtraction": result
    }
