import requests
import pytest
from helpers import generate_random_string

@pytest.fixture
def register_new_courier():
    # Генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

    assert response.status_code == 201 and "ok" in response.json() and response.json()["ok"] is True, \
        f"Ожидался код 201 и 'ok': true, получен {response.status_code} и {response.json()}"

    yield {"login": login, "password": password, "firstName": first_name}

    # Удаление курьера после теста
    delete_url = f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{login}"
    requests.delete(delete_url)

@pytest.fixture
def delete_courier():
    def _delete_courier(login):
        delete_url = f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{login}"
        response = requests.delete(delete_url)
        assert response.status_code == 200 and "ok" in response.json() and response.json()["ok"] is True, \
            f"Ожидался код 200 и 'ok': true, получен {response.status_code} и {response.json()}"
    return _delete_courier

@pytest.fixture
def send_login_request():
    def _send_login_request(payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        return response
    return _send_login_request

@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru/api/v1/orders"

@pytest.fixture
def send_create_order_request(base_url):
    def _send_create_order_request(payload):
        response = requests.post(base_url, json=payload)
        return response
    return _send_create_order_request

@pytest.fixture
def send_get_orders_request(base_url):
    def _send_get_orders_request(params=None):
        response = requests.get(base_url, params=params)
        return response
    return _send_get_orders_request