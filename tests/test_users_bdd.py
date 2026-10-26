
from pytest_bdd import scenarios, given, when, then

scenarios("features/users.feature")


@given("que la API está disponible")
def api_is_available(client):
    return client


@when(
    "envío los datos de un usuario nuevo",
    target_fixture="response",
)
def send_new_user(client):
    return client.post(
        "/users/",
        json={
            "name": "Usuario Gherkin",
            "email": "gherkin@example.com",
        },
    )


@then("la respuesta debe tener código 201")
def check_status_code(response):
    assert response.status_code == 201


@then("la respuesta debe incluir su nombre, correo e identificador")
def check_user_data(response):
    data = response.json()
    assert data["name"] == "Usuario Gherkin"
    assert data["email"] == "gherkin@example.com"
    assert isinstance(data["id"], int)
