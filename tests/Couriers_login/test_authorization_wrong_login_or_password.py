from classes.class_test_courier_authorization import TestCourierAuthorization
import pytest

class TestAuthorizationWrongLoginOrPassword(TestCourierAuthorization):
    def test_wrong_login(self):
        # """Тест на проверку, что система вернёт ошибку, если неправильно указать логин"""
        
        payload = {
            "login": "wrong_login",
            "password": self.password
        }

        response = self.send_login_request(payload)

        assert response.status_code == 404, \
            f"Ожидался код 404 при неправильном логине, получен {response.status_code}"

    def test_wrong_password(self):
        # """Тест на проверку, что система вернёт ошибку, если неправильно указать пароль"""
        
        payload = {
            "login": self.login,
            "password": "wrong_password"
        }

        response = self.send_login_request(payload)

        assert response.status_code == 404, \
            f"Ожидался код 404 при неправильном пароле, получен {response.status_code}"