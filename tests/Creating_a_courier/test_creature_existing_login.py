from classes.class_test_courier_creation import TestCourierCreation, register_new_courier_and_return_login_password
import pytest

class TestCreatureExistingLogin(TestCourierCreation):
    def test_existing_login(self):
        # """Тест на проверку, что если создать пользователя с логином, который уже есть, возвращается ошибка"""
        
        # Генерируем нового курьера
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Создаём первого курьера с уникальным логином
        response_first = self.send_create_courier_request(payload)

        # Пытаемся создать второго курьера с тем же логином
        response_second = self.send_create_courier_request(payload)

        # Проверяем, что создание первого курьера прошло успешно и создание второго курьера завершилось ошибкой из-за повторяющегося логина
        assert response_first.status_code == 201 and response_second.status_code == 409, \
            f"Ожидался код 201 для первого курьера и 409 для второго, получены {response_first.status_code} и {response_second.status_code}"