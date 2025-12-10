import pytest
import allure

class TestOrdersList:
    @pytest.mark.usefixtures("send_get_orders_request")
    @allure.title("Тест на проверку, что в теле ответа возвращается список заказов")
    def test_get_orders_list(self, send_get_orders_request):
        with allure.step("Отправляем запрос на получение списка заказов"):
            response = send_get_orders_request()

        with allure.step("Проверяем, что ответ содержит ожидаемый код 200"):
            assert response.status_code == 200, \
                f"Ожидался код 200 при получении списка заказов, получен {response.status_code}"

        with allure.step("Проверяем, что в теле ответа есть список заказов"):
            error_message = (
                f"Ожидался список заказов в ответе, получены: "
                f"response json - {response.json()}"
            )
            assert "orders" in response.json(), error_message
            assert isinstance(response.json()["orders"], list), \
                "Ожидалось, что 'orders' будет списком"