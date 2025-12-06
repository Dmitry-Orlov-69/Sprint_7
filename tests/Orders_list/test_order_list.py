from classes.class_test_orders_list import TestOrdersList
import pytest

class TestOrderList(TestOrdersList):
    def test_get_orders_list(self):
        # """Тест на проверку, что в теле ответа возвращается список заказов"""
        
        response = self.send_get_orders_request()
        
        error_message = (
            f"Ожидался код 200 и список заказов в ответе, получены: "
            f"status code - {response.status_code}, "
            f"response json - {response.json()}"
        )
        assert response.status_code == 200 and "orders" in response.json() and isinstance(response.json()["orders"], list), error_message