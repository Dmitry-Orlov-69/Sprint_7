import pytest
import allure
from data import test_data

class TestOrderCreation:
    @pytest.mark.parametrize("color", ["BLACK", "GREY"])
    @allure.title("Тест на проверку, что при создании заказа можно указать один из цветов — BLACK или GREY")
    def test_order_with_one_color(self, send_create_order_request, color):
        with allure.step("Формируем payload для создания заказа с указанным цветом"):
            payload = {
                **test_data,
                "color": [color]
            }

        with allure.step("Отправляем запрос на создание заказа"):
            response = send_create_order_request(payload)

        with allure.step("Проверяем, что ответ содержит ожидаемый код 201 и track в теле ответа"):
            assert response.status_code == 201, \
                f"Ожидался код 201 при создании заказа с цветом {color}, получен {response.status_code}"
            assert "track" in response.json(), \
                "Ожидалось наличие 'track' в ответе"

    @allure.title("Тест на проверку, что при создании заказа можно указать оба цвета — BLACK и GREY")
    def test_order_with_both_colors(self, send_create_order_request):
        with allure.step("Формируем payload для создания заказа с обоими цветами"):
            payload = {
                **test_data,
                "color": ["BLACK", "GREY"]
            }

        with allure.step("Отправляем запрос на создание заказа"):
            response = send_create_order_request(payload)

        with allure.step("Проверяем, что ответ содержит ожидаемый код 201 и track в теле ответа"):
            assert response.status_code == 201, \
                f"Ожидался код 201 при создании заказа с цветами BLACK и GREY, получен {response.status_code}"
            assert "track" in response.json(), \
                "Ожидалось наличие 'track' в ответе"

    @allure.title("Тест на проверку, что при создании заказа можно не указывать цвет")
    def test_order_without_color(self, send_create_order_request):
        with allure.step("Формируем payload для создания заказа без указания цвета"):
            payload = test_data

        with allure.step("Отправляем запрос на создание заказа"):
            response = send_create_order_request(payload)

        with allure.step("Проверяем, что ответ содержит ожидаемый код 201 и track в теле ответа"):
            assert response.status_code == 201, \
                f"Ожидался код 201 при создании заказа без указания цвета, получен {response.status_code}"
            assert "track" in response.json(), \
                "Ожидалось наличие 'track' в ответе"

    @allure.title("Тест на проверку, что тело ответа при создании заказа содержит track")
    def test_order_contains_track(self, send_create_order_request):
        with allure.step("Формируем payload для создания заказа"):
            payload = test_data

        with allure.step("Отправляем запрос на создание заказа"):
            response = send_create_order_request(payload)

        with allure.step("Проверяем, что ответ содержит ожидаемый код 201 и track в теле ответа"):
            error_message = (
                f"Ожидался код 201 и наличие 'track' в ответе, получены: "
                f"status code - {response.status_code}, "
                f"response json - {response.json()}"
            )
            assert response.status_code == 201 and "track" in response.json(), error_message