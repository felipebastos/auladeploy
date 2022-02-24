import pytest
from flask_app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_request_to_slash(client):
    response = client.get("/")
    assert b"Valeu" in response.data


def test_request_to_slash_pink(client):
    response = client.get("/pink")
    assert b"mais uma vez" in response.data


def test_request_slash_nova(client):
    response = client.get("/nova")
    assert b"nova" in response.data
