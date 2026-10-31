from ciapp.app import add, app


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index_returns_message():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from the Skillsforge CI demo"


def test_add_endpoint_rejects_bad_input():
    client = app.test_client()
    response = client.get("/add?a=two&b=3")
    assert response.status_code == 400
