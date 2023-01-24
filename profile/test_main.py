from fastapi.testclient import TestClient
from starlette import status
from time import perf_counter
from motor.motor_asyncio import AsyncIOMotorClient

from .main import app


TEST_MONGO_URL = 'mongodb://localhost:27017'
test_client = AsyncIOMotorClient(TEST_MONGO_URL)
SQLALCHEMY_SILENCE_UBER_WARNING = 1

override_database = test_client.test_db

client = TestClient(app)
response_time = .1


def setup_profile():
    data = {"user": "string", "follows": "string"}
    response = client.post("/profile/", json=data)
    return response.json()


def test_get_profile():
    end = perf_counter()
    response = client.get("/profile/")
    start = perf_counter()
    assert end - start <= response_time
    assert response.status_code == status.HTTP_200_OK
    assert bool(response.json())


def test_create_profile():
    end = perf_counter()
    response = client.post("/profile/", json={"user": "string", "follows": "string"})
    start = perf_counter()
    assert end - start <= response_time
    assert response.status_code == status.HTTP_201_CREATED


def test_get_particular_profile():
    profile = setup_profile()
    end = perf_counter()
    response = client.get(f'/profile/{profile.get("id")}/')
    start = perf_counter()
    assert end - start <= response_time
    assert response.status_code == status.HTTP_200_OK


def test_delete_profile():
    profile = setup_profile()
    end = perf_counter()
    response = client.delete(f'/profile/{profile.get("id")}/')
    start = perf_counter()
    assert end - start <= response_time
    assert response.status_code == status.HTTP_204_NO_CONTENT
