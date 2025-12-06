from classes.class_test_courier_creation import TestCourierCreation
import pytest

class TestCreatureMissingField(TestCourierCreation):
    def test_missing_field(self):
        # """Тест на проверку, что если одного из полей нет, запрос возвращает ошибку"""
        
        # Пытаемся создать курьера без одного из обязательных полей
        payload_missing_field = {
            "login": "test_login",
            # firstName отсутствует
            "password": "test_password"
        }
        response_missing_field = self.send_create_courier_request(payload_missing_field)

        # Проверяем, что создание курьера завершилось ошибкой из-за отсутствия обязательных полей
        assert response_missing_field.status_code == 400, \
            f"Ожидался код 400 при отсутствии обязательных полей, получен {response_missing_field.status_code}"