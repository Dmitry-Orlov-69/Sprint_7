from classes.class_test_courier_creation import TestCourierCreation, register_new_courier_and_return_login_password
import pytest

class TestIdenticalCouriers(TestCourierCreation):
    def test_cannot_create_identical_couriers(self):
        # """Тест на проверку, что нельзя создать двух одинаковых курьеров"""
        
        # Генерируем нового курьера
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Создаём первого курьера
        response_first = self.send_create_courier_request(payload)

        # Пытаемся создать второго курьера с теми же данными
        response_second = self.send_create_courier_request(payload)

        # Проверяем, что первый курьер был успешно создан и создание второго курьера завершилось ошибкой
        assert response_first.status_code == 201 and response_second.status_code == 409, \
            f"Ожидался код 201 для первого курьера и 409 для второго, получены {response_first.status_code} и {response_second.status_code}"