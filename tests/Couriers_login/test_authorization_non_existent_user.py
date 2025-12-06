from classes.class_test_courier_authorization import TestCourierAuthorization
import pytest

class TestAuthorizationNonExistentUser(TestCourierAuthorization):
    def test_non_existent_user(self):
        # """Тест на проверку, что при авторизации под несуществующим пользователем возвращается ошибка"""
        
        payload = {
            "login": "non_existent_login",
            "password": "non_existent_password"
        }

        response = self.send_login_request(payload)

        assert response.status_code == 404, \
            f"Ожидался код 404 при попытке авторизации несуществующим пользователем, получен {response.status_code}"