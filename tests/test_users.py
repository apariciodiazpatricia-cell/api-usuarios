
def test_create_user_returns_201_and_user_data(client):
    response = client.post(
        "/users/",
        json={
            "name": "Usuario de prueba",
            "email": "prueba.automatizada@example.com",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Usuario de prueba"
    assert data["email"] == "prueba.automatizada@example.com"
    assert isinstance(data["id"], int)


def test_create_user_with_duplicate_email_returns_409(client):
    user_data = {
        "name": "Usuario de prueba",
        "email": "duplicado@example.com",
    }

    first_response = client.post("/users/", json=user_data)
    second_response = client.post("/users/", json=user_data)

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == (
        "Este correo electrónico ya está registrado"
    )
