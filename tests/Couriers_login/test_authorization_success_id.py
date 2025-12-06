from classes.class_test_courier_authorization import TestCourierAuthorization
import pytest

class TestAuthorizationSuccessId(TestCourierAuthorization):
    def test_successful_authorization_returns_id(self):
        # """Тест на проверку, что успешный запрос на авторизацию возвращает id курьера"""
        
        payload = {
            "login": self.login,
            "password": self.password
        }

        response = self.send_login_request(payload)

        error_message = (
            f"Ожидался код 200 и наличие 'id' в ответе, получены: "
            f"status code - {response.status_code}, "
            f"response json - {response.json()}"
        )
        assert response.status_code == 200 and "id" in response.json(), error_message