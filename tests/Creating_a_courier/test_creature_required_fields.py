from classes.class_test_courier_creation import TestCourierCreation
import pytest

class TestCreatureRequiredFields(TestCourierCreation):
    def test_required_fields(self):
        # """Тест на проверку, что для создания курьера нужно передать все обязательные поля"""
        
        # Пытаемся создать курьера без указания некоторых полей
        payload_incomplete = {
            "login": "test_login",
            # password отсутствует
            "firstName": "test_name"
        }
        response_incomplete = self.send_create_courier_request(payload_incomplete)

        # Проверяем, что создание курьера завершилось ошибкой из-за отсутствия обязательных полей
        assert response_incomplete.status_code == 400, \
            f"Ожидался код 400 при отсутствии обязательных полей, получен {response_incomplete.status_code}"