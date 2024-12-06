from fastapi.testclient import TestClient
from main import app
from db_tiny.tinyDB import tinydb_form

client = TestClient(app=app)


def test_tinydb():
    assert len(tinydb_form()) >= 0


def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"massage": "Hello index!"}


def test_post_user_true_request():
    user_true = {
        "phone": "+79645226237",
        "test": "01.01.1985",
        "birth_date": "01.01.1985",
        "email": "test@example.com",
    }
    response = client.post("/", json=user_true)
    assert response.status_code == 200
    assert response.json() == "Model: User"
    print(response.json())


def test_post_company_true_request():
    company_true = {
        "company_phone": "+79645226237",
        "test": "01.01.1985",
        "profile": "01.01.1985",
        "company_email": "test@example.com",
    }
    response = client.post("/", json=company_true)
    assert response.status_code == 200
    assert response.json() == "Model: Company"
    print(response.json())


def test_post_user_false_request():
    user_false = {
        "phone": "+7964521256237",
        "test": "01.01.1985",
        "birth_date": "01.011985",
        "email": "test@examplecom",
    }
    response = client.post("/", json=user_false)
    assert response.status_code == 200
    assert response.json() == {
        "birth_date": "str",
        "email": "str",
        "phone": "str",
        "test": "data",
    }
    print(response.json())


def test_post_company_false_request():
    company_false = {
        "company_phone": "+796452256237a",
        "test": "01.01.1985",
        "profile": "01.021.1985",
        "company_email": "testexample.com",
    }
    response = client.post("/", json=company_false)
    assert response.status_code == 200
    assert response.json() == {
        "company_email": "str",
        "company_phone": "str",
        "profile": "str",
        "test": "data",
    }
    print(response.json())


def test_post_noname_request():
    noname = {
        "test_phone": "+79645226237",
        "test_str": "String",
        "test_date": "01.01.1985",
        "test_email": "test@example.com",
    }
    response = client.post("/", json=noname)
    assert response.status_code == 200
    assert response.json() == {
        "test_date": "data",
        "test_email": "email",
        "test_phone": "phone",
        "test_str": "str",
    }
    print(response.json())
