from fastapi.testclient import TestClient
from main import app, mean
import pytest
import json

client = TestClient(app)

def test_sort_mean():
    response = client.get("/restaurants/sort_mean")
    assert response.status_code == 200
    data = response.json()
    for r in data:
        assert mean(r) <= mean(list(data.keys())[0])

def test_sort_alpha():
    response = client.get("/restaurants/sort_alpha")
    assert response.status_code == 200
    data = response.json()
    first_entry_name = list(data.keys())[0]
    assert all(name > first_entry_name for name in list(data.keys())[1:])

def test_mean():
    response = client.get("/mean")
    assert response.status_code == 200
    data = response.json()
    mean_before = sum(grade for grade in data.values()) / len(data)
    grade_data = {
        "resto": "Le Great Escape",
        "name": "thomas",
        "grade": 1
    }
    response = client.post("/grade", json=grade_data)
    assert response.status_code == 200
    response = client.get("/mean")
    assert response.status_code == 200
    data = response.json()
    mean_after = sum(grade for grade in data.values()) / len(data)
    assert mean_after == pytest.approx(mean_before, abs=0.1)

def test_add_restaurant():
    response_before = client.get("/restaurants")
    assert response_before.status_code == 200
    data_before = response_before.json()
    num_restaurants_before = len(data_before)
    grade_data = {
        "resto": "test",
        "name": "thomas",
        "grade": 1
    }
    response = client.post("/grade", json=grade_data)
    assert response.status_code == 200

    response_after = client.get("/restaurants")
    assert response_after.status_code == 200
    data_after = response_after.json()
    num_restaurants_after = len(data_after)

    assert num_restaurants_after == num_restaurants_before + 1

def test_restaurants_data():
    response = client.get("/restaurants")
    assert response.status_code == 200
    data = response.json()
    expected_data = {
        "Bamee Bistro": [
            {"Alice": 4},
            {"Bob": 3},
            {"Claire": 5}
        ],
    }
    assert data["Bamee Bistro"] == expected_data["Bamee Bistro"]

def test_remove_testing_updates():
    print("Removing testing updates")
    response = client.get("/restaurants")
    assert response.status_code == 200
    data = response.json()
    for entry in data["Le Great Escape"]:
        if "thomas" in entry:
            data["Le Great Escape"].remove(entry)
            break
    for entry in data:
        if "test" in entry:
            del data[entry]
            break 
    assert "test" not in data
    assert "thomas" not in data["Le Great Escape"]
    with open("restaurants.json", "w") as f:
        json.dump(data, f, indent=4)