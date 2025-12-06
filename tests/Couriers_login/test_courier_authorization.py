from classes.class_test_courier_authorization import TestCourierAuthorization
import pytest

class TestCourierCanAuthorize(TestCourierAuthorization):
    def test_courier_can_authorize(self):
        # """Тест на проверку, что курьер может авторизоваться"""
        
        # Получаем данные для авторизации курьера
        login, password = self.login, self.password

        payload = {
            "login": login,
            "password": password
        }

        # Отправляем запрос на авторизацию курьера
        response = self.send_login_request(payload)

        # Проверяем, что ответ содержит ожидаемый код 200 и id курьера
        assert response.status_code == 200 and "id" in response.json(), \
            f"Ожидался код 200 и наличие id в ответе, получены {response.status_code} и {response.json()}"