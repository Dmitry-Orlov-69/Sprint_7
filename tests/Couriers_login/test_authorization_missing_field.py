from classes.class_test_courier_authorization import TestCourierAuthorization
import pytest

class TestAuthorizationMissingField(TestCourierAuthorization):
    def test_missing_login(self):
        # """Тест на проверку, что при отсутствии логина возвращается ошибка"""
        
        payload = {
            "password": self.password
        }

        response = self.send_login_request(payload)

        assert response.status_code == 400, \
            f"Ожидался код 400 при отсутствии логина, получен {response.status_code}"

    def test_missing_password(self):
        # """Тест на проверку, что при отсутствии пароля возвращается ошибка"""
        
        payload = {
            "login": self.login
        }

        response = self.send_login_request(payload)

        assert response.status_code == 400, \
            f"Ожидался код 400 при отсутствии пароля, получен {response.status_code}"