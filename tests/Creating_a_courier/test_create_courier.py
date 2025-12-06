from classes.class_test_courier_creation import TestCourierCreation, register_new_courier_and_return_login_password
import pytest

class TestCreateCourier(TestCourierCreation):
    def test_create_courier(self):
        # """Тест на создание курьера"""

        # Генерируем нового курьера
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = self.send_create_courier_request(payload)

        # Проверяем код ответа и тело ответа
        assert response.status_code == 201 and "ok" in response.json() and response.json()["ok"] is True, \
            f"Ожидался код 201 и 'ok': true, получен {response.status_code} и {response.json()}"