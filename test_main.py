
from fastapi.testclient import TestClient
from main import app

# Create test client
client = TestClient(app)

# Test 1: Normal subtraction
def test_subtraction():
    response = client.post(
        "/subtract",
        json={"num1": 20, "num2": 10}
    )

    assert response.status_code == 200
    assert response.json()["subtraction"] == 10


# Test 2: Subtraction with negative result
def test_negative_result():
    response = client.post(
        "/subtract",
        json={"num1": 10, "num2": 20}
    )

    assert response.status_code == 200
    assert response.json()["subtraction"] == -10


# Test 3: Subtraction with decimal values
def test_decimal_subtraction():
    response = client.post(
        "/subtract",
        json={"num1": 15.5, "num2": 5.5}
    )

    assert response.status_code == 200
    assert response.json()["subtraction"] == 10


# Test 4: Subtraction of equal numbers
def test_equal_numbers():
    response = client.post(
        "/subtract",
        json={"num1": 10, "num2": 10}
    )

    assert response.status_code == 200
    assert response.json()["subtraction"] == 0


# Test 5: Invalid input
def test_invalid_input():
    response = client.post(
        "/subtract",
        json={"num1": "abc", "num2": 10}
    )

    assert response.status_code == 422
