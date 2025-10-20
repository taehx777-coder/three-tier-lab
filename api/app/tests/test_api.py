from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_items_list_returns_seed_data():
    r = client.get("/items")
    assert r.status_code == 200
    data = r.json()
    # 최소 2개 시드 데이터가 있어야 함(first, second)
    names = [i["name"] for i in data]
    assert "first" in names and "second" in names
