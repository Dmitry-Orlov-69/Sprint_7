from classes.class_test_courier_creation import TestCourierCreation, register_new_courier_and_return_login_password
import pytest

class TestCreatureOkTrue(TestCourierCreation):
    def test_ok_true(self):
        # """Тест на проверку, что успешный запрос возвращает {'ok': True}"""
        
        # Генерируем нового курьера
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Отправляем запрос на создание курьера
        response = self.send_create_courier_request(payload)

        # Проверяем, что ответ содержит ожидаемый код 201 и {"ok": True}
        assert response.status_code == 201 and response.json()["ok"] is True, \
            f"Ожидался код 201 и 'ok': True при создании курьера, получены {response.status_code} и {response.json()}"