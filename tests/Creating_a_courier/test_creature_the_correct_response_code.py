from classes.class_test_courier_creation import TestCourierCreation, register_new_courier_and_return_login_password
import pytest

class TestCreatureTheCorrectResponseCode(TestCourierCreation):
    def test_correct_response_code(self):
        # """Тест на проверку, что запрос возвращает правильный код ответа"""
        
        # Генерируем нового курьера
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Отправляем запрос на создание курьера
        response = self.send_create_courier_request(payload)

        # Проверяем, что ответ содержит ожидаемый код 201
        assert response.status_code == 201, \
            f"Ожидался код 201 при создании курьера, получен {response.status_code}"