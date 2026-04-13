from service.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
def test_create_account():
    client = app.test_client()
    data = {"name": "Mutiara"}
    response = client.post("/accounts", json=data)
    assert response.status_code == 201

def test_get_accounts():
    client = app.test_client()
    response = client.get("/accounts")
    assert response.status_code == 200
def test_get_account_by_id():
    client = app.test_client()
    client.post("/accounts", json={"name": "Test"})
    response = client.get("/accounts/0")
    assert response.status_code == 200
